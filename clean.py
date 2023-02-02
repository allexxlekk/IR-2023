import pandas as pd
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize
import re
import random


# df = pd.read_csv("BX-Users-clean.csv")

# for i, row in df.iterrows():

#     print(i)
#     new_location = row["location"].split(",")[-1].strip()
#     df.loc[i, "location"] = new_location.lower()

# df.to_csv("test2.csv", index=False)


# AGE AND COUNTRY PMF
# ages = []
# countries = []

# for i, row in df.iterrows():
#     if row["age"] > 0:
#         ages.append(row["age"])
#     if type(row["location"]) != float:
#         countries.append(row["location"])


# rPLACE MISSING VALUES
# df = df.fillna(0)
# for i, row in df.iterrows():
#     print(i)
#     age = random.choice(ages)
#     country = random.choice(countries)
#     if row["age"] == 0:
#         df.at[i, "age"] = age
#     if row["location"] == 0:
#         df.at[i, "location"] = country


# df.to_csv("test2.csv", index=False)

# df = pd.read_csv('BX-Users-clean.csv')
# countries = []
# for _,row in df.iterrows():
#     if row["location"] not in countries:
#         countries.append(row["location"])

# print(len(countries))

# for i,row in df.iterrows():
#     print(i)
#     country_enc = countries.index(row['location'])
#     df.at[i, 'country_encoding'] = country_enc

# df.to_csv("test2.csv", index=False)


# Clean ratings
# users_df = pd.read_csv('BX-Users-clean.csv')
# ratings_df = pd.read_csv('BX-Book-Ratings.csv')
# uid_list = []
# isbn_list = []
# ratings_list = []

# for i,row in ratings_df.iterrows():
#     print(i)
#     uid = row['uid']
#     check_df = users_df[users_df["uid"] == uid]

#     if not check_df.empty:
#         isbn = str(row["isbn"])
#         rating = int(row["rating"])

#         uid_list.append(uid)
#         isbn_list.append(isbn)
#         ratings_list.append(rating)

# df = pd.DataFrame(list(zip(uid_list, isbn_list, ratings_list)),
#                columns =['uid', 'isbn', 'rating'])

# df.to_csv('BX-Book-Ratings-clean.csv')

# users_df = pd.read_csv('BX-Users-clean.csv')
# ratings_df = pd.read_csv('BX-Book-Ratings-clean.csv')

# # for i,row in ratings_df.iterrows():
# #     print(i)
# #     uid = row['uid']
# #     check_df = users_df[users_df["uid"] == uid]

# #     if not check_df.empty:
# #         isbn = str(row["isbn"])
# #         rating = int(row["rating"])

# #         uid_list.append(uid)
# #         isbn_list.append(isbn)
# #         ratings_list.append(rating)

# # df = pd.DataFrame(list(zip(uid_list, isbn_list, ratings_list)),
# #                columns =['uid', 'isbn', 'rating'])

# # df.to_csv('BX-Book-Ratings-clean.csv')


# ghosts = []
# for i,row in ratings_df.iterrows():
#     uid = row["uid"]
#     user_cluster = users_df[users_df["uid"] == uid]
#     if user_cluster.empty and uid not in ghosts:
#         ghosts.append(uid)
#         print(uid)
#     if len(ghosts) == 3000:
#         break

# for i,g in enumerate(ghosts):
#     print(i)
#     ratings_df = ratings_df.drop(ratings_df[ratings_df.uid == g].index)

# ratings_df.to_csv('BX-Book-Ratings-clean.csv', index=False)
# cluster_ratings = [{"0195153448" : 3, "0345377443": 5}, {"0679425608": 8}]
# df_books = pd.read_csv('BX-Books.csv')
# for i, d in enumerate(cluster_ratings):
#     print("Cluster: ", i)
#     isbn_list = []
#     summary_list = []
#     rating_list = []
#     for key, value in d.items():
#         book_isbn = key
#         print(book_isbn)
#         book_summary = df_books[df_books["isbn"] == key]['summary'].values[0]
#         print(book_summary)
#         book_rating = int(value)

