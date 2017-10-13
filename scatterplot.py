import csv
from pprint import pprint
import matplotlib.pyplot as plt
from itertools import combinations

normalized=[
    '/srv/home/rgarcia/tuberculosis-nrp/data/nrp1_nrp2/norm/ng_nrp1_24h_l1.txt',
    '/srv/home/rgarcia/tuberculosis-nrp/data/nrp1_nrp2/norm/ng_nrp1_24h_l2.txt',
    '/srv/home/rgarcia/tuberculosis-nrp/data/nrp1_nrp2/norm/ng_nrp1_48h_l1.txt',
    '/srv/home/rgarcia/tuberculosis-nrp/data/nrp1_nrp2/norm/ng_nrp1_48h_l2.txt',
    '/srv/home/rgarcia/tuberculosis-nrp/data/nrp1_nrp2/norm/ng_nrp2_24h_l1.txt',
    '/srv/home/rgarcia/tuberculosis-nrp/data/nrp1_nrp2/norm/ng_nrp2_24h_l2.txt',
    '/srv/home/rgarcia/tuberculosis-nrp/data/nrp1_nrp2/norm/ng_nrp2_48h_l1.txt',
    '/srv/home/rgarcia/tuberculosis-nrp/data/nrp1_nrp2/norm/ng_nrp2_48h_l2.txt',
]

A = {}
probes = set()

for path in normalized:
    with open(path) as f:
        r = csv.reader(f, delimiter='\t')
        sample = r.next().pop()
        A[sample] = {}
        for row in r:
            (probe, intensity) = row
            probes.add(probe)
            A[sample][probe] = float(intensity)

probes = list(probes)


for pair in combinations(A.keys(), 2):
    x = [A[pair[0]][probe] for probe in probes]
    y = [A[pair[1]][probe] for probe in probes]
    plt.scatter(x, y)
    plt.title("intensities")
    plt.xlabel(pair[0])
    plt.ylabel(pair[1])
    plt.savefig("plots/%s_%s.png" % pair)
