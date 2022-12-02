"""This module accepts a search query and optionally a user id
and returns the best matching result from the Elasticsearch Books index"""
from elasticsearch import Elasticsearch
import pandas as pd


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
    """Queries Elastisearch client based on user input"""
    query_body = {"query": {"bool": {"must": {"match": {"book_title": user_query}}}}}
    response = es_client.search(index="books", body=query_body, size = 10)
    for h in response['hits']['hits']:
        result = {
            "Title": h['_source']['book_title'],
            "Author": h['_source']['book_author'],
            "Year of Publication" : h['_source']['year_of_publication'],
            "Ranking Score": h['_score']
        }

        print(result)

if __name__ == "__main__":
    es = es_connect()
    es_search(es, "mythology")
