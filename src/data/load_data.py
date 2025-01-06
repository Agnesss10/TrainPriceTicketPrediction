""" This module helps locate directories in the main project directory.
"""
from pathlib import Path

# path for the project directory
project_dir = Path(__file__).resolve().parents[3]


def get_data_dir() -> Path:
    """
    Gets raw directory path.
    """
    return project_dir / 'data'


def get_results_dir() -> Path:
    """
    Gets results directory path.
    """
    return project_dir / 'results'


def get_reports_dir() -> Path:
    """
    Gets reports directory path.
    """
    return project_dir / 'reports'


def get_references_dir() -> Path:
    """
    Gets references directory path.
    """
    return project_dir / 'references'

def load_data(file_path, spark):
    """
    Charge les données à partir du chemin spécifié.

    Args:
        file_path (str): Chemin vers le fichier CSV.

    Returns:
        pandas.DataFrame: Données chargées sous forme de DataFrame.
    """
    try:
        data = spark.read.csv(file_path, header=True, inferSchema=True)
        print("Données chargées avec succès.")
        return data
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return None
