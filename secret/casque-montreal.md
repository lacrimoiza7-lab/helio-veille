# Casque de Montréal — *The Secret* (Byron Preiss, 1982)

> Notes de travail. Toute ligne non sourcée est marquée **[hypothèse]** ou
> **[à vérifier]** — pas de broderie.
>
> **Révision du 2026-08-26** : passe au scan haute résolution local
> (`09_pleine_qualite.jpg`, 3064 × 4878, 15,8 Mo). Cette passe **infirme** deux
> choses que les versions précédentes tenaient pour acquises. Voir § Rétractations.

## Cadre

- 12 casques en céramique enterrés ; chaque cachette encodée par une **peinture + un vers** à apparier.
- Trouvés à ce jour : Chicago (1983), Cleveland (2004), Boston (2019). Montréal : **non trouvé**.
- Appariement retenu par la communauté : **Image 9 + Vers 5**.

## Rétractations — 2026-08-26

### 1. Le « 1881 » n'est PAS dans l'image 9. (erreur corrigée)

Les crops `81.png` (« 1881 ») et `41.png` (« 1442 ») du dossier de travail
montrent des cartouches **gravés dans de la pierre grise**, en relief, éclairés
au soleil. Le troisième crop du même lot, `euclid.png`, porte l'annotation du
site : « **Euclid Ave and Month indicator** ». Euclid Avenue est à **Cleveland**.

Ces trois crops viennent donc de la **peinture de Cleveland**, pas de l'image 9.
L'image 9 est une peinture sombre sur fond ocre : elle ne contient **aucune
surface de pierre**, aucun cartouche, aucune plaque.

**Conséquence :** la déduction « puisque l'artiste cache des chiffres lisibles
(1881), la voie forte est de chercher un 45 en chiffres » **tombe**. Elle était
bâtie sur la mauvaise image. Le lien 1881 → incorporation du Canadien Pacifique
→ George Stephen est un raisonnement juste appliqué à un objet qui n'existe pas
dans le tableau de Montréal.

Ce que Cleveland dit vraiment, et qui reste utile : **les deux méthodes de
Palencar ne se mélangent pas.** À Cleveland il grave les chiffres en clair dans
la pierre ; à Chicago il les dessine avec les bras d'un moulin. Montréal n'a pas
de pierre — donc, s'il y a un nombre, il est **dessiné par une forme**, pas écrit.

### 2. Le vers 5 « Lane / Two twenty two… » est BON. (rejet infondé)

La version précédente notait le texte comme « douteux / mal recoupé, à ne pas
utiliser ». C'est faux : le fichier `american.PNG` du dossier de travail est le
**scan de la page imprimée de l'édition américaine**, avec la vignette du casque
en regard. Le texte ci-dessous en est la transcription directe.

## Vers 5 — texte de référence (vérifié sur la page imprimée)

```
Lane
Two twenty two
You'll see an arc of lights
Weight and roots extended
Together saved the site
Of granite walls
Wind swept halls
Citadel in the night
A wingless bird ascended
Born of ancient dreams of flight
Beneath the only standing member
Of a forest
To the south
White stone closest
At twelve paces
From the west side
Get permission
To dig out.
```

18 lignes. Acrostiche : `L T Y W T O W` · **`C A B B O T`** · `T W A F G T`.
Le bloc central (lignes 8–13) donne **CABBOT** — ou, décalé d'un cran, **ABBOT**,
soit **sir John Abbott**, maire de Montréal et premier ministre du Canada.

## Ancrage géographique (consensus communautaire)

- **Golden Square Mile**, **Maison George-Stephen** (Le Mount Stephen).
- Objet « **leg-eater** » caché dans l'image (coin du col) = base d'un lampadaire
  de la Maison George-Stephen → principal indice reliant l'image à Montréal.
  **[non confirmé par Palencar]**
- Fiche 12treasures pour l'image 9 : Octobre / Opale / **10 h** / Calendula /
  **Pays-Bas** ; « The Opal of the Lowland Gnomes: A cloud of shining, shifting smoke ».

## Les chiffres — état réel de la case

Relevé sur la fiche 12treasures de l'image 9 (2026-08-26) :

| Champ | Valeur portée |
|---|---|
| Latitude / longitude | **73** |
| Heure | **10 heures** |
| Mois | Octobre |
| Nation | Pays-Bas |
| Fleur | Calendula |
| Pierre | Opale |

Montréal est à 45,5° N / 73,6° O. Cleveland (41,5° N / 81,7° O) a **les deux**
chiffres gravés dans sa peinture — 1442 → 41, 1881 → 81. Donc le pendant du 73
devrait exister. **La case « 45 » est vide depuis 44 ans.** L'hypothèse d'Iza
reste donc une question ouverte légitime, même si son point de départ (le 1881)
était mal attribué.

## Balayage du scan haute résolution — 2026-08-26

Méthode : `09_pleine_qualite.jpg` en pleine résolution, flou gaussien r ≈ 1,8 px
pour noyer la trame d'imprimerie, puis étirement de contraste sur percentiles
2–98, puis agrandissement Lanczos ×3 à ×6. Le script est dans `secret/zoom.py`.

