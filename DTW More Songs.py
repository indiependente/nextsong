
# coding: utf-8

# In[1]:

#get_ipython().magic(u'matplotlib inline')
#import matplotlib
#import matplotlib.pyplot as plt
#import librosa
import os
import sys
from extract_chroma import read_pitches
from extract_chroma import read_sample
from random import sample
import hdf5_getters
import numpy as np
from dtw import dtw
from numpy.linalg import norm
import cPickle as pickle
#matplotlib.rcParams['figure.figsize'] = (10.0, 8.0)


# In[2]:

def norm2(x, y):
    return norm(x - y, ord=2)

def get_song_info(h5):
    print '%s - %s | (%s) | %s bpm' % (hdf5_getters.get_artist_name(h5), hdf5_getters.get_title(h5), hdf5_getters.get_year(h5), hdf5_getters.get_tempo(h5))

def pickle_this(data, filename):
    pickle.dump(data, open(filename, 'wb'))    

# In[3]:


h5sample = read_sample()
n = len(h5sample)
# print 'n:', n
# In[6]:

# print [ [(i,j,dtw(x, y, dist=norm2) for i, x in enumerate(h5sample)] for j, y in enumerate(h5sample) if i != j ]

distance_matrix = np.zeros((n,n))

for i in xrange(n):
    for j in xrange(i, n):
        # print '(%s,%s)' % (i,j)
        distance_matrix[i][j] = dtw(h5sample[i], h5sample[j], norm2)

# print np.shape(distance_matrix)
pickle_this(distance_matrix, 'distance_matrix.p')
