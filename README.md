# Manejo-de-Datos-Biologicos

Marco teórico:
Para este trabajo final de la materia “Manejo de datos en biología computacional. Herramientas de estadística” he propuesto estudiar el sistema biológico el cual me encuentro estudiando en el marco de mi doctorado. Este sistema es la bacteria Rizhobium favelukesii LPU83. R. favelkesii es una alfa proteo-bacteria capaz de llevar a cabo un proceso de simbiosis con su par simbionte Alfalfa (donde se produce un nuevo órgano denominado nódulo) y capaz de sobrevivir a pH ácidos moderados (pH 4.6). Estas características lo hacen un interesante objeto de estudio de los mecanismos de tolerancia a la acidez. Dado esto, es que en nuestro laboratorio se hicieron estudios transcriptómicos (RNA-seq) y proteómicos de R. favelukesii en condiciones de acidez. A partir de estos ensayos se filtraron aquellos genes diferencialmente expresados en condiciones de pH ácido (pH4.6) respecto de pH neutro (pH7) y se seleccionaron los siguientes genes: LPU83_0308, LPU83_1066, LPU83_1088 y LPU83_1729. Dichos genes fueron interrumpidos por simple inserción de vector, generando así cepas mutantes donde el correcto plegamiento de los productos de dichos genes se ve afectado y, por ende, también su funcionalidad. Estos mutantes fueron sometidos a diferentes ensayos. Entre ellos, el que se presentará en este trabajo: estudiar recuento de viables obtenidos a partir de nodulos. Este ensayo nos permitirá poder profundizar sobre el estudio de estos genes y su importancia, en este caso, para la proliferación o no, de las bacterias dentro de los nódulos.

Descripción del ensayo:
Para este ensayo, 18 plantas fueron inoculadas con una misma cantidad de bacterias vivas, y crecidas en las mismas condiciones. Las cepas utilizadas fueron LPU83_WT, que funcionó como control positivo, y los cuatro mutantes generados LPU83_0308, LPU83_1066, LPU83_1088 y LPU83_1729, como cepas a evaluar. Pasados los 45 días post inoculación, se cortaron y pesaron el total de nódulos por planta. Dichos nodulos fueron esterilizados superficialmente, y triturados en solución fisiológica para extraer todas las bacterias internas. Luego dichas extraciones fueron diluidas en forma seriada, y de cada dilucion se colocaron 10 gotas de 10ults en placa con medio de cultivo para hacer los recuentos de viables.

De esta manera entonces se obtiene una tabla con dos entradas:
hoja1 = Supervivencia_(ufc_mg_nodulos)
hoja2 = peso_nódulos_mg_planta

Se trabajo sobre la hoja1 para los analisis en este trabajo.

Primero se graficó la distribucion de las frecuencias de las medidas para cada grupo (LPU83_WT, LPU83_0308, LPU83_1066, LPU83_1088 y LPU83_1729).
Tales graficos se presentan en los archivos:

!Frecuencia_LPU83_WT.png
!Frecuencia_LPU83_0308.png)
!Frecuencia_LPU83_1066.png)
!Frecuencia_LPU83_1088.png)
!Frecuencia_LPU83_1729.png)


