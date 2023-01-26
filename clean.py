import pandas as pd
import random


df = pd.read_csv("BX-Users-clean.csv")

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

df = pd.read_csv('BX-Users-clean.csv')
countries = [] 
for _,row in df.iterrows():
    if row["location"] not in countries:
        countries.append(row["location"])
        
print(len(countries))

# for i,row in df.iterrows():
#     print(i)
#     country_enc = countries.index(row['location'])
#     df.at[i, 'country_encoding'] = country_enc
    
# df.to_csv("test2.csv", index=False)
    
