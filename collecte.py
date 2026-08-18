#!/usr/bin/env python3
# ── Collecte des mesures, dans le nuage ─────────────────────────────────
#
# Pourquoi ce fichier existe : la station Helio-Watch tourne sur un PC qui
# n'est pas allume en permanence. Tant que la collecte vit sur cette machine,
# PC eteint = trou dans l'historique.
#
# L'idee qui rend la chose facile : LES FLUX PORTENT LEUR PROPRE FENETRE.
# Mesure faite le 2026-08-18 :
#
#     vent solaire      23,9 h a la minute   (1395 points)
#     champ magnetique  23,9 h a la minute   (1438 points)
#     Kp                 6,0 h a la minute
#     rayons X           6,0 h
#     seismes (all_day) 24 h
#     F10.7             cadence lente, 60 releves
#
# Il ne faut donc PAS interroger toutes les minutes pour avoir une resolution
# a la minute : il suffit de passer assez souvent pour que les fenetres se
# chevauchent. Toutes les 4 heures laisse une marge confortable meme sur la
# plus courte (6 h), ce qui absorbe les retards de GitHub — les taches
# planifiees y sont couramment repoussees de 5 a 20 minutes, parfois sautees.
#
# Aucun modele n'intervient ici. C'est un script : ce qui sort du flux est ce
# qui est ecrit, sans recopie ni interpretation. La seule autre entree du
# projet produite par un agent (veille.json) reste distincte et etiquetee
# comme telle a l'ecran.
#
# L'ISS est volontairement absente : wheretheiss.at ne rend que la position
# instantanee, sans fenetre. A 4 h d'intervalle on obtiendrait des points sans
# rapport les uns avec les autres, pas une trace. Elle reste construite en
# local, quand la station tourne.

import json, gzip, io, sys, os, re, urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

RACINE  = Path(__file__).resolve().parent
MESURES = RACINE / "mesures"
UA = "helio-watch-collecte/1.0 (+https://github.com/lacrimoiza7-lab/helio-veille)"


# ── Telechargement ──────────────────────────────────────────────────────

