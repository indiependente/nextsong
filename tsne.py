import numpy as np

import sklearn
from sklearn.manifold import TSNE
from dendro import symmetrize
import matplotlib.pyplot as plt
import matplotlib

import seaborn as sns
import cPickle as pickle

sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", font_scale=1.5,
                rc={"lines.linewidth": 2.5})

def scatter(x):
    # We choose a color palette with seaborn.
    # palette = np.array(sns.color_palette("hls", 10))

    # We create a scatter plot.
    f = plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40)
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    ax.axis('off')
    ax.axis('tight')

    return f, ax, sc


# Random state. If None, use the numpy.random singleton 
RS = None 

D = symmetrize(pickle.load(open('distance_matrix.p', 'rb')))

proj = TSNE(n_components=2, random_state=RS, metric='precomputed').fit_transform(D)
scatter(proj)
plt.savefig('tsne.png', dpi=120)
