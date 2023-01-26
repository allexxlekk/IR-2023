import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()
from sklearn.cluster import KMeans

CLUSTERS = 6


def elbow(data):
    """
    Using the Elbow Method to Identify
    optimal number of clusters.
    """
    wcss = []
    for i in range(1, 25):
        kmeans = KMeans(i)
        kmeans.fit(data)
        wcss_iter = kmeans.inertia_
        wcss.append(wcss_iter)

    number_of_clusters = range(1, 25)
    plt.plot(number_of_clusters, wcss)
    plt.title("The Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("Within Cluster Sum-of-Squares")
    plt.show()


def loadData(filename):
    """
    Load the data from csv
    and return dataframe for clustering
    """
    df = pd.read_csv(filename)
    x = []
    y = []
    for _, row in df.iterrows():
        x.append(float(row["age"]))
        y.append(float(row["country_encoding"]))

    newdf = pd.DataFrame(list(zip(x, y)), columns=["AGE", "COUNTRY"])

    return newdf


def showClusters(data_with_clusters):
    # Plot Results
    plt.scatter(
        data_with_clusters["AGE"],
        data_with_clusters["COUNTRY"],
        c=data_with_clusters["cluster"],
        cmap="rainbow",
    )
    plt.xlabel("USER AGE")
    plt.ylabel("USER COUNTRY")
    plt.xlim(18, 100)
    plt.show()


def clustering(filename):
    """Perform Clustering"""
    df = loadData(filename)

    kmeans = KMeans(CLUSTERS, n_init=10)
    id_clusters = kmeans.fit_predict(df)
    data_with_clusters = df.copy()
    data_with_clusters["cluster"] = id_clusters

    showClusters(data_with_clusters)


if __name__ == "__main__":

    # Save clustered data to csv

    # showClusters(data_with_clusters)
    # dfnew = pd.read_csv("test2.csv")
    # dfnew["Cluster"] = id_clusters
    # dfnew.to_csv("test.csv", index=False)

    # Load clustered users
    df_users = pd.read_csv("test.csv")

    for i in range(0, CLUSTERS):

        print("CLUSTER : ", i)

        books_cluster =  {} #{isbn : accumlative_rating, users_rated } => {isbn: avg_rating}
        # Get users dataframe of a specific cluster
        cluster_users = df_users[df_users["cluster"] == i]

        for _, row in cluster_users.iterrows():
            
            # User id
            user_id = row['uid']
            print("----------")
