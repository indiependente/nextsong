import numpy as np
# from numpy import linalg
# from numpy.linalg import norm
# from scipy.spatial.distance import squareform, pdist

import sklearn
from sklearn.manifold import TSNE
# from sklearn.datasets import load_digits
# from sklearn.preprocessing import scale

# from sklearn.metrics.pairwise import pairwise_distances
# from sklearn.manifold.t_sne import (_joint_probabilities,
#                                     _kl_divergence)
# from sklearn.utils.extmath import _ravel

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
    palette = np.array(sns.color_palette("hls", 10))

    # We create a scatter plot.
    f = plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40)
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    ax.axis('off')
    ax.axis('tight')

    return f, ax, sc


# Random state.
RS = 20150101

D = pickle.load(open('distance_matrix.p', 'rb'))

proj = TSNE(n_components=2, random_state=RS, metric='precomputed').fit_transform(D)
scatter(proj)
plt.savefig('tsne.png', dpi=120)
