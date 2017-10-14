import numpy as np
from slugify import slugify
from pprint import pprint


from design import contrasts_tb, contrasts_macrophage


def delta(title, pair):
    genes = np.genfromtxt(pair[0]['path'], delimiter=',', usecols=(0,), dtype=str)
    x = np.genfromtxt(pair[0]['path'], delimiter=',', usecols=(1,))
    y = np.genfromtxt(pair[1]['path'], delimiter=',', usecols=(1,))

    np.savetxt("data/deltas/%s.tsv" % slugify(title),
               np.stack([genes, (x - y)], axis=-1),
               fmt='%s')


for title in contrasts_macrophage:
    d = delta(title, contrasts_macrophage[title])

for title in contrasts_tb:
    d = delta(title, contrasts_tb[title])
