
# Partie 2 : Programmation objet pour l'Internet des Objets (IoT)

La plateforme **SmartLink** permet de superviser des équipements IoT (*Internet of Things*).
Une plateforme est composée de plusieurs équipements IoT (capteurs, actionneurs, nœuds, ...) communiquant via un ou plusieurs protocoles de communication.
L'objectif de cet exercice est de développer une partie de cette application.

---

## Classe de base : `EquipementIoT`

Un objet de la classe **`EquipementIoT`** représente un équipement générique de la plateforme et possède les attributs suivants :
- **`id`** (entier positif),
- **`nom`** (chaîne de 30 caractères maximum),
- **`protocole`** (liste de protocoles acceptés par l'équipement, chaque protocole est désigné par un nom).

### 2.1 Définition de la classe `EquipementIoT`
- **Constructeur** : Initialiser ses attributs à l'aide des informations transmises en paramètres.
- **Décorateurs `property`** : Permettre d'accéder et de modifier les attributs **`id`** et **`_nom`**.
- **Attribut `_protocole`** : Initialisé à une liste vide, puis complété via la méthode **`ajouter_protocole()`**, qui ajoute un ou plusieurs protocoles passés en paramètres.
- **Affichage** : `print(e)` doit afficher les attributs **`_id`** et **`_nom`** de l'objet `e` de la classe `EquipementIoT`.

---

## Sous-classes de `EquipementIoT`

Les sous-classes sont les suivantes :
1. **`CapteurIoT`** : Permet d'effectuer une mesure.
2. **`ActionneurIoT`** (non demandée dans cet exercice) :
   - Effectue une action selon son état **OFF** ou **ON**.
   - En plus des attributs hérités, possède un attribut **`_etat`** dont la valeur est **"OFF"** ou **"ON"**.
   - L'appel de la méthode **`collecte()`** sur un objet `ActionneurIoT` retourne son état.
3. **`NoeudIoT`** : Regroupe plusieurs capteurs, actionneurs ou autres nœuds.

### 2.2 Classe `CapteurIoT`
- **Attribut supplémentaire** : **`_mesure`** (valeur initialisée à `None`).
- **Méthode `collecte()`** :
  - Affecte une valeur aléatoire à l'attribut **`_mesure`** (utiliser `randint(min, max)` du module `random` pour générer un entier aléatoire entre `min` et `max`).
  - Retourne cette même valeur.
- **Affichage** : `print(c)` doit afficher les attributs **`_id`** et **`_nom`** de l'objet `c` de la classe `CapteurIoT`.

**→ Définir la classe `CapteurIoT` selon la description ci-dessus.**

---

### 2.3 Classe `NoeudIoT`
- **Attribut supplémentaire** : **`_equipements`** (liste des équipements IoT regroupés par le nœud, initialisée à une liste vide).
- **Méthode `connecter(e)`** :
  - Ajoute l'objet `e` dans la liste **`_equipements`** **si et seulement si** :
    1. `e` est un équipement IoT (`CapteurIoT`, `ActionneurIoT` ou `NoeudIoT`).
    2. `e` a **au moins un protocole en commun** avec le nœud.
  - Affiche un message indiquant si la connexion a pu se faire ou non.
- **Méthode `collecte()`** :
  - Construit et retourne un **dictionnaire** `{clé: valeur}` où :
    - **`clé`** = `id` de l'équipement regroupé dans le nœud.
    - **`valeur`** =
      - la **mesure** si c'est un capteur,
      - l'**état** si c'est un actionneur,
      - le **dictionnaire du regroupement** (résultat de `collecte()`) si c'est un nœud.
- **Affichage** : `print(n)` doit afficher les attributs **`_id`** et **`_nom`** de l'objet `n` de la classe `NoeudIoT`.

**→ Définir la classe `NoeudIoT` selon la description ci-dessus.**

---

### 2.4 Fusion de nœuds avec l'opérateur `+`
On souhaite pouvoir **fusionner 2 objets `NoeudIoT`** (`n1` et `n2`) avec l'opérateur `+`.
Le résultat est un **nouvel objet `NoeudIoT`** dont :
- **`id`** = somme des `id` de `n1` et `n2`,
- **`nom`** = concaténation des noms de `n1` et `n2`,
- **`protocoles`** = union des protocoles de `n1` et `n2`,
- **`equipements`** = union des équipements de `n1` et `n2` (**sans doublons**).

**→ Modifier la classe `NoeudIoT` en conséquence.**

---

### 2.5 Exercice pratique
Soit l'extrait de code suivant dans `main()` :

```python
def main():
    protocoles = ["ble", "zigbee", "wifi", "uwb", "loran"]
    thermometre = CapteurIoT(25, "Température")
    luminosite = CapteurIoT(2, "Luminosité")
    ventilo = ActionneurIoT(47, "Ventilateur")
    led = ActionneurIoT(10, "Lumière")
    noeud_a = NoeudIoT(6, "routeur_hall")
```

**Compléter le code pour :**
1. Créer un objet **`noeud_b`** dont :
   - le nom est **"routeur_salle"**
   - l'`id` est **7**.
2. Lui ajouter les protocoles **"ble"**, **"zigbee"** et **"wifi"**.
3. Connecter à **`noeud_b`** les équipements compatibles parmi **`thermometre`**, **`ventilo`**, **`led`** et **`luminosite`**.
4. Créer un nouveau nœud **`noeud_lab`** qui correspond à la **fusion** de **`noeud_a`** et **`noeud_b`**.
5. Modifier son nom pour l'appeler **"routeur_labo"**.
6. Afficher :
   - l'`id` et le `nom` de **`noeud_lab`**,
   - les **données de collecte** de **`noeud_lab`**.
7. **Gérer les exceptions** : Afficher l'erreur si une exception est déclenchée.
