import numpy as np
import pandas as pd
from keras.preprocessing.text import one_hot
from keras.utils import pad_sequences
from keras.utils import to_categorical
# TODO Create embedding layer
#   - Keras
#   - One hot encoding from vocabulary
#   - Model

# TODO Create output vector
#   - One hot encoding


# Word Embedding Parameters
INPUT_DIM = 112350  # Size of vocabulary
OUTPUT_DIM = 100    # Size of the output vectors
INPUT_LENGTH = 50   # Size of largest input text

ratings = []
df_data = pd.read_csv('temp.csv')
for i,row in df_data.iterrows():
    ratings.append(int(row['rating']))
    

# Example of movie ratings (1 to 10)
labels = np.array(ratings)

# One-hot encoding of the ratings
one_hot_ratings = to_categorical(ratings - 1, num_classes=10)

print(one_hot_ratings)