def telecharge(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept-Encoding": "gzip", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        brut = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            brut = gzip.decompress(brut)
    return json.loads(brut.decode("utf-8", "replace"))


def iso(s):
    """Les flux datent en '2026-08-18T14:20:00' sans fuseau, mais c'est de
    l'UTC. Le laisser naif ferait interpreter l'heure comme locale au moment
    de relire l'historique — soit un decalage silencieux de plusieurs heures.
    On pose le fuseau explicitement, toujours."""
    if not s:
        return None
    s = str(s).strip().replace(" ", "T").replace("Z", "")
    s = re.sub(r"\.\d+$", "", s)
    for f in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M"):
        try:
            return datetime.strptime(s, f).replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    return None


# ── Reducteurs ──────────────────────────────────────────────────────────
# Chacun rend une liste de (instant, valeurs). L'instant est celui de la
# MESURE, jamais celui de la collecte : c'est toute la difference entre un
# historique a la minute et six points par jour.

def _rtsw(champs):
    def f(brut):
        # rtsw_wind_1m contient TROIS sondes (SOLAR1/ACE/IMAP), une seule
        # active. Les melanger produirait des sauts qu'on lirait comme des
        # evenements. On garde l'active, et on note laquelle.
        actifs = [x for x in brut if x.get("active")] or brut
        out = []
        for x in actifs:
            t = iso(x.get("time_tag"))
            if not t:
                continue
            v = {c: x.get(c) for c in champs}
            v["sonde"] = x.get("source")
            out.append((t, v))
        return out
    return f


def _kp(brut):
    return [(iso(x.get("time_tag")),
             {"kp_index": x.get("kp_index"), "estimated_kp": x.get("estimated_kp")})
            for x in brut if iso(x.get("time_tag"))]


def _rayons_x(brut):
    # Deux bandes coexistent dans le meme fichier ; la bande longue
    # (0.1-0.8 nm) est celle qui definit la classe d'eruption.
    out = []
    for x in brut:
        t = iso(x.get("time_tag"))
        if t and str(x.get("energy", "")).startswith("0.1"):
            out.append((t, {"flux": x.get("flux"), "satellite": x.get("satellite")}))
    return out


def _f107(brut):
    return [(iso(x.get("time_tag")), {"flux": x.get("flux")})
            for x in brut if iso(x.get("time_tag"))]


def _seismes(brut):
    # Un seisme est un EVENEMENT, pas un echantillon : on l'indexe par son
    # identifiant USGS et son heure d'origine, pas par l'heure de collecte.
    out = []
    for f in brut.get("features") or []:
        p = f.get("properties") or {}
        g = (f.get("geometry") or {}).get("coordinates") or [None, None, None]
        ms = p.get("time")
        if not ms:
            continue
        out.append((datetime.fromtimestamp(ms / 1000, timezone.utc), {
            "id": f.get("id"), "mag": p.get("mag"), "lieu": p.get("place"),
            "lon": g[0], "lat": g[1], "profondeur_km": g[2],
        }))
    return out


def _aurore(brut):
    # Instantane sans fenetre : un seul point par collecte. On ne garde que
    # le total, la grille complete (922 ko) n'a pas sa place dans un historique.
    t = iso(brut.get("Observation Time") or brut.get("observation_time"))
    if not t:
        return []
    pts = brut.get("coordinates") or []
    return [(t, {"cellules_5pc": sum(1 for c in pts if len(c) > 2 and c[2] >= 5),
                 "total": len(pts)})]


SOURCES = {
    "vent": ("https://services.swpc.noaa.gov/json/rtsw/rtsw_wind_1m.json",
             _rtsw(["proton_speed", "proton_density", "proton_temperature"])),
    "mag": ("https://services.swpc.noaa.gov/json/rtsw/rtsw_mag_1m.json",
            _rtsw(["bt", "bx_gsm", "by_gsm", "bz_gsm"])),
    "kp": ("https://services.swpc.noaa.gov/json/planetary_k_index_1m.json", _kp),
    "rayons_x": ("https://services.swpc.noaa.gov/json/goes/primary/xrays-6-hour.json",
                 _rayons_x),
    "f107": ("https://services.swpc.noaa.gov/json/f107_cm_flux.json", _f107),
    # all_day et non all_hour : la fenetre d'une heure ne survivrait pas a une
    # cadence de 4 h, on perdrait la plupart des secousses.
    "seismes": ("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson",
                _seismes),
    "aurore": ("https://services.swpc.noaa.gov/json/ovation_aurora_latest.json", _aurore),
}


# ── Ecriture, par jour, sans doublon ────────────────────────────────────

def fichier(nom, jour):
    return MESURES / nom / (jour + ".ndjson.gz")


def cle(nom, o):
    """La cle d'unicite d'un releve, calculee UNIQUEMENT depuis le releve
    lui-meme — jamais depuis le contexte de la collecte.

    Piege trouve a la mesure : la premiere version composait la cle des seismes
    a l'ecriture (instant + identifiant) mais la relecture ne rebatissait que
    l'instant. Aucune cle ne correspondait donc jamais, et le fichier
    reprenait les 259 memes secousses a chaque passage. Une seule fonction,
    utilisee des deux cotes, rend la faute impossible."""
    t = o["t"]
    if nom == "seismes":
        # Deux secousses peuvent partager la meme seconde : l'instant seul ne
        # suffit pas, l'identifiant USGS tranche.
        ident = (o.get("v") or {}).get("id")
        return t + "|" + ident if ident else t
    return t


def lit(nom, f):
    if not f.exists():
        return {}
    out = {}
    try:
        with gzip.open(f, "rt", encoding="utf-8") as fh:
            for l in fh:
                try:
                    o = json.loads(l)
                    out[cle(nom, o)] = o
                except Exception:
                    continue
    except OSError:
        return {}
    return out


def fusionne(nom, points):
    """Les fenetres se chevauchent d'une collecte a l'autre : sans
    deduplication, chaque point serait ecrit six fois par jour. La cle est
    l'instant de la mesure — et pour les seismes, leur identifiant, parce que
    deux secousses peuvent partager la meme seconde."""
    par_jour = {}
    for t, v in points:
        if t is None:
            continue
        par_jour.setdefault(t.strftime("%Y-%m-%d"), []).append((t, v))

    ecrits = 0
    for jour, lot in sorted(par_jour.items()):
        f = fichier(nom, jour)
        f.parent.mkdir(parents=True, exist_ok=True)
        connus = lit(nom, f)
        avant = len(connus)
        for t, v in lot:
            o = {"t": t.isoformat(), "v": v}
            connus[cle(nom, o)] = o
        if len(connus) == avant:
            continue
        # Reecrit trie : un fichier qui grandit dans le desordre est illisible
        # a l'oeil, et le tri ne coute rien a ces volumes.
        #
        # mtime=0 est indispensable : gzip ecrit l'heure de compression dans
        # son en-tete, donc deux ecritures au contenu IDENTIQUE produisent des
        # octets differents. Sans ca, git verrait un changement a chaque
        # passage et le depot se remplirait de commits vides.
        # `gzip.open(..., "wt")` n'accepte pas mtime — il faut passer par
        # GzipFile, qui lui l'accepte, et l'habiller pour ecrire du texte.
        with open(f, "wb") as brut_fh:
            with gzip.GzipFile(fileobj=brut_fh, mode="wb", compresslevel=9,
                               mtime=0) as gz:
                with io.TextIOWrapper(gz, encoding="utf-8", newline="\n") as fh:
                    for k in sorted(connus):
                        fh.write(json.dumps(connus[k], ensure_ascii=False,
                                            separators=(",", ":")) + "\n")
        ecrits += len(connus) - avant
    return ecrits


def purge(jours=400):
    """On garde un peu plus d'un an. Sans borne, le depot enfle sans fin."""
    limite = (datetime.now(timezone.utc) - timedelta(days=jours)).strftime("%Y-%m-%d")
    n = 0
    for d in MESURES.glob("*/*.ndjson.gz"):
        if d.stem.replace(".ndjson", "") < limite:
            d.unlink()
            n += 1
    return n


def main():
    MESURES.mkdir(parents=True, exist_ok=True)
    etat = {"collecte_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "sources": {}}
    echecs = 0

    for nom, (url, red) in SOURCES.items():
        try:
            brut = telecharge(url)
            pts = red(brut)
            n = fusionne(nom, pts)
            couvert = None
            ts = sorted(t for t, _ in pts if t)
            if ts:
                couvert = round((ts[-1] - ts[0]).total_seconds() / 3600, 1)
            etat["sources"][nom] = {"ok": True, "recus": len(pts), "nouveaux": n,
                                    "fenetre_h": couvert,
                                    "dernier": ts[-1].isoformat() if ts else None}
            print("%-10s %5d recus  %5d nouveaux  fenetre %s h" %
                  (nom, len(pts), n, couvert))
        except Exception as e:
            # Une source qui tombe ne doit pas emporter les six autres.
            echecs += 1
            etat["sources"][nom] = {"ok": False, "erreur": str(e)[:200]}
            print("%-10s ECHEC : %s" % (nom, e), file=sys.stderr)

    supprimes = purge()
    if supprimes:
        print("purge : %d fichiers au-dela de 400 jours" % supprimes)
    etat["purges"] = supprimes

    (MESURES / "_etat.json").write_text(
        json.dumps(etat, ensure_ascii=False, indent=2), encoding="utf-8")

    # Sortie non nulle seulement si TOUT est tombe : un flux SWPC absent est
    # un fait courant, pas une panne de la collecte.
    if echecs == len(SOURCES):
        print("toutes les sources ont echoue", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
