library('agilp')


inputdir <- "/srv/home/rgarcia/microarreglos/nrp1_nrp2/"
raw_dir <- "/srv/home/rgarcia/microarreglos/nrp1_nrp2/raw/"

# extract red and green median expression data
AAProcess(input = inputdir, output = raw_dir, s = 9)

# create baseline
baselinefile <- "/srv/home/rgarcia/microarreglos/nrp1_nrp2/out/baseline.txt"
Baseline(NORM="LOG", allfiles=TRUE, input=raw_dir, baseout=outbase)

# normalize
outputdir <- "/srv/home/rgarcia/microarreglos/nrp1_nrp2/out/"
AALoess(input=raw_dir, output=outputdir, baseline = baselinefile, LOG="TRUE")
