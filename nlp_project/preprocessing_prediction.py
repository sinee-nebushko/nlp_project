from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import text_to_word_sequence
import nlp_сnn
import numpy as np
import re


def text_to_sequences(text):
    words = text_to_word_sequence(text)
    index = nlp_сnn.index
    start_char = 1
    index_from = 3
    sequence = [start_char] + [index_from + index[w] for w in words if w in index]
    return [sequence]


def clean_text(text):
    text = text.lower()
    text = re.sub('<br\s+/>', '', text)
    text = re.sub('  +', ' ', text)
    text = re.sub('ß', 'ss', text)
    text = re.sub('’', "'", text)
    text = re.sub('[^a-zA-Z0-9!.,?;:\-()\' äàâæçéèêîïíìöôóòœüûúùÿ]+', '', text)
    text = re.sub(' +', ' ', text)
    return text


def prepr_pred(text):
    text = clean_text(text)
    sequences = text_to_sequences(text)
    padded_seq = pad_sequences(sequences, maxlen=280)
    model = nlp_сnn.model
    with nlp_сnn.graph.as_default():
        pred = model.predict(np.array(padded_seq))

    middle_acc = int(pred.mean()*100)
    if middle_acc > 50:
        a = 'Positive'
        m_a = middle_acc
    else:
        a = 'Negative'
        m_a = 100-middle_acc
    return a, m_a




