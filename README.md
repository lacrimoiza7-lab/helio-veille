# helio-veille

Données de veille pour la station [Helio-Watch](https://github.com/lacrimoiza7-lab),
collectées dans le nuage pour que l'historique continue de se remplir quand le
PC de la station est éteint.

Deux contenus de nature **très différente**, et qui ne doivent pas être
confondus :

## `mesures/` — des mesures d'instruments

Écrit toutes les 4 heures par [`collecte.py`](collecte.py), exécuté par
[une tâche planifiée](.github/workflows/collecte.yml). **Aucun modèle n'intervient** :
c'est un script, ce qui sort du flux amont est ce qui est écrit, sans recopie
ni interprétation.

| dossier | source | fenêtre portée par le flux |
|---|---|---|
| `vent/` | NOAA SWPC · RTSW | 24 h à la minute |
| `mag/` | NOAA SWPC · RTSW | 24 h à la minute |
| `kp/` | NOAA SWPC | 6 h à la minute |
| `rayons_x/` | NOAA GOES | 6 h |
| `f107/` | NOAA SWPC | cadence lente |
| `seismes/` | USGS | 24 h |
| `aurore/` | NOAA OVATION | instantané |

Un fichier NDJSON gzippé par jour et par source, une ligne par relevé :

```json
{"t":"2026-08-18T14:20:00+00:00","v":{"proton_speed":427.6,"proton_density":9.76}}
```

`t` est l'instant de la **mesure**, pas celui de la collecte. C'est ce qui
permet une résolution à la minute avec un passage toutes les 4 heures : les
fenêtres se chevauchent largement, et les relevés déjà connus sont ignorés.

`mesures/_etat.json` porte le compte rendu du dernier passage.

**L'ISS est volontairement absente.** `wheretheiss.at` ne rend que la position
instantanée, sans fenêtre : à 4 h d'intervalle on obtiendrait des points sans
rapport les uns avec les autres, pas une trace au sol. Elle reste construite
en local, à la cadence de 20 s, quand la station tourne.

## `veille.json` — la sortie d'un agent

Le ciel profond n'a pas de flux à consommer : GCN Circulars ne répond plus.
Un agent va donc **chercher** une fois par jour et dépose ici sa synthèse.
C'est la seule entrée du projet produite par un modèle, d'où son étiquette
distincte à l'écran de la station. Elle ne se mélange jamais aux mesures.
