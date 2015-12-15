
# coding: utf-8

# In[80]:

import numpy as np
import cPickle as pickle
from pydtw import dtw2d
from joblib import Parallel, delayed


# In[81]:

def pickle_this(data, filename='distance_matrix.p'):
    pickle.dump(data, open(filename, 'wb'))


# In[82]:

def inner_loop(sample, i, n):
    row = np.zeros((n,))
    for j in xrange(i, n):
        row[j] = dtw2d(sample[i], sample[j])[-1,-1]
    return row


# In[83]:

sample = pickle.load( open( 'sample_pitches.p', 'rb' ) )
n = sample.shape[0]


# In[95]:

distance_matrix = np.asmatrix(Parallel(n_jobs=6)(delayed(inner_loop)(sample, i, n) for i in range(n)))
pickle_this(distance_matrix)