Zones passées, en pixels du fichier pleine qualité :

| Zone | Boîte (x0,y0,x1,y1) | Résultat |
|---|---|---|
| Bandeau du bonnet + cabochon | 900, 960 → 2080, 1220 | damier régulier 3 rangs, cabochon rond au centre. Rien d'écrit. |
| Boucle de cheveux droite (le « 73 ») | 1980, 1480 → 2320, 1780 | **ne lit pas 73** — voir ci-dessous |
| Col en escalier (yoke) | 980, 1980 → 2060, 2540 | damier + degrés ; une **croix en X marquée dans le pli du tissu sombre** sous le V du col |
| Panneau haut (Saltire) | 1820, 2210 → 2080, 2430 | X franc, double cadre, barres sombres haut et bas |
| Panneau bas (figure) | 1820, 2440 → 2080, 2680 | figure nue + masse noire — voir ci-dessous |
| Objet noir aux pieds | 1940, 2560 → 2040, 2660 | ~60 × 70 px natifs : la résolution du scan s'arrête là |
| Objet pendant sous le panneau | 1780, 2650 → 2120, 2900 | forme nette — voir ci-dessous |
| Manchette gauche | 940, 3130 → 1300, 3560 | damier régulier, ~5 colonnes, fondu dans l'ombre |
| Manchette droite | 2020, 3140 → 2360, 3570 | damier régulier, ~5–6 colonnes, fondu dans l'ombre |
| Fond ocre, côté droit | 2200, 1250 → 3000, 1950 | taches claires diffuses, aucune forme lisible |
| Manteau noir entier | 200, 2700 → 2950, 4700 | ombres remontées : **tissage en chevrons et plis verticaux, rien d'autre** |

**Résultat du balayage : aucun chiffre arabe lisible nulle part dans l'image 9.**
Ni 45, ni 73, ni aucun autre. Ce n'est pas « je n'ai pas trouvé faute de
résolution » — le scan est net au point de montrer le grain de la trame, les
poils du pinceau dans les manchettes et le tissage du drap. S'il y avait un
cartouche chiffré comme celui de Cleveland, il serait visible.

### Le « 73 » de la communauté ne tient pas au scan HD

Le crop `tie_73.png` est la mèche de cheveux qui retombe à droite du visage
(zone 1980,1480 → 2320,1780). Au HD, c'est **une mèche peinte à deux boucles** :
une grande boucle en crochet, une plus petite en dessous. Sur l'image web
compressée d'où vient le crop, le bruit fabrique un contour qui suggère 7 et 3.
Sur le scan, la suggestion disparaît. **[à traiter comme un Rorschach, pas comme
une donnée]** — ce qui veut dire que la case « 73 » est possiblement vide, elle
aussi, et que la ligne « le 73 est déjà repéré » était trop généreuse.

### Ce que le panneau du bas montre vraiment

Figure **masculine nue**, de profil **vers la droite**, accroupie et penchée vers
l'avant. Un bras replié, coude en pointe, levé **en arrière** au-dessus de la
tête. Jambes fléchies en fente, pied arrière au sol à gauche.

À ses pieds, à droite : une **masse noire pleine**, sommet arrondi, avec une
petite **anse en arc** greffée au coin haut-gauche et un **ergot rectangulaire**
à la base. En couleur, le fond du panneau est crème ; la masse est franchement
noire, pas grise — donc **pas de la pierre nue rendue en gris**.

Lectures possibles de la masse, aucune tranchée à cette résolution :
- **[hypothèse]** pierre de curling (dôme + poignée en col de cygne). Le Royal
  Montreal Curling Club, 1807, est le plus vieux club sportif d'Amérique du Nord,
  fondé par des marchands écossais. **[à vérifier]**
- **[hypothèse]** chaudron / marmite à anse.
- **[hypothèse]** cloche. Palencar a confirmé le rébus `L + cloche = Liberty` à
  Philadelphie ; une cloche est un dôme surmonté d'une boucle.

### L'objet qui pend sous le panneau du bas

C'est la forme la **plus nette** de tout le balayage, et c'est elle que la
communauté invoque pour justifier « Pays-Bas ». Au HD : une **hampe effilée**
part du coin bas-gauche du cadre, descend à ~40° vers la droite, puis s'élargit
en un **corps arrondi à intérieur clair**, avec une encoche sombre à la jonction.
Longueur de la hampe ≈ 3 × la largeur du corps.

