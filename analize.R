library('agilp')



normalize <- function(base_dir, data_dir) {
    data_dir <- file.path(base_dir, "data", "", fsep = "/")
    avg_dir <- file.path(base_dir, "avg", "", fsep = "/")
    norm_dir <- file.path(base_dir, "norm", "", fsep = "/")
    dir.create(avg_dir)
    dir.create(norm_dir)

    ## extract green median expression data
    AAProcess(input = data_dir, output = avg_dir, s = 9)

    # create baseline
    baseline_file <- file.path(norm_dir, "baseline.txt", fsep = "/")
    Baseline(input=avg_dir, baseout=baseline_file)

    # normalize
    AALoess(input=avg_dir, output=norm_dir, baseline=baseline_file, LOG=TRUE)
}


normalize("/srv/home/rgarcia/tuberculosis-nrp/data/log_ctrl_lavado0")
normalize("/srv/home/rgarcia/tuberculosis-nrp/data/log_ctrl_lavado1")
normalize("/srv/home/rgarcia/tuberculosis-nrp/data/log_ctrl_lavado2")
normalize("/srv/home/rgarcia/tuberculosis-nrp/data/nrp1_nrp2")
