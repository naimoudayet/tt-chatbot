import json
import random
import tensorflow
from tensorflow.python.ops.variables import report_uninitialized_variables
import tflearn
import numpy
import nltk
import pickle
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

with open("./bot/data.json") as file:
    data = json.load(file)

try:
    with open("./bot/data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("./bot/data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

# tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)  # 8 neurons for the hidden layers
net = tflearn.fully_connected(net, 8)  # 8 neurons for the hidden layers
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)  # DNN is a type of neural network
model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("./bot/model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


def webhook(question):
    results = model.predict([bag_of_words(question, words)])[0]
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    

    if results[results_index] > 0.5:

        for tg in data["intents"]: 
            if tg['tag'] == tag:

                responses = tg['responses']

        return random.choice(responses)

    else:
        return "Je n'ai pas compris, réessayez."