import argparse
import csv
import functional_categories as fc
import gene_probes as gp

parser = argparse.ArgumentParser(
        description='add annotations to intensities file')
parser.add_argument('exp', type=argparse.FileType('r'),
                    help='intensity file as output from agilp')
args = parser.parse_args()

reader = csv.reader(args.exp, delimiter='\t')
w = csv.writer(open(args.exp.name.replace('.txt', '_ann.csv'), 'w'), delimiter="|")

header = ['probe', 'intensity', ''] + fc.ann_header
w.writerow(header)

for row in reader:

    symbol = gp.macrophage.get(row[0],
                               gp.tb.get(row[0],
                                         gp.controls.get(row[0],
                                                         row[0])))
    if symbol in fc.M:
        row.append('macrophage')
    else:
        row.append('')

    row += fc.ann.get(symbol, [])

    w.writerow(row)
