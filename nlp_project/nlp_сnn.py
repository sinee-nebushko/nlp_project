from keras.datasets import imdb
from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.layers import LSTM, Dense, Conv1D, MaxPooling1D


def nlp_imdb_learn():
    max_review_length = 280
    (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

    x_train = sequence.pad_sequences(x_train, maxlen=max_review_length)
    x_test = sequence.pad_sequences(x_test, maxlen=max_review_length)

    embedding_vector_length = 32
    model = Sequential()
    model.add(Embedding(10000, embedding_vector_length, input_length=max_review_length))
    model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(LSTM(100))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=2, batch_size=200)
    model.evaluate(x_test, y_test, verbose=0)

    # model.summary()
    # scores = model.evaluate(X_test, y_test, verbose=0)
    # print('Accuracy: %.2f' % (scores[1]*100))
    return model


