from pprint import pprint
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
from slugify import slugify

from design import contrasts_tb


def scatter_plot(title, pair, color='red'):

    x = np.genfromtxt(pair[0]['path'], delimiter=',', usecols=(1,))
    y = np.genfromtxt(pair[1]['path'], delimiter=',', usecols=(1,))

    plt.scatter(x, y, alpha=0.11, color=red, marker='.')
    plt.title(title)
    plt.xlabel(pair[0]['title'])
    plt.ylabel(pair[1]['title'])
    plt.savefig("plots/%s" % slugify(title))
    plt.cla()

for title in contrasts_tb:
    scatter_plot(title, contrasts_tb[title])
