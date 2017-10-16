library(limma)


targets <- readTargets("targets.txt")
RG <- read.maimages(targets, source="agilent",  green.only=TRUE)

RG <- backgroundCorrect(RG, method="normexp", offset=1)
plotDensities(RG)
MA <- normalizeBetweenArrays(RG, method="quantile")
plotDensities(MA)


# make the design matrix
d.levels = unique(targets$Condition)
d.factor = factor(targets$Condition, levels=d.levels)
d.design = model.matrix(~0 + d.factor)
colnames(d.design) = levels(d.factor)

contrast.matrix <- makeContrasts("nrp1_24", "nrp1_48", levels=d.design)

## fit <- lmFit(MA)
## fit <- eBayes(fit)
