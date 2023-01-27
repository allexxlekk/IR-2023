import pandas as pd
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
