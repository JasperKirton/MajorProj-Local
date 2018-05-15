#Import all dependencies

import gensim
from nltk import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from os import listdir
# from os.path import isfile, join

# now create a list that contains the name of all the text file in
# your data folder

docLabels = []
docLabels = [f for f in listdir("/Users/jasperkirton/Documents/gSMiths/MajorProj/Train/") if f.endswith('.txt')]

# create a list data that stores the content of all text files in order of their names in docLabels

data = []
for doc in docLabels:
    data.append(open("/Users/jasperkirton/Documents/gSMiths/MajorProj/Train/" + doc).read())

#tokenizer = RegexpTokenizer(r'\w+')  # think i'm discarding this as it's excluding punctuation, instead we use the following:
#tokens = word_tokenize(text)
stopword_set = set(stopwords.words('english'))


# This function does all cleaning of data using the two objects above
def nlp_clean(data):
    new_data = []
    for d in data:
        new_str = d.lower()
        dlist = word_tokenize(new_str)
        dlist = list(set(dlist).difference(stopword_set))
        new_data.append(dlist)
    return new_data


class LabeledLineSentence(object):

    def __init__(self, doc_list, labels_list):

        self.labels_list = labels_list
        self.doc_list = doc_list

    def __iter__(self):

        for idx, doc in enumerate(self.doc_list):
            yield gensim.models.doc2vec.TaggedDocument(doc, [self.labels_list[idx]])  # labeled sentence is deprecated, still loads i guess, maybe a better way to do it...


data = nlp_clean(data)

# iterator returned over all docs
it = LabeledLineSentence(data, docLabels)

model = gensim.models.Doc2Vec(vector_size=300, min_count=2, alpha=0.025)
model.build_vocab(it)


model.train(it, total_examples=model.corpus_count, epochs=200)  # using inner epochs seems to work well

# saving the created model and confirm
model.save('doc2vec.model')
print('model saved')




