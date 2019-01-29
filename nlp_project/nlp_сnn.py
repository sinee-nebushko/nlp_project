from keras.datasets import imdb
from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.layers import LSTM, Dense, Conv1D, MaxPooling1D
max_review_length = 280
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=10000)

X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)

embedding_vector_length = 32
model = Sequential()
model.add(Embedding(10000, embedding_vector_length, input_length=max_review_length))
model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(LSTM(100))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=2, batch_size=200)
model.evaluate(X_test, y_test, verbose=0)

# model.summary()
# scores = model.evaluate(X_test, y_test, verbose=0)
# print('Accuracy: %.2f' % (scores[1]*100))

