from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from nlp_сnn import nlp_imdb_learn
import numpy as np
import re


def clean_text(text):
    text = text.lower()
    text = re.sub('<br />', '', text)
    text = re.sub('(\n|\r|\t)+', ' ', text)
    text = re.sub('ß', 'ss', text)
    text = re.sub('’', "'", text)
    text = re.sub('[^a-zA-Z0-9!.,?;:\-()\' äàâæçéèêîïíìöôóòœüûúùÿ]+', '', text)
    text = re.sub(' +', ' ', text)
    return text


def prepr_pred():
    with open(r'nlp_project\text.txt', 'r', encoding='utf-8') as f:
        t = f.read()
        text = clean_text(t)
        tokenizer = Tokenizer(num_words=100)
        tokenizer.fit_on_texts(text)

        sequences = tokenizer.texts_to_sequences(text)
        padded_seq = pad_sequences(sequences, maxlen=280)
        model = nlp_imdb_learn()
        pred_cl = model.predict_classes(np.array(padded_seq))
        pred = model.predict(np.array(padded_seq))
        middle_acc_cl = pred_cl.mean()
        middle_acc = pred.mean()*100
        middle_acc = int(middle_acc)
        if middle_acc_cl > 0.3:
            a = 'Positive'
        else:
            a = 'Negative'

    return a, middle_acc, t