- Lecture communautaire : **sabot de bois** (talon étroit, bout relevé) → Pays-Bas.
- **[hypothèse]** la même silhouette lit aussi bien comme **tête de club** au bout
  d'un manche — un club de golf. Le Royal Montreal Golf Club a été fondé en
  **1873** par l'Écossais Alexander Dennistoun et jouait à ses débuts sur le
  **parc du Mont-Royal**. Le « 73 » que personne n'arrive à trouver dans les
  cheveux serait alors une **date**, pas un contour. **[à vérifier — c'est une
  convergence séduisante, donc exactement le genre de chose qui mérite d'être
  cassée avant d'être crue]**
- **[hypothèse]** louche, corne à poudre, chausse-pied.

### Le panneau du haut

Cadre double, un **X franc** à l'intérieur, barre sombre en haut et en bas. Les
quatre triangles clairs découpés par le X ne sont **pas égaux** : ceux du haut et
du bas sont des triangles pleins, ceux de gauche et de droite sont pincés en
pointes de flèche. La fiche 12treasures s'en sert deux fois : **X = 10 = octobre**
(mois) **et 10 heures** (heure). Le thème écossais ajoute une troisième lecture,
le **sautoir de saint André**, non retenue par la communauté parce qu'elle a
étiqueté l'image « Pays-Bas ».

Une **deuxième croix en X**, celle-là marquée dans les plis du drap sombre, est
visible juste sous le V du col (zone 1450–1650 × 2560–2680). Elle n'est pas
décorative : elle est dessinée à la hachure comme le reste du tissu. **[à verser
au dossier écossais]**

## Écosse ou Pays-Bas — l'argument (inchangé)

**Pour l'Écosse :** galon en damier (*diced band*) du bonnet militaire écossais ;
sautoir au panneau du haut ; second sautoir dans les plis du col ; « Lowlands »
est le nom des Basses-Terres d'Écosse et la litanie sépare déjà le « peuple
celte » (Highlands, Irlande) des « Lowland Gnomes » ; **Montréal a une communauté
écossaise fondatrice et n'a pas de communauté néerlandaise**, ce qui contredit la
règle des ethnies vérifiée sur les trois casques trouvés (Cleveland/Grèce,
Boston/Italie, Chicago/Irlande).

**Pour les Pays-Bas :** toutes les autres entrées de la litanie sont de grands
blocs nationaux ; tout le genre du gnome vient d'un livre néerlandais ; l'objet
pendant se lit comme un sabot.

## Où en est l'hypothèse « 45 »

**Plausible, toujours pas vérifiée, et la voie « chiffre écrit » est maintenant
fermée** — le balayage HD complet ne trouve aucun chiffre écrit dans l'image 9.

Reste ouvert, par ordre de valeur :

1. **Un nombre dessiné par une forme**, méthode Chicago. Candidats non épuisés :
   le décompte des degrés de l'escalier du col (gauche et droite ont des nombres
   de marches différents), le décompte des cases des manchettes, le décompte des
   rangs du bandeau.
2. **Le rébus**, méthode confirmée de Palencar. Attaquer « Lane » par là :
   chercher dans l'image un objet qui *fait* « lane », pas un lieu qui *s'appelle*
   Lane. (La Banque de noms de lieux du Québec ne donne **aucun** « Lane » sur
   l'île de Montréal, sur 131 463 toponymes.)
3. **Le décompte vigésimal** : *còig air dhà fhichead* = 5 + (2 × 20). Deux
   groupes de vingt objets identiques plus cinq. Porte de sortie secondaire.
4. **La vidéo Palencar** : https://youtu.be/taEKPdeFvzU — source de presque
   toutes ses confirmations publiques. Il n'a **jamais rien dit** sur Montréal.

## TODO(human) — verdict d'Iza sur les deux objets

Deux formes sont nettes au scan mais **je ne peux pas les identifier** : la
résolution du scan s'arrête pile là où il faudrait trancher. Ton œil sur l'objet
est meilleur que mes percentiles.

Remplace les deux lignes ci-dessous par ce que tu vois, et pourquoi.

- **La masse noire aux pieds de la figure** (zone `1940,2560 → 2040,2660`) :
  →
- **L'objet qui pend sous le panneau du bas** (zone `1780,2650 → 2120,2900`) :
  →

## Où sont les fichiers

- Scan pleine qualité : `C:\Users\misty\Claude\Secret\images\09_pleine_qualite.jpg`
  (3064 × 4878). C'est **le seul** qui permette de trancher au zoom.
- Page imprimée du vers 5 : `american.PNG` (même dossier).
- Crops **de Cleveland**, à ne plus confondre avec l'image 9 : `41.png`,
  `81.png`, `euclid.png`, `4187.PNG`.
- Script de zoom détramé : `secret/zoom.py` (ce dépôt).

## Sources consultées

- Page imprimée de l'édition américaine du vers 5 (scan local `american.PNG`).
- Édition japonaise, pages 239-240, section 第5の詩 (sept mots-clés désignés par
  l'équipe de Preiss).
- 12treasures.com/front/09-montreal/ (fiche de l'image 9).
- thesecretatreasurehunt.fandom.com — page « John Jude Palencar
  Hints/Confirmations ».
- Banque de noms de lieux du Québec (toponymie.gouv.qc.ca).
- Société St. Andrew's de Montréal (standrews.qc.ca), tournée 37 arrêts.
- `thesecretofthesecret.com` et `thesecret.pbworks.com` sont **morts**.
