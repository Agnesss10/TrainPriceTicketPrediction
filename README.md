TrainPriceTicketPrediction
==============================
# Prédiction des Prix des Billets de Train en Espagne

Ce projet vise à développer un modèle prédictif permettant d'estimer les prix des billets de train en Espagne, basé sur des caractéristiques telles que l'origine, la destination, le type de train, la classe, et les détails temporels.

## Objectifs
- Fournir un outil permettant aux voyageurs d'anticiper les prix des billets.
- Permettre aux compagnies ferroviaires d'optimiser leurs stratégies tarifaires.

## Données
Les données proviennent du dataset Kaggle : [Spanish High-Speed Rail System Ticket Pricing](https://www.kaggle.com/datasets/thegurusteam/spanish-high-speed-rail-system-ticket-pricing/).

### Schéma des données
| Colonne            | Type        | Description                             |
|--------------------|-------------|-----------------------------------------|
| id                 | Integer     | Identifiant unique du trajet            |
| company            | String      | Compagnie ferroviaire                  |
| origin             | String      | Ville d'origine                        |
| destination        | String      | Ville de destination                   |
| departure          | Timestamp   | Heure de départ                       |
| arrival            | Timestamp   | Heure d'arrivée                       |
| duration           | Double      | Durée du trajet (en heures)            |
| vehicle_type       | String      | Type de train                          |
| vehicle_class      | String      | Classe de train                        |
| price              | Double      | Prix du billet                         |
| fare               | String      | Type de tarif                          |
| departure_hour     | Integer     | Heure de départ                       |
| departure_day      | Integer     | Jour du mois                           |
| departure_month    | Integer     | Mois                                   |
| features           | Vector      | Caractéristiques transformées pour le modèle |

## Processus du Projet

### 1. Exploration et Préparation des Données
- **Nettoyage** : Gestion des valeurs manquantes (élimination des lignes avec `price` null, remplissage des colonnes `vehicle_class` et `fare` avec "Unknown").
- **Transformation des dates** : Extraction des informations utiles (éléments temporels comme `departure_hour`, `departure_day`, `departure_month`).
- **Indexation et Encodage** : Conversion des variables catégoriques (ég. `vehicle_type`, `origin`, `destination`) en index numériques avec `StringIndexer`.
- **Assemblage** : Combinaison des caractéristiques numériques et encodées dans une colonne `features` avec `VectorAssembler`.

### 2. Division des Données
- Les données sont divisées en ensembles d'entraînement et de test (à hauteur de 80%-20%) avec la fonction `randomSplit`.

### 3. Implémentation des Modèles
Plusieurs modèles de Machine Learning ont été implémentés pour la prédiction des prix :

1. **Régression Linéaire**
2. **Decision Tree Regressor**
3. **Random Forest Regressor**
4. **Gradiant Boosting**


### 4. Évaluation des Modèles
- **Métriques** :
  - RMSE (Root Mean Squared Error) : Mesure de l'erreur quadratique moyenne.
  - MAE (Mean Absolute Error) : Mesure de l'erreur absolue moyenne.
  - R² (Coefficient de Détermination) : Proportion de la variance expliquée par le modèle.

### 5. Sauvegarde des Résultats
- Les modèles entraînés peuvent être sauvegardés pour des prédictions futures.

## Prérequis
- **PySpark** : Pour la manipulation et le traitement des données.
- **Python 3.7+**.
- **Bibliothèques** :
  - `pandas`, `matplotlib`, `seaborn` (pour la visualisation des données).

## Instructions

### 1. Installation
- Installez les dépendances :
  ```bash
  pip install pyspark pandas matplotlib seaborn
  ```

### 2. Exécution : Lancez le notbook principal "main" 


## Organisation du Projet
------------

    ├── LICENSE             <- N/A license file
    ├── Makefile            <- Makefile with commands like `make data` or `make train`
    ├── README.md           <- The top-level README for individuals using this project
    ├── data
    │   ├── intermediate    <- Intermediate data that has been transformed
    │   ├── processed       <- The final, canonical data sets for modeling
    │   └── raw             <- The original, immutable data dump
    │
    ├── docs                <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models              <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks           <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                          the creator's initials, and a short `-` delimited description, e.g.
    │                          `1.0-ilm-initial-data-exploration`.
    │
    ├── references          <- Data dictionaries, manuals, and all other explanatory materials
    │
    ├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting
    |
    ├── results             <- Generated results from data analysis and fitting models
    │
    ├── src                 <- Source code for use in this project
    │   ├── __init__.py     <- Makes src a Python module
    │   │
    │   ├── data            <- Scripts to load and process data
    │   │   └── load_data.py
    |   |   └── create_int_data
    │   │   └── create_pro_data.py
    │   │
    │   ├── models          <- Scripts for models and fitting processed data
    │   │   └── model.py
    │   │
    │   └── visualization   <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    ├── requirements.txt    <- The requirements file for reproducing the analysis environment, e.g.
    │                          generated with `pip freeze > requirements.txt`
    │
    ├── setup.py            <- makes project pip installable (pip install -e .) so src can be imported
    |
    └── test_environment.py <- checks that correct python interpreter is installed

## Améliorations Futures
- Tester des modèles avancés comme XGBoost.
- Intégrer des données externes (par exemple, événements locaux, conditions météo).
- Mettre en place une API pour permettre des prédictions en temps réel.

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
