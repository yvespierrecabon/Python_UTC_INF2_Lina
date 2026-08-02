# Contexte Persistant - Session Python UTC INF2 Lina

## **Informations Générales**
- **Projet** : [Python_UTC_INF2_Lina](https://github.com/yvespierrecabon/Python_UTC_INF2_Lina)
- **Répertoire Local** : `/workspace/yvespierrecabon__Python_UTC_INF2_Lina`
- **Objectif** : Support pour les travaux pratiques et projets en Python (UTC INF2).
- **Utilisateur** : yvespierrecabon

---

## **Objectifs Actuels**
*À mettre à jour à chaque nouvelle tâche ou changement de priorité*
- [ ] **Priorité 1** : Corriger la logique de `est_couicable` dans `TD2/Q1.py` (comparer la **somme des chiffres** au lieu du nombre de chiffres).
- [ ] **Priorité 2** : Implémenter les fonctions pour le **carré magique** (Q2 du TD2).
- [ ] **Priorité 3** : Ajouter des tests unitaires pour valider les solutions.

---

## **Environnement Technique**
- **Langage Principal** : Python (version : à vérifier)
- **Outils** : Git, GitHub, VS Code (ou autre IDE)
- **Dépendances** : 
  - `pypdf` (pour lire les PDFs, utilisé dans le sandbox).

---

## **Structure des Fichiers**
*À compléter au fur et à mesure de l'exploration du projet*

### **Répertoire Racine**
- `.git/` : Dépôt Git.
- `.idea/` : Configuration IDE (IntelliJ/PyCharm).
- `CONTEXT.md` : Contexte persistant du projet (ce fichier).
- `AVANCEMENT.md` : Historique des actions menées.

### **Sous-Répertoires**
- **`TD1/`** : Contient les exercices du TD1.
  - `Q1.py` : Solutions pour la question 1 (boucles et motifs).
  - `Q2.py` : Solutions pour la question 2 (diviseurs communs).
  - `Q3.py` : Solutions pour la question 3 (moyennes, valeurs proches de 0).
  - `Q4.py` : Solutions pour la question 4 (comptage de caractères, lettres, chiffres).
  - `Q5.py` : Solutions pour la question 5 (triage des étudiants par note).
  - `TD1.pdf` : Énoncé du TD1.

- **`TD2/`** : Contient les exercices du TD2.
  - `Q1.py` : Solutions pour la question 1 (nombres couicables). **À corriger** : la logique de `est_couicable` doit comparer la **somme des chiffres** (et non le nombre de chiffres).
  - `Q2.py` : Solutions pour la question 2 (carré magique). **À corriger** : `somme_colonne` utilise `mat[:][i]` (incorrect).
  - `Correction-TD2.pdf` : Correction du TD2 (à vérifier).
  - `TD2.pdf` : Énoncé du TD2 (lu et analysé).

- **`TD3/`** : Contient les exercices du TD3.
  - `fcts_carre_magique.py`
  - `Q1.py`, `Q2.py`, `Q3.py`
  - `TD3.pdf`

- **`TD4/`** : Contient les exercices du TD4.
  - `TD4-Objet 1.pdf`
  - `TD4.py`

- **`TD5/`** : Contient les exercices du TD5.
  - `TD5-Objet 2.pdf`
  - `Q1.py`

- **`TP3_Objets/`** : Contient les exercices du TP3 (Objets).
  - `TP3_Sujet.pdf` : Énoncé du TP3.
  - `pokemons.py` : Implémentation de la classe Pokemon.
  - `poupees_russes.py` : Implémentation des poupées russes.
  - `rectangle.py` : Implémentation de la classe Rectangle.

- **`Exams/`** : Contient les examens et partiels.
  - **`2024_median/`** : Examen médian de 2024.
    - `Médian-p2024.pdf` : Énoncé de l'examen (inclut l'exercice 3 sur le HTML).
    - `html.py` : **Implémentation en cours** des classes pour générer du HTML (exercice 3).
      - **Classes** : `Balise`, `BaliseContenu`, `Html`, `Titre`, `Paragraphe`, `Gras`, `Image`.
      - **Fonctionnalités** :
        - Compteur de balises (`Balise._compteur`).
        - Génération de code HTML valide via `__str__`.
        - Vérification des attributs (ex: `src` pour `Image`).
    - `20230416_001.jpg` : Image de test pour la classe `Image`.

