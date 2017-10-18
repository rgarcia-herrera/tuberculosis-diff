import argparse
import csv
import functional_categories as fc

parser = argparse.ArgumentParser(
        description='split into macrophage and tb, annotate')
parser.add_argument('exp', type=argparse.FileType('r'),
                    help='limma TopTable output as CSV file')
parser.add_argument('out', type=argparse.FileType('w'),
                    help='output path')
args = parser.parse_args()

reader = csv.reader(args.exp, delimiter='\t')
w = csv.writer(args.out)

for row in reader:

    SystematicName = row[5]
    if SystematicName in fc.M:  #
        row += ['macrophage', ]
    else:
        row += ['TB', ]

    row += fc.ann.get(SystematicName,
                      [])

    w.writerow(row)
