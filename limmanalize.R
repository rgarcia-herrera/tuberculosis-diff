library(limma)

targets <- readTargets("targets.txt")

x <- read.maimages(targets, source="agilent", green.only=TRUE)

y <- backgroundCorrect(x, method="normexp", offset=16)

y <- normalizeBetweenArrays(y, method="quantile")

y.ave <- avereps(y, ID=y$genes$ProbeName)


f <- factor(targets$Condition, levels = unique(targets$Condition))
design <- model.matrix(~0 + f)
colnames(design) <- levels(f)

fit <- lmFit(y.ave, design)

contrasts <- c("nrp1_24-nrp1_48",
               "nrp1_24-nrp2_24",
               "nrp1_48-nrp2_48",
               "nrp2_24-nrp2_48")

for (contrast in contrasts) {

    contrast.matrix <- makeContrasts(contrast, levels=design)

    fit2 <- contrasts.fit(fit, contrast.matrix)
    fit2 <- eBayes(fit2)

    output <- topTable(fit2, adjust="BH", coef=contrast, genelist=y.ave$genes, number=Inf)
    write.table(output, file=paste("data/contrasts/", contrast, ".txt", sep=""), sep="\t", quote=FALSE)

    ## results <- decideTests(fit2)
    ## summary(results)
    ## vennDiagram(results)
    ## plotMA(fit2, 2)
    ## volcanoplot(fit2)
}
