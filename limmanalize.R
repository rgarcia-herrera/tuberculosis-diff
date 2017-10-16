library(limma)

targets <- readTargets("targets.txt")

x <- read.maimages(targets, source="agilent", green.only=TRUE)

y <- backgroundCorrect(x, method="normexp", offset=16)


png('lplots/pre-norm.png', width=14, height=14, units = 'cm', res=300)
plotDensities(y, legend=FALSE,
              col=c('grey10', 'grey20', 'grey30', 'grey40', 'grey50', 'grey60', 'grey70', 'grey80'))
dev.off()


y <- normalizeBetweenArrays(y, method="quantile")

png('lplots/normalized.png', width=14, height=14, units = 'cm', res=300)
plotDensities(y, legend=FALSE,
              col=c('grey10', 'grey20', 'grey30', 'grey40', 'grey50', 'grey60', 'grey70', 'grey80'))
dev.off()

y.ave <- avereps(y, ID=y$genes$ProbeName)

# create design
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

    results <- decideTests(fit2)

    png(paste("lplots/ma_", contrast, ".png", sep=""),
        width=14, height=14, units = 'cm', res=300)
    plotMA(fit2, 1)
    dev.off()

    png(paste("lplots/volcano_", contrast, ".png", sep=""),
        width=14, height=14, units = 'cm', res=300)
    volcanoplot(fit2, names=fit2$genes, main=contrast)
    dev.off()

}
