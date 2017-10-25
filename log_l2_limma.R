library(limma)

targets <- readTargets("log_l2_targets.txt")

x <- read.maimages(targets, source="agilent", green.only=TRUE)

y <- backgroundCorrect(x, method="normexp", offset=16)


png('lplots/log_l2/pre-norm.png', width=14, height=14, units = 'cm', res=300)
plotDensities(y, legend=FALSE,
              col=c('grey10', 'grey20', 'grey30', 'grey40', 'grey50', 'grey60', 'grey70', 'grey80'))
dev.off()


y <- normalizeBetweenArrays(y, method="quantile")

png('lplots/log_l2/normalized.png', width=14, height=14, units = 'cm', res=300)
plotDensities(y, legend=FALSE,
              col=c('grey10', 'grey20', 'grey30', 'grey40', 'grey50', 'grey60', 'grey70', 'grey80'))
dev.off()

y.ave <- avereps(y, ID=y$genes$ProbeName)

# create design
f <- factor(targets$Condition, levels = unique(targets$Condition))
design <- model.matrix(~0 + f)
colnames(design) <- levels(f)

fit <- lmFit(y.ave, design)

contrasts <- c('ctrl_4h-ctrl_24h', 'ctrl_24h-ctrl_48h',
               'ctrl_24h-log_24h',
               'ctrl_48h-log_48h',
               'log_24h-log_48h')

for (contrast in contrasts) {

    contrast.matrix <- makeContrasts(contrast, levels=design)

    fit2 <- contrasts.fit(fit, contrast.matrix)
    fit2 <- eBayes(fit2)

    output <- topTable(fit2, adjust="BH", coef=contrast, genelist=y.ave$genes, number=Inf)
    write.table(output, file=paste("data/log_l2_contrasts/", contrast, ".txt", sep=""), sep="\t", quote=FALSE)

    output <- topTable(fit2, adjust="BH", coef=contrast, genelist=y.ave$genes, number=10)
    write.table(output, file=paste("data/log_l2_contrasts/", contrast, "_top10.txt", sep=""), sep="\t", quote=FALSE)

    results <- decideTests(fit2)

    png(paste("lplots/log_l2/ma_", contrast, ".png", sep=""),
        width=14, height=14, units = 'cm', res=300)
    plotMA(fit2, 1)
    dev.off()

    png(paste("lplots/log_l2/volcano_", contrast, ".png", sep=""),
        width=14, height=14, units = 'cm', res=300)
    volcanoplot(fit2, names=fit2$genes, main=contrast)
    dev.off()

}
