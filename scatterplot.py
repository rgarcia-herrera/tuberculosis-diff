from pprint import pprint
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from slugify import slugify

from design import contrasts_tb, contrasts_macrophage


def scatter_plot(title, pair, color='red', top=10):

    # place dots
    x = np.genfromtxt(pair[0]['path'], delimiter=',', usecols=(1,))
    y = np.genfromtxt(pair[1]['path'], delimiter=',', usecols=(1,))

    plt.plot([round(x.min()), round(y.max())],
             [round(x.min()), round(y.max())], color='red', alpha=0.5)

    plt.scatter(x, y, alpha=0.7, marker='.', color=color)


    # place labels
    genes = np.genfromtxt(pair[0]['path'], delimiter=',', usecols=(0,), dtype=str)
    d = np.stack([genes, x, y, (x - y)], axis=-1)
    d = [[x[0],
          float(x[1]),
          float(x[2]),
          abs(float(x[3]))] for x in d]
    d.sort(key=lambda x: x[3])
    top_genes = d[-top:]

    for g in top_genes:
        plt.annotate(g[0],
                     xy=(float(g[1]), float(g[2])),
                     xytext=(30, -40),
                     textcoords='offset points', ha='right', va='top',
                     bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.5),
                     arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

    # add main and axes titles
    plt.title(title)
    plt.xlabel(pair[0]['title'])
    plt.ylabel(pair[1]['title'])
    plt.axis('equal')

    # write out
    plt.savefig("plots/%s" % slugify(title))
    plt.cla()


for title in contrasts_tb:
    scatter_plot(title, contrasts_tb[title], color='purple', top=5)


for title in contrasts_macrophage:
    scatter_plot(title, contrasts_macrophage[title], color='blue', top=5)
