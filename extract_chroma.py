import os
import sys
import hdf5_getters
import cPickle as pickle


def dump_pitches(rootdir = './data/', filename = 'pitches.p'):
    h5list = []
    pitches = []

    for subdir, dirs, files in os.walk(rootdir):
        for f in files:
            if f.lower().endswith('.h5'):
                h5list.append(hdf5_getters.open_h5_file_read(os.path.join(subdir, f)))
                pitches.append(hdf5_getters.get_segments_pitches(h5list[-1]))
                h5list[-1].close()
    del h5list

    pickle.dump( pitches, open( filename, "wb" ) )

def read_pitches(filename = 'pitches.p'):
    return pickle.load( open( 'pitches.p', 'rb' ) )





if __name__ == '__main__':
    dump_pitches()