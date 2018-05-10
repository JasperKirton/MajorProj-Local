import gensim
import pickle
import os

# loading the model
d2v_model = gensim.models.doc2vec.Doc2Vec.load('doc2vec.model')

# start testing
# printing the vector of document at index 1 in docLabels

#docvec = d2v_model.docvecs[0]
#print(docvec)

# printing the vector of the file using its name
#docvec = d2v_model.docvecs['train.txt']  # if string tag used in training
#print(docvec)

# to get most similar document with similarity scores using document-index
#similar_doc = d2v_model.docvecs.most_similar(5341)
#print(similar_doc)

# to get most similar document with similarity scores using document-name
sims = d2v_model.docvecs.most_similar('6031.txt')
print(sims)


# to get vector of document that are not present in corpus
#docvec = d2v_model.docvecs.infer_vector('war.txt')
# print(docvec)

# pickle
#d2v_model.save('model.pkl', pickle_protocol=2)

'''

dest = os.path.join('d2vModel', 'pkl_objects')

if not os.path.exists(dest):
    os.makedirs(dest)


pickle.dump(d2v_model,
            open(os.path.join(dest, 'model.pkl'), 'wb'),
            protocol=4)
'''