#         isbn_list.append(book_isbn)
#         summary_list.append(book_summary)
#         rating_list.append(book_rating)

#     clusterdf = pd.DataFrame({"isbn" : isbn_list, "summary": book_summary, "rating" : rating_list})

#     clusterdf.to_csv(f'cluster{i+1}.csv', index= False)

# df_cluster1 = pd.read_csv('cluster1.csv')
# print(df_cluster1)
# d = {isbn : rating, isbn2 : rating ....}

# # Extended list of stop words from nltk.
# stop_words = list(stopwords.words("english"))
# # Common unrecognized characters.
# stop_words.extend(["”", "“", "’", "s", "—", "–", "%", "‘", "…", "[", "]", ",", "."])

# df_books = pd.read_csv("BX-Books.csv")

# for i, row in df_books.iterrows():
#     print(i)
#     summary = row["summary"]
#     summary = re.sub(r'[^a-zA-Z0-9\s\-]+', '', summary)
#     text_tokens = word_tokenize(summary)

#     tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
#     summary = (" ").join(tokens_without_sw)
#     df_books.at[i, "summary"] = summary

# df_books.to_csv('test.csv', index=False)

# df_books = pd.read_csv('BX-Books-clean.csv')
# with open('vocabulary.dat', 'w') as f:
#     vocab = []
#     for i, row in df_books.iterrows():
#         print(i)
#         summary = row['summary']
#         summary_wordlist = summary.split(' ')
#         for word in summary_wordlist:
#             if word not in vocab:
#                 vocab.append(word)
#     print('Writing to file, please wait....')
#     for word in vocab:

#         f.write(word+'\n')

# df_books.to_csv('test.csv', index = False)

# df_books = pd.read_csv('BX-Books-clean.csv')
# max_l = 0
# for i,row in df_books.iterrows():
#     print(i)
#     summary = row['summary']
#     summary_list = summary.split(' ')
#     if len(summary_list) > max_l:
#         max_l = len(summary_list)

# print(max_l)


# # df_reviews = pd.read_csv('BX-Book-Ratings.csv')
# # isbn_list = []
# # rating_list = []
# # for i,row in df_reviews.iterrows():
# #     print(i)
# #     if row['rating'] != 0:
# #         isbn_list.append(row['isbn'])
# #         rating_list.append(int(row['rating']))
# # new_df = pd.DataFrame({"isbn": isbn_list, "rating" : rating_list})
# # new_df.to_csv('reviews-train.csv', index=False)
# df_ratings = pd.read_csv("BX-Book-Ratings-clean.csv")
# user_ratings = df_ratings[df_ratings["rating"] > 0]
# books_cluster = {}
# for k, row in user_ratings.iterrows():
#     print(k)
#     book_isbn = str(row["isbn"])
#     book_isbn = book_isbn.zfill(10)
#     book_rating = float(row["rating"])

#     if book_isbn not in books_cluster.keys():
#         books_cluster[book_isbn] = {
#             "acc_rating": book_rating,
#             "users_rated": 1,
#         }
#     else:
#         books_cluster[book_isbn]["acc_rating"] += book_rating
#         books_cluster[book_isbn]["users_rated"] += 1
        
# books_cluster_average = {}
# for isbn,values in books_cluster.items():
#     total_sum = float(values['acc_rating'])
#     no_ratings = float(values['users_rated'])
    
#     books_cluster_average[isbn] = int(total_sum/ no_ratings)


# for key, value in books_cluster_average.items():
#     print(key, value)

# df_books = pd.read_csv("BX-Books-clean.csv")
# isbn_list = []
# summary_list = []
# rating_list = []
# i = 0
# for key, value in books_cluster_average.items():
#     i += 1
#     print(i)
#     book_isbn = str(key)
#     book_summary = df_books[df_books["isbn"] == key]["summary"].values[0]
#     book_rating = int(value)

#     isbn_list.append(book_isbn)
#     summary_list.append(book_summary)
#     rating_list.append(book_rating)

# clusterdf = pd.DataFrame(
#     {"isbn": isbn_list, "summary": summary_list, "rating": rating_list}
# )

# clusterdf.to_csv("test.csv", index=False)
