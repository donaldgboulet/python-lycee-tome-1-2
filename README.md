# Plan de formation Python — 2026-2027

Objectif : maîtriser Python en un an et arriver à la fac avec un projet concret derrière soi.

Ce plan s'appuie sur les deux tomes déjà présents dans ce dossier :

- **Tome 1** (`Python au lycée– tome 1/livre-python1.pdf`) — 17 chapitres de fondamentaux (conditions, boucles, fonctions, listes, chaînes, fichiers) + 10 projets appliqués. Le travail déjà fait est dans `Python au lycée– tome 1/Fondamentaux/` et `Python au lycée– tome 1/projet/`.
- **Tome 2** (`Python au lycée– tome 2/livre-python2.pdf`) — 26 chapitres avancés en deux parties : mathématiques appliquées + informatique (suites, nombres complexes, dérivées, exponentielles, logarithmes, intégrales, **programmation orientée objet**, mouvement de particules, algorithmes récursifs, calcul parallèle), puis 11 projets avancés (automates, cryptographie, images et matrices, ensemble de Mandelbrot, images 3D, Sudoku, fractales, Big Data sur 2 chapitres).

Les dossiers `Cours/` et `Projets/` créés dans `Python au lycée– tome 2/` reprennent la même logique que ceux déjà utilisés dans le Tome 1, pour rester cohérent avec ce qui existe déjà.

Ce dépôt regroupe aussi ce qui existait dans l'ancien dossier `Formation_Python_2026` (fusionné ici le 28/08/2026) :

- `Python au lycée– tome 1/Fondamentaux/chapitre_5_Arithmétique_Boucle_tant_que.py` — le chapitre 5 déjà commencé
- `Python au lycée– tome 1/projet/projet_convertisseur_notes.py` — un projet déjà réalisé
- `computer_vision/` et `computervision/` — exploration IA (détection de mains avec OpenCV/mediapipe), en dehors du programme Tome 1/2 mais conservée
- `Ressources/apprendre-a-programmer-avec-python-3.pdf` — livre de référence complémentaire

## Pourquoi les deux tomes avant les projets data

1. Les deux PDF couvrent l'ensemble du programme (conditions, boucles, fonctions, POO, algorithmes).
2. À eux deux, ils totalisent 21 projets concrets à publier sur GitHub.
3. La programmation orientée objet (Tome 2, ch.8) est un prérequis pour bien utiliser NumPy, Pandas et scikit-learn ensuite.
4. Les algorithmes récursifs et le calcul parallèle donnent des bases utiles avant le Big Data.

En résumé : Tome 1 (fondamentaux solides) → Tome 2 (POO + algorithmes avancés) → NumPy/Pandas (data science) → vrais projets data (Kaggle, etc.). C'est un investissement de 9 à 12 mois.

## Calendrier

### Phase 1 — Fondamentaux (septembre à décembre 2026)

Objectif : maîtriser le Tome 1 en entier.

| Période | Contenu |
|---|---|
| Septembre – octobre | Ch.1-3 (mise en route, si...alors), ch.4-7 (fonctions, listes, chaînes), exercices réguliers, commit Git chaque semaine |
| Novembre | Ch.8-9 (fichiers, visualisation), ch.10-13 (notions avancées), tous les exercices |
| Décembre | Ch.14-23 — les 10 projets du Tome 1, projets simples mais complets, publiés sur GitHub |

À la fin de cette phase : conditions, boucles, fonctions, fichiers, listes maîtrisés.

### Phase 2 — Spécialisation (janvier à mai 2027)

Objectif : POO et algorithmes.

| Période | Contenu |
|---|---|
| Janvier – février | Ch.8 (POO — important), ch.10-11 (algorithmes récursifs), exercices POO approfondis, premiers petits projets orientés objet |
| Mars | Ch.9 (mouvement de particules / simulation), ch.12 (calcul parallèle), projets intermédiaires, introduction Big Data (ch.22-23) |
| Avril – mai | Ch.13-21 — projets avancés : automates, cryptographie, images et matrices, Mandelbrot |

À la fin de cette phase : POO maîtrisée, algorithmes avancés, projets complexes réalisés.

### Phase 3 — Data science (juin 2027 et après)

Objectif : NumPy, Pandas, Machine Learning.

| Période | Contenu |
|---|---|
| Juin – juillet | NumPy (tableaux n-dimensionnels), Pandas (analyse de données), Matplotlib avancé, premiers projets data |
| Août et après | Machine Learning (scikit-learn), projets sur données réelles (Kaggle), introduction Deep Learning (TensorFlow), portfolio data science |

## Suivi

| Mois | Contenu | Résultat attendu |
|---|---|---|
| Sept. 2026 | Ch.1-3 Tome 1 | Exercices des 3 premiers chapitres |
| Oct. 2026 | Ch.4-7 Tome 1 | Exercices fonctions/listes/chaînes |
| Nov. 2026 | Ch.8-13 Tome 1 | Fichiers + notions avancées |
| Déc. 2026 | Projets ch.14-23 | 10 projets complets sur GitHub |
| Jan. 2027 | Ch.8 POO (Tome 2) | POO maîtrisée |
| Fév. 2027 | Ch.9-12 Tome 2 | Algorithmes avancés |
| Mars-Mai 2027 | Projets ch.13-21 | 9 projets avancés |
| Juin+ 2027 | NumPy / Pandas | Début data science |

## Prochaines étapes

1. Continuer le chapitre 5 du Tome 1 (arithmétique, boucle "tant que", nombres de Fermat) — c'est là où le travail s'est arrêté.
2. Committer sur Git chaque semaine (voir `GUIDE_GIT_THONNY.md` dans ce dossier).
3. À la fin de chaque chapitre, faire les exercices avant de passer au suivant.
4. En décembre, consacrer le mois aux 10 projets du Tome 1 plutôt que d'avancer dans le Tome 2.
5. Revenir à ce README pour ajuster le calendrier si le rythme réel diffère (c'est normal et attendu).

## Statut

Dépôt consolidé le 28/08/2026 : ce dossier remplace désormais l'ancien `Formation_Python_2026` (qui pointait vers `github.com/donaldgboulet/-Formation_Python_2026`). Tout le contenu utile de l'ancien dossier a été récupéré ici, réorganisé selon la structure Tome 1 / Tome 2.
