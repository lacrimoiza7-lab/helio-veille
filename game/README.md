# Ti-Shaw et l'Étoile perdue d'Hélio

Un petit jeu d'aventure vue de dessus (dans l'esprit des classiques action-aventure
des années 80), avec **Ti-Shaw** en héros et **Mister BigNip** le poisson orange
comme compagnon. Ti-Shaw doit récupérer l'Étoile perdue de la station Helio-Watch,
gardée au fond d'un donjon.

## Comment jouer

**Double-clique sur `ti-shaw.html`** — ça s'ouvre dans ton navigateur (Chrome,
Firefox, Edge…). Aucune installation, aucune connexion internet requise.

| Touche | Action |
|--------|--------|
| `←` `↑` `↓` `→` ou `W A S D` | Déplacer Ti-Shaw |
| `Z` / `Espace` / `J` | Coup d'épée |
| `Entrée` | Commencer / recommencer |
| `P` | Pause |
| `M` | Couper / remettre le son |

Sur mobile/tablette : glisse le doigt pour bouger, tape pour frapper.

## Le but

1. Explore les 9 zones de l'extérieur d'Hélio.
2. Trouve la **clé** (zone est, gardée par des ennemis).
3. Entre dans la **caverne** (zone nord) pour accéder au donjon.
4. Ouvre la **porte verrouillée** avec ta clé.
5. Bats le **boss** et touche l'**Étoile d'Hélio** pour gagner !

Mister BigNip t'accompagne partout et **crache des bulles** sur les ennemis proches —
il combat avec toi.

## Pensé pour une petite machine (Celeron, 4 Go)

- **Un seul fichier HTML de ~28 Ko**, zéro dépendance, zéro image à télécharger.
- Résolution interne minuscule (256×208) agrandie par le navigateur → le processeur
  ne calcule presque rien.
- Les décors de chaque écran sont **pré-dessinés une fois puis réutilisés** (pas de
  recalcul à chaque image).
- Boucle de jeu à **pas fixe** : la vitesse reste constante même si l'affichage
  descend à 30 images/seconde.
- Tous les personnages et décors sont **dessinés au code** (rectangles de pixels),
  donc rien à charger et aucun asset externe.

## Note

Jeu original : les personnages, la carte, les graphismes et la musique sont créés
de zéro. Seul le *genre* (aventure vue de dessus) s'inspire des classiques ;
aucun contenu d'un jeu existant n'est réutilisé.
