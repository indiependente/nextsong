
# coding: utf-8

# In[80]:

import numpy as np
import cPickle as pickle
from pydtw import dtw2d
from joblib import Parallel, delayed
from collections import defaultdict
import itertools
import joblib.parallel

class CallBack(object):
    completed = defaultdict(int)

    def __init__(self, index, parallel):
        self.index = index
        self.parallel = parallel

    def __call__(self, index):
        CallBack.completed[self.parallel] += 1
        if CallBack.completed[self.parallel] % 743 == 0:
            print("{}%".format(CallBack.completed[self.parallel]/74))
        if self.parallel._original_iterable:
            self.parallel.dispatch_next()

joblib.parallel.CallBack = CallBack

# In[81]:

def pickle_this(data, filename='distance_matrix.p'):
    pickle.dump(data, open(filename, 'wb'))



# In[83]:

sample = pickle.load( open( 'pitches.p', 'rb' ) )
n = len(sample)


# In[95]:

distance_matrix = np.asmatrix(Parallel(n_jobs=6)(delayed(dtw2d)(sample[i], sample[j]) for i,j in itertools.product(range(n), range(n)) if i < j))
pickle_this(distance_matrix)

