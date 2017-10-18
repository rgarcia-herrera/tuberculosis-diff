import csv
from os import path


ann={}
for n in [0, 1, 2, 3, 5, 6, 7, 8, 9, 10]:
    with open(path.join(path.dirname(path.realpath(__file__)),
                        "%s.txt" % n), 'r') as f:
        r = csv.reader(f, delimiter="\t")
        for row in r:
            ann[row[0]] = row

            synonyms = [syn.replace("<I>", "").replace("</I>", "")
                        for syn in row[1].split(', ')]
            for syn in synonyms:
                ann[syn] = row

            ann[row[2]] = row
