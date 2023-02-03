import numpy as np
import pandas as pd
from keras.preprocessing.text import one_hot
from keras.utils import pad_sequences
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding




# Word Embedding Parameters
INPUT_DIM = 112350  # Size of vocabulary
OUTPUT_DIM = 100    # Size of the output vectors
INPUT_LENGTH = 50   # Size of largest input text

ratings = []
summaries = []
df_data = pd.read_csv('train.csv')
for i,row in df_data.iterrows():
    ratings.append(int(row['rating']))
    summaries.append(row['summary'])


# Encode summaries for embedding
encoded_summaries = [one_hot(d, INPUT_DIM) for d in summaries]
print(encoded_summaries)
padded_summaries = pad_sequences(encoded_summaries, maxlen=INPUT_LENGTH, padding='post')

# Create One Hot Encoding For Rating
ratings = np.array(ratings)
labels = to_categorical(ratings - 1, num_classes=10)

# define the model
model = Sequential()
model.add(Embedding(INPUT_DIM, 8, input_length=INPUT_LENGTH, name="embeddings"))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))
# compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# summarize the model
print(model.summary())
# fit the model
model.fit(padded_summaries, labels, epochs=50, verbose=1)
# evaluate the model
loss, accuracy = model.evaluate(padded_summaries, labels, verbose=1)
print('Accuracy: %f' % (accuracy*100))
