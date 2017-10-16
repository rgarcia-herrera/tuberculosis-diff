library(limma)

targets <- readTargets("targets.txt")

x <- read.maimages(targets, path="somedirectory", source="agilent",green.only=TRUE)

y <- backgroundCorrect(x, method="normexp", offset=16)

y <- normalizeBetweenArrays(y, method="quantile")

y.ave <- avereps(y, ID=y$genes$ProbeName)


f <- factor(targets$Condition, levels = unique(targets$Condition))
design <- model.matrix(~0 + f)
colnames(design) <- levels(f)

fit <- lmFit(y.ave, design)

contrast.matrix <- makeContrasts("Treatment1-Treatment2", "Treatment1-Treatment3", "Treatment2-Treatment1", levels=design)

fit2 <- contrasts.fit(fit, contrast.matrix)
fit2 <- eBayes(fit2)


output <- topTable(fit2, adjust="BH", coef="Treatment1-Treatment2", genelist=y.ave$genes, number=Inf)
write.table(output, file="Treatment1_vs_Treatment.txt", sep="\t", quote=FALSE)