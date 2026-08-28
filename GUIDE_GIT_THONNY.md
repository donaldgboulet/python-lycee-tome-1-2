# Guide Git simple avec Thonny

Un guide minimal pour suivre sa progression avec Git, sans complexité inutile.

## 1. Installer Git

Si ce n'est pas déjà fait, installer Git pour Windows : https://git-scm.com/download/win

Vérifier l'installation dans un terminal (menu Démarrer → PowerShell) :

```
git --version
```

## 2. Se présenter à Git (une seule fois)

```
git config --global user.name "Votre nom"
git config --global user.email "votre@email.com"
```

## 3. Créer le dépôt (une seule fois)

Dans PowerShell, se placer dans le dossier du projet puis initialiser :

```
cd "C:\Users\edgbo\OneDrive\Documents\OSG_2026\python_2026\python_pour_le_lycee_tome_1_2"
git init
```

Créer un fichier `.gitignore` pour ne pas suivre les fichiers inutiles (déjà fait si ce fichier existe) :

```
__pycache__/
*.pyc
.thonny/
```

## 4. Le cycle hebdomadaire

Après une séance de travail (par exemple à la fin de chaque semaine, ou après chaque chapitre terminé) :

```
git add .
git commit -m "Ch.4 : fonctions - exercices terminés"
```

Le message de commit doit dire ce qui a été fait, pas juste "update". Exemples de bons messages :

- `"Ch.3 : conditions - tous les exercices"`
- `"Projet 2 : calculatrice géométrie - version complète"`
- `"Ch.8 Tome 2 : POO - première classe créée"`

## 5. Publier sur GitHub

Créer un dépôt vide sur https://github.com/new (sans README, sans licence — le dépôt local en a déjà).

Puis, une seule fois, relier le dépôt local au dépôt GitHub :

```
git remote add origin https://github.com/VOTRE_UTILISATEUR/NOM_DU_DEPOT.git
git branch -M main
git push -u origin main
```

Ensuite, à chaque nouveau commit, il suffit de :

```
git push
```

## 6. Utiliser Thonny au quotidien

Thonny n'a pas besoin de plugin Git particulier : le code s'écrit et s'exécute normalement dans Thonny, et les commandes `git add` / `git commit` / `git push` se lancent depuis PowerShell dans le dossier du projet, séparément de Thonny.

Routine simple :

1. Coder et tester dans Thonny.
2. Une fois satisfait du résultat, ouvrir PowerShell dans le dossier du projet.
3. `git add .` puis `git commit -m "..."` puis `git push`.

## 7. Vérifier l'état du projet

À tout moment, pour voir ce qui a changé depuis le dernier commit :

```
git status
```

Pour voir l'historique des commits :

```
git log --oneline
```
