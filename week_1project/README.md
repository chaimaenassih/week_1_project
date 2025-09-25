# Flask CRUD API Assessment

Ce projet est une API REST construite avec le framework Python Flask, conçue pour gérer des enregistrements d'étudiants. Elle offre des opérations CRUD complètes (Create, Read, Update, Delete) avec la prise en charge de la pagination.

---

## Fonctionnalités de l'API

L'API expose les points de terminaison suivants :

-   **`GET /students`** : Récupère la liste de tous les étudiants. Prend en charge la pagination avec les paramètres de requête `page` et `limit`.
-   **`GET /students/<id>`** : Récupère un étudiant spécifique par son ID.
-   **`POST /students`** : Crée un nouvel étudiant.
-   **`PUT /students/<id>`** : Met à jour un étudiant existant par son ID.
-   **`DELETE /students/<id>`** : Supprime un étudiant par son ID.

---

## Configuration du Projet

Ce projet peut être configuré à l'aide de `uv` (recommandé) ou de `pip`.

### Méthode 1 : Utilisation de `uv` (Recommandé)

1.  **Installez `uv`** si ce n'est pas déjà fait :
    ```bash
    pip install uv
    ```

2.  **Clonez le projet** et naviguez jusqu'au répertoire :
    ```bash
    git clone <URL_DU_REPO>
    cd week_1_project
    ```

3.  **Créez et activez l'environnement virtuel** :
    ```bash
    uv venv
    # Sur macOS/Linux:
    source .venv/bin/activate
    # Sur Windows:
    .venv\Scripts\activate
    ```

4.  **Installez les dépendances** à partir de `pyproject.toml` :
    ```bash
    uv sync
    ```

### Méthode 2 : Utilisation de `pip`

1.  **Créez et activez un environnement virtuel** :
    ```bash
    python -m venv .venv
    # Sur macOS/Linux:
    source .venv/bin/activate
    # Sur Windows:
    .venv\Scripts\activate
    ```

2.  **Installez les dépendances** à partir de `requirements.txt` :
    ```bash
    pip install -r requirements.txt
    ```

---

## Comment Exécuter l'Application

1.  **Assurez-vous que l'environnement virtuel est activé.**
2.  **Lancez l'application Flask** en exécutant le fichier `main.py` :
    ```bash
    python main.py
    ```
3.  L'API sera accessible à l'adresse **`http://127.0.0.1:5001`**.

---

## Comment Tester l'API

Les points de terminaison de l'API peuvent être testés en utilisant le fichier `test-api.rest`.
Si vous utilisez VS Code, assurez-vous d'avoir l'extension **REST Client** installée. Ouvrez le fichier `test-api.rest` et cliquez sur le lien "Send Request" au-dessus de chaque requête pour la tester.

Vous pouvez également utiliser des outils comme `curl` ou Postman pour envoyer des requêtes à l'API.

---

## Structure du Projet