### **Ancien fichier supprimé**
- `main.py` : **Supprimé le 20-07-2026** (remplacé par les fichiers `Qx.py` séparés).

---

## **Dernières Actions**
*Référence rapide aux dernières actions menées - voir AVANCEMENT.md pour l'historique complet*
- **Dernière Mise à Jour** : 25-07-2026
- **Dernière Tâche** : Ajout du répertoire `TP3_Objets/` avec ses fichiers (énoncé PDF et codes Python).

---

## **Points d'Attention**
*Problèmes récurrents, contraintes, ou notes importantes à retenir*
- **Contraintes** : 
  - Respecter les énoncés des TDs (ex: `est_couicable` doit comparer la **somme des chiffres**, pas le nombre de chiffres).
- **Problèmes Connus** :
  - **`TD2/Q1.py`** : La fonction `est_couicable` a une logique incorrecte (correction proposée dans `AVANCEMENT.md`).
  - **`TD2/Q2.py`** : La fonction `somme_colonne` utilise `mat[:][i]` (incorrect, doit être corrigé).
- **Bonnes Pratiques** :
  - Les solutions sont organisées dans des **sous-répertoires par TD/TP** (`TD1/`, `TD2/`, `TP3_Objets/`, etc.).
  - Utiliser `.gitkeep` pour conserver les répertoires vides dans Git.
  - Toujours vérifier les **docstrings** et les **types** dans les fonctions.

---

## **Règles de Travail**
1. **Persistance** : Ce fichier doit être lu **à chaque nouvelle session** pour maintenir le contexte.
2. **Synchronisation Systématique** :
   - **À chaque demande d'analyse de fichier**, je dois **toujours commencer par synchroniser le dépôt GitHub avec la sandbox** via :
     ```bash
     cd /workspace/yvespierrecabon__Python_UTC_INF2_Lina && git fetch --all && git pull origin main
     ```
   - Cela garantit que j'analyse **la dernière version** des fichiers poussés par l'utilisateur.
3. **Mises à Jour** : 
   - Mettre à jour ce fichier **après chaque tâche significative**.
   - Toujours vérifier la cohérence avec `AVANCEMENT.md`.
4. **Clarté** : 
   - Utiliser des sections claires (`##`, `###`).
   - Privilégier les listes à puces pour les éléments dynamiques.
5. **Autonomie de Codage** :
   - **Privilégier les explications générales et les exemples de code génériques** plutôt que des corrections directes.
   - L'utilisateur préfère coder lui-même en s'inspirant des concepts et des bonnes pratiques fournis.
   - **Exemple** :
     - ✅ Donner : *"Pour implémenter `@property`, voici la syntaxe : ```@property def nom(self): return self._nom```".*
     - ❌ Éviter : *"Voici le code corrigé pour ta classe `Individu` : [code complet]."*

---

## **Prochaines Étapes**
*Idées ou tâches planifiées pour les prochaines sessions*
- [ ] Corriger `est_couicable` dans `TD2/Q1.py` (voir analyse dans `AVANCEMENT.md`).
- [ ] Corriger `somme_colonne` dans `TD2/Q2.py` (remplacer `mat[:][i]` par `sum(row[j] for row in mat)`).
- [ ] Implémenter `carre_magique_normal(mat)` (Q2, question 6 du TD2).
- [ ] Ajouter des tests unitaires pour valider les solutions.
- [ ] Vérifier la cohérence des fichiers `Qx.py` avec les énoncés des TDs.
- [ ] Analyser les fichiers du **TP3_Objets** (pokemons.py, poupees_russes.py, rectangle.py).
- [ ] **Finaliser l'exercice 3 de `Exams/2024_median/html.py`** :
  - [x] Implémenter les classes `Balise`, `BaliseContenu`, `Html`, `Titre`, `Paragraphe`, `Gras`, `Image`.
  - [x] Ajouter un compteur de balises (`Balise._compteur`).
  - [x] Centraliser `__str__` dans `BaliseContenu` pour éviter la duplication de code.
  - [x] Vérifier l'existence du fichier `src` pour `Image`.
  - [ ] **Corriger `main()`** pour afficher **6 balises** (actuellement 5).
    - **Solution** : Créer un 2ème objet `Gras` ou ajouter une balise supplémentaire (ex: `Paragraphe`).
  - [ ] Valider le typage de `niveau` dans `Titre` (changer `str` en `int` avec validation 1-6).

---

*Dernière modification : 02-08-2026*