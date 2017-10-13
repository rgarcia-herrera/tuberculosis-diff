library('agilp')


inputdir <- "/srv/home/rgarcia/microarreglos/nrp1_nrp2/"
avg_dir <- "/srv/home/rgarcia/microarreglos/nrp1_nrp2/avg/"

# extract red and green median expression data
AAProcess(input = inputdir, output = avg_dir, s = 9)

# create baseline
baselinefile <- "/srv/home/rgarcia/microarreglos/nrp1_nrp2/norm/baseline.txt"
Baseline(NORM="LOG", allfiles=TRUE, input=avg_dir, baseout=baselinefile)

# normalize
normdir <- "/srv/home/rgarcia/microarreglos/nrp1_nrp2/norm/"
AALoess(input=avg_dir, output=normdir, baseline = baselinefile, LOG="TRUE")
