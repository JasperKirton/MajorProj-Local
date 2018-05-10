import pickle
import os

dest = os.path.join('d2vModel', 'pkl_objects')

if not os.path.exists(dest):
    os.makedirs(dest)

pickle.dump(stopword_set,
            open(os.path.join(dest, 'stopwords.pkl'), 'wb'),
            protocol=4)

pickle.dump(d2v_model,
            open(os.path.join(dest, 'model.pkl'), 'wb'),
            protocol=4)



