import argparse
import csv
import gene_probes

parser = argparse.ArgumentParser(
        description='split into macrophage and tb')
parser.add_argument('exp', type=argparse.FileType('r'),
                    help='Normalized, batch-averaged expression TSV file.')
args = parser.parse_args()


macrophage_path = args.exp.name.replace('.txt', '_macrophage.tsv')
tb_path = args.exp.name.replace('.txt', '_tb.tsv')


reader = csv.reader(args.exp, delimiter=' ')


with open(macrophage_path, 'w') as m, open(tb_path, 'w') as t:
    mw = csv.writer(m)
    tw = csv.writer(t)

    for row in reader:
        if row[0] in gene_probes.macrophage:
            mw.writerow([gene_probes.macrophage[row[0]],
                         row[1]])
        elif row[0] in gene_probes.tb:
            tw.writerow([gene_probes.tb[row[0]],
                         row[1]])
        else:
            print row
