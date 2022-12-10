"""This module accepts a search query and optionally a user id
and returns the best matching result from the Elasticsearch Books index"""
from elasticsearch import Elasticsearch
import pandas as pd
from sys import argv


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
            f" Cluster Name: {client.info().body['cluster_name']}\nCluster UUID: {client.info().body['cluster_uuid']}"
        )
    else:
        print("Could not connect to Elasticsearch cluster.")

    return client


def es_search(es_client, user_query, user_id=None):
    """Queries Elastisearch client based on user input."""
    query_body = {"query": {"bool": {"must": {"match": {"book_title": user_query}}}}}
    # TODO  make better query
    response = es_client.search(index="books", body=query_body, size=10)
    # TODO combine user rating
    # TODO create metric with weighted average perhaps
    # TODO refactor the code
    for h in response["hits"]["hits"]:
        result = {
            "Title": h["_source"]["book_title"],
            "Author": h["_source"]["book_author"],
            "Year of Publication": h["_source"]["year_of_publication"],
            "Ranking Score": h["_score"],
        }

        print(result)


def getRatings(user_id):
    """Get all the ratings of a certain user."""
    df = pd.read_csv("BX-Book-Ratings.csv")
    result = df[df["uid"] == user_id][["uid", "isbn", "rating"]]

    user_ratings = {}  # Create dict isbn : user-rating
    for i, r in result.iterrows():
        user_ratings[r["isbn"]] = r["rating"]

    return user_ratings


if __name__ == "__main__":
    # es = es_connect()
    # es_search(es, "mythology")
    # getRatings(3)
    query, ID = getArgs()
    print(getRatings(ID))
