import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def dist_missing(missing_values):
    plt.figure(figsize=(10, 6))
    sns.barplot(x="column", y="missing_values", data=missing_values)
    plt.xticks(rotation=45)
    plt.title("Valeurs manquantes par colonne")
    plt.xlabel("Colonnes")
    plt.ylabel("Nombre de valeurs manquantes")
    plt.show()


def dist_ticket_price(df):
    prices = df.select("price").toPandas()["price"]

    plt.figure(figsize=(8, 5))
    plt.hist(prices, bins=30, color='blue', alpha=0.7)
    plt.title("Distribution des prix des billets")
    plt.xlabel("Prix (€)")
    plt.ylabel("Fréquence")
    plt.show()

def dist_vehicle_type(df):
    vehicle_types = df.select("vehicle_type").toPandas()

    plt.figure(figsize=(8, 5))
    sns.countplot(x='vehicle_type', data=vehicle_types, palette='viridis')
    plt.title("Répartition par type de véhicule")
    plt.xticks(rotation=45)
    plt.ylabel("Nombre de trajets")
    plt.show()

def dist_price_by_vehicle_class(df):
    vehicle_data = df.select("vehicle_type", "vehicle_class", "price").toPandas()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='vehicle_type', y='price', hue='vehicle_class', data=vehicle_data)
    plt.title("Prix par type de véhicule et classe")
    plt.xticks(rotation=45)
    plt.ylabel("Prix (€)")
    plt.show()

def dist_price_by_origin_destination(df):
    origin_dest_data = df.select("origin", "destination", "price").toPandas()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='origin', y='price', data=origin_dest_data)
    plt.title("Prix moyen par ville d'origine")
    plt.xticks(rotation=45)
    plt.ylabel("Prix (€)")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='destination', y='price', data=origin_dest_data)
    plt.title("Prix moyen par ville de destination")
    plt.xticks(rotation=45)
    plt.ylabel("Prix (€)")
    plt.show()

def dist_mean_price_by_departure_hour(df):
    avg_price_by_hour = (
        df.groupBy("departure_hour")
        .mean("price")
        .toPandas()
        .sort_values(by="departure_hour")
    )

    plt.figure(figsize=(8, 5))
    plt.bar(avg_price_by_hour['departure_hour'], avg_price_by_hour['avg(price)'], color='orange')
    plt.title("Prix moyen par heure de départ")
    plt.xlabel("Heure de départ")
    plt.ylabel("Prix moyen (€)")
    plt.show()
