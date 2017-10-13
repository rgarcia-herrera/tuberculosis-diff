# Tuberculosis-NRP


Timeseries, gene expression, time series.


# Datos

1. Carpeta txt Log Glu y ctrls 2 lavado. De las tres carpetas log Glu
y ctrls esta es con la que debemos comenzar. Ddentro de cada carpeta
hay dos de cada archivo que terminan en L1 o L2... esto quiere decir
que son dos réplicas biológicas de cada experimento, con excepción de
los controles que están formados por una mezcla de RNAs de diferentes
experimentos. De esta forma en esta carpeta tenemos:

a) CTLR 4 h- este es el experimento de células sin infectar...o sea
que solo tiene rna de macrófagos. 4 horas es el primer tiempo en todos
los experimentos.

b) CTRL 24h y CTRL 48h- son los experimentos de los siguientes
tiempos... otra vez son células sin infectar... unicamente RNA de
macrófagos

c) Despues vienen los archivos de las condiciones de infección que son
LOG (de fase logarítmica de crecimiento) en experimentos de 24 y 48h
con dos y tres replicas biológicas, respectivamente. En estos
experimentos hay RNA tanto del macrófago como de M. tuberculosis.  No
tenemos la fase de 4h en los areglos porque ese RNA bacteriano no
estaba listo.

OK entoces de este arreglo solo hay que analizar la expresión de los
experimentos de 24h y de 48h

2. Carpeta txt NRP1 y NRP2- las NRP son las fases de latencia in
vitro de tb. La fase 1 es de hipoxia (baja tensión de o2) y la fase
2 es de anoxia (sin o2). Y así para cada fase de latencia tenemos dos
archivos del exp de 24 h y dos del de 48 porque son dos replicas
biológicas.


# Análisis

1. Tenemos que analizar las fases LOG contra el primer tiempo qe
tenemos que es el de 24h...o sea que tenemos que saber que diferencias
hay entre el exprimento de 48h glucosa respecto al experimento de 24 h

2. Con las fases NRP es lo mismo... primero teemos que saber que
diferencias hasy entre NRP1 48h respecto a NRP1 24h y lo mismo para
NRP2....

Lo importante es comparar cada lote con su igual... osea los LOG 48h
L1 con LOG 24L1 y asi los L2.... Lo mismo para los NRP.

3. En el caso de NRP tamnien hay que comparar entre las fases y el
mismo tiempo... es decir NRP2 24H contra el mismo lote de NRP1 24h y
asi NRP2 48h contra NRP1 48h.

4. Finalmente tendriamos que saber que onda con NRP1 24h contra LOG
24h y asi con 48h y lo mism para NRP2 24h contra GLU 24h y lo mismo
para 48h

Creo que si reportamos los analisis entre fases estaría ideal... o sea
el análisis 4. De ahi los análisis 1-3 tienen la misma importancia

<img src="design.png">

--------

http://master.bioconductor.org/help/workflows/arrays/

http://master.bioconductor.org/help/course-materials/

http://bioconductor.org/packages/2.5/bioc/html/limma.html

https://support.bioconductor.org/p/31224/
