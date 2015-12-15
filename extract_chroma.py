import os
import sys
import hdf5_getters
import numpy as np
import cPickle as pickle
from random import sample

def dump_pitches(rootdir = './data/', filename = 'pitches.p'):
    h5list = []
    pitches = []
    tags = []

    for subdir, dirs, files in os.walk(rootdir):
        for f in files:
            if f.lower().endswith('.h5'):
                h5list.append(hdf5_getters.open_h5_file_read(os.path.join(subdir, f)))
                pitches.append(hdf5_getters.get_segments_pitches(h5list[-1]))
                tags.append('%s - %s - %s - %s' % (hdf5_getters.get_artist_name(h5list[-1]), hdf5_getters.get_title(h5list[-1]), hdf5_getters.get_year(h5list[-1]), hdf5_getters.get_tempo(h5list[-1])))
                h5list[-1].close()
    del h5list

    pickle.dump( pitches, open( filename, 'wb' ) )
    pickle.dump( tags, open( 'tags.p', 'wb' ) )


def dump_sample(n = 100, filename = 'sample_pitches.p'):
    pitches = np.asarray(read_pitches())
    tags = np.asarray(read_tags())
    size = len(pitches)
    if len(tags) != size:
        print 'Error: pitches and tags length must match!'
        raise
    if n > size: 
        print 'Error: n must be less or equal the size of the dataset!'
        raise
    idx = np.random.choice(size, n, replace=False) 
    pickle.dump(pitches[idx], open (filename, 'wb'))
    pickle.dump(tags[idx], open ('sample_tags.p', 'wb'))

def read_pitches(filename = 'pitches.p'):
    return pickle.load( open( filename, 'rb' ) )

def read_tags():
    return pickle.load( open( 'tags.p', 'rb' ) )

def read_sample(filename = 'sample_pitches.p'):
    return pickle.load( open( 'sample_pitches.p', 'rb' ) )

def read_sample_tags(filename = 'sample_tags.p'):
    return pickle.load( open( 'sample_tags.p', 'rb' ) )


###########################################################
if __name__ == '__main__':
    dump_pitches()
    dump_sample(1000)
