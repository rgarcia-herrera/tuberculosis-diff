import numpy as np
from slugify import slugify
from pprint import pprint


from design import contrasts_tb, contrasts_macrophage


def delta(title, pair):
    genes = np.genfromtxt(pair[0]['path'], delimiter=',', usecols=(0,), dtype=str)
    x = np.genfromtxt(pair[0]['path'], delimiter=',', usecols=(1,))
    y = np.genfromtxt(pair[1]['path'], delimiter=',', usecols=(1,))

    return np.stack([genes, (x - y)], axis=-1)


for title in contrasts_macrophage:
    np.savetxt("data/deltas/%s.tsv" % slugify(title),
               delta(title, contrasts_macrophage[title]),
               fmt='%s')

for title in contrasts_tb:
    np.savetxt("data/deltas/%s.tsv" % slugify(title),
               delta(title, contrasts_tb[title]),
               fmt='%s')
