# Contexte Persistant - Session Python UTC INF2 Lina

## ud83d\udccc **Informations Gnrales**
- **Projet** : [Python_UTC_INF2_Lina](https://github.com/yvespierrecabon/Python_UTC_INF2_Lina)
- **Rpertoire Local** : `/workspace/yvespierrecabon__Python_UTC_INF2_Lina`
- **Objectif** : Support pour les travaux pratiques et projets en Python (UTC INF2).
- **Utilisateur** : yvespierrecabon

---

## ud83c\udfaf **Objectifs Actuels**
*( mettre  jour  chaque nouvelle t2che ou changement de priorit)*
- [ ] **Priorit 1** : Corriger la logique de `est_couicable` dans `TD2/Q1.py` (comparer la **somme des chiffres** au lieu du nombre de chiffres).
- [ ] **Priorit 2** : Impl9menter les fonctions pour le **carr magique** (Q2 du TD2).
- [ ] **Priorit 3** : Ajouter des tests unitaires pour valider les solutions.

---

## ud83d\udd27 **Environnement Technique**
- **Langage Principal** : Python (version :  v9rifier)
- **Outils** : Git, GitHub, VS Code (ou autre IDE)
- **D9pendances** : 
  - `pypdf` (pour lire les PDFs, utilis dans le sandbox).

---

## ud83d\udcc2 **Structure des Fichiers**
*( compl9ter au fur et  mesure de l'exploration du projet)*

### **R9pertoire Racine**
- `.git/` : D9pt Git.
- `.idea/` : Configuration IDE (IntelliJ/PyCharm).
- `CONTEXT.md` : Contexte persistant du projet (ce fichier).
- `AVANCEMENT.md` : Historique des actions men9es.

### **Sous-R9pertoires**
- **`TD1/`** : Contient les exercices du TD1.
  - `Q1.py` : Solutions pour la question 1 (boucles et motifs).
  - `Q2.py` : Solutions pour la question 2 (diviseurs communs).
  - `Q3.py` : Solutions pour la question 3 (moyennes, valeurs proches de 0).
  - `Q4.py` : Solutions pour la question 4 (comptage de caractres, lettres, chiffres).
  - `Q5.py` : Solutions pour la question 5 (triage des 9tudiants par note).
  - `TD1.pdf` : 9nonc du TD1.

- **`TD2/`** : Contient les exercices du TD2.
  - `Q1.py` : Solutions pour la question 1 (nombres couicables). ** corriger** : la logique de `est_couicable` doit comparer la **somme des chiffres** (et non le nombre de chiffres).
  - `Q2.py` : Solutions pour la question 2 (carr magique). ** corriger** : `somme_colonne` utilise `mat[:][i]` (incorrect).
  - `Correction-TD2.pdf` : Correction du TD2 ( v9rifier).
  - `TD2.pdf` : 9nonc du TD2 (lu et analys).

- **`TD3/`** : Contient les exercices du TD3.
  - `fcts_carre_magique.py`
  - `Q1.py`, `Q2.py`, `Q3.py`
  - `TD3.pdf`

- **`TD4/`** : Contient les exercices du TD4.
  - `TD4-Objet 1.pdf`
  - `TD4.py`

### **Ancien fichier supprim**
- `main.py` : **Supprim le 20-07-2026** (remplac par les fichiers `Qx.py` s9par9s).

---

## ud83d\ude80 **Dernires Actions**
*(Rfrence rapide aux dernires actions men9es - voir AVANCEMENT.md pour l'historique complet)*
- **Dernire Mise  Jour** : 24-07-2026
- **Dernire T2che** : Mise  jour des rgles de travail pour inclure l'autonomie de codage.

---

## 26a0\ufe0f **Points d'Attention**
*(Problmes r9currents, contraintes, ou notes importantes  retenir)*
- **Contraintes** : 
  - Respecter les 9nonc9s des TDs (ex: `est_couicable` doit comparer la **somme des chiffres**, pas le nombre de chiffres).
- **Problmes Connus** :
  - **`TD2/Q1.py`** : La fonction `est_couicable` a une logique incorrecte (correction propos9e dans `AVANCEMENT.md`).
  - **`TD2/Q2.py`** : La fonction `somme_colonne` utilise `mat[:][i]` (incorrect, doit atre corrig9).
- **Bonnes Pratiques** :
  - Les solutions sont organis9es dans des **sous-r9pertoires par TD** (`TD1/`, `TD2/`, etc.).
  - Utiliser `.gitkeep` pour conserver les r9pertoires vides dans Git.
  - Toujours v9rifier les **docstrings** et les **types** dans les fonctions.

---

## ud83d\udd04 **Rgles de Travail**
1. **Persistance** : Ce fichier doit atre lu ** chaque nouvelle session** pour maintenir le contexte.
2. **Synchronisation Systmatique** :
   - ** chaque demande d'analyse de fichier**, je dois **toujours commencer par synchroniser le d9pt GitHub avec la sandbox** via :
     ```bash
     cd /workspace/yvespierrecabon__Python_UTC_INF2_Lina && git fetch --all && git pull origin main
     ```
   - Cela garantit que j'analyse **la dernire version** des fichiers pouss9s par l'utilisateur.
3. **Mises  Jour** : 
   - Mettre  jour ce fichier **aprs chaque t2che significative**.
   - Toujours v9rifier la coh9rence avec `AVANCEMENT.md`.
4. **Clart** : 
   - Utiliser des sections claires (`##`, `###`).
   - Privil9gier les listes  puces pour les 9l9ments dynamiques.
5. **Autonomie de Codage** :
   - **Privil9gier les explications g9n9rales et les exemples de code g9n9riques** pluttt que des corrections directes.
   - L'utilisateur prfre coder lui-meme en s'inspirant des concepts et des bonnes pratiques fournis.
   - **Exemple** :
     - 9 Donner : *"Pour impl9menter `@property`, voici la syntaxe : ```@property def nom(self): return self._nom```".*
     - 8 9viter : *"Voici le code corrig9 pour ta classe `Individu` : [code complet]."*

---

## ud83d\udcc5 **Prochaines 9tapes**
*(Id9es ou t2ches planifi9es pour les prochaines sessions)*
- [ ] Corriger `est_couicable` dans `TD2/Q1.py` (voir analyse dans `AVANCEMENT.md`).
- [ ] Corriger `somme_colonne` dans `TD2/Q2.py` (remplacer `mat[:][i]` par `sum(row[j] for row in mat)`).
- [ ] Impl9menter `carre_magique_normal(mat)` (Q2, question 6 du TD2).
- [ ] Ajouter des tests unitaires pour valider les solutions.
- [ ] V9rifier la coh9rence des fichiers `Qx.py` avec les 9nonc9s des TDs.

---

*Dernire modification : 24-07-2026*