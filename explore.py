import csv
from pprint import pprint
import matplotlib.pyplot as plt
from itertools import combinations

raws=['/srv/home/rgarcia/microarreglos/nrp1_nrp2/raw/gRaw_NRP1_24H_L1.txt',
      '/srv/home/rgarcia/microarreglos/nrp1_nrp2/raw/gRaw_NRP1_24H_L2.txt',
      '/srv/home/rgarcia/microarreglos/nrp1_nrp2/raw/gRaw_NRP1_48H_L1.txt',
      '/srv/home/rgarcia/microarreglos/nrp1_nrp2/raw/gRaw_NRP1_48H_L2.txt',
      '/srv/home/rgarcia/microarreglos/nrp1_nrp2/raw/gRaw_NRP2_24H_L1.txt',
      '/srv/home/rgarcia/microarreglos/nrp1_nrp2/raw/gRaw_NRP2_24H_L2.txt',
      '/srv/home/rgarcia/microarreglos/nrp1_nrp2/raw/gRaw_NRP2_48H_L1.txt',
      '/srv/home/rgarcia/microarreglos/nrp1_nrp2/raw/gRaw_NRP2_48H_L2.txt']

aaloess=[
    '/srv/home/rgarcia/microarreglos/nrp1_nrp2/out/ng_NRP1_24H_L1.txt',
    '/srv/home/rgarcia/microarreglos/nrp1_nrp2/out/ng_NRP1_24H_L2.txt',
    '/srv/home/rgarcia/microarreglos/nrp1_nrp2/out/ng_NRP1_48H_L1.txt',
    '/srv/home/rgarcia/microarreglos/nrp1_nrp2/out/ng_NRP1_48H_L2.txt',
    '/srv/home/rgarcia/microarreglos/nrp1_nrp2/out/ng_NRP2_24H_L1.txt',
    '/srv/home/rgarcia/microarreglos/nrp1_nrp2/out/ng_NRP2_24H_L2.txt',
    '/srv/home/rgarcia/microarreglos/nrp1_nrp2/out/ng_NRP2_48H_L1.txt',
    '/srv/home/rgarcia/microarreglos/nrp1_nrp2/out/ng_NRP2_48H_L2.txt']


A = {}
probes = set()

for path in aaloess:
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
    plt.title("raw intensities")
    plt.xlabel(pair[0].replace("gRaw_", "").replace("_", " ").replace(".txt", ""))
    plt.ylabel(pair[1].replace("gRaw_", "").replace("_", " ").replace(".txt", ""))
    plt.savefig("%s_%s.png" % pair)
