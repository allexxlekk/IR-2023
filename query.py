"""This module accepts a search query and optionally a user id
and returns the best matching result from the Elasticsearch Books index"""
from elasticsearch import Elasticsearch
import pandas as pd
from sys import argv

# Coefficients values for the weighted average.
RATING_COEFF = 0.5
RANK_COEFF = 0.5

# TODO refactor the code


def getArgs():
    """Gets the values of the arguments given in the command line."""
    # Case: Query and User ID
    if len(argv) == 3:
        return argv[1], int(argv[2])
    return argv[1], None


def es_connect():
    """Connects to the cluster and notifies user."""

    client = Elasticsearch("http://localhost:9200")
    if client.ping():
        print("Successfully connected to Elasticsearch cluster.")
        print(
            f" Cluster Name: {client.info().body['cluster_name']}\n Cluster UUID: {client.info().body['cluster_uuid']}"
        )
    else:
        print("Could not connect to Elasticsearch cluster.")

    return client


def es_search(es_client, user_query):
    """Queries Elastisearch client based on user input."""
    query_body = {"bool": {"should": {"match": {"book_title": user_query}}}}
    response = es_client.search(index="books", query=query_body, size=1000)
    results = []
    for h in response["hits"]["hits"]:
        result = {
            "isbn": h["_source"]["isbn"],
            "title": h["_source"]["book_title"],
            "author": h["_source"]["book_author"],
            "year_of_publication": h["_source"]["year_of_publication"],
            "rank": float(h["_score"]),
        }
        results.append(result)

    return results


def getRatings(user_id):
    """Get all the ratings of a certain user."""
    df = pd.read_csv("BX-Book-Ratings.csv")
    result = df[df["uid"] == user_id][["uid", "isbn", "rating"]]

    user_ratings = {}  # Create dict isbn : user-rating
    for i, r in result.iterrows():
        user_ratings[r["isbn"]] = float(r["rating"])

    return user_ratings


def calibrateResults(elastic_results, user_ratings):
    """Combine user ratings and elastic search response into the final list."""
    # Final result calculated using weighted average.
    for r in elastic_results:
        rating = float(user_ratings[r["isbn"]]) if r["isbn"] in user_ratings else None
        if rating != None:
            # 0 rated books go to the bottom of the result list.
            if rating == 0:
                r["rank"] = 0
            else:
                r["rank"] = rating * RATING_COEFF + r["rank"] * RANK_COEFF
        else:
            # calculate rank only based on the Elasticsearch result.
            r["rank"] = r["rank"] * RANK_COEFF

    return elastic_results


def getResults(es_client):
    """Query Elasticsearch and return final results."""
    # Get query and user id from the command line.
    user_query, user_id = getArgs()
    # Query elastic search.
    elastic_results = es_search(es_client, user_query)

    # Recalibrate elastic search results based on users ratings.
    if user_id != None:
        user_ratings = getRatings(user_id)
        elastic_results = calibrateResults(elastic_results, user_ratings)

    return elastic_results


def printResults(results):
    """Prints the final result in a readable format"""
    # Sort the results based on rank if user id was provided.
    if len(argv) == 3:
        results = sorted(results, key=lambda x: x["rank"], reverse=True)
        
    # Keep 10% of the resutls
    results = results[:int(len(results)/10):]
    
    print(f"\n{len(results)} Results: \n")
    for r in results:
        print(
            f' Title: {r["title"]}, Author: {r["author"]}\n Matching rank: {r["rank"]}'
        )
        print("--------------------------------------------------------------------")


if __name__ == "__main__":
    es = es_connect()
    results = getResults(es)
    printResults(results)
