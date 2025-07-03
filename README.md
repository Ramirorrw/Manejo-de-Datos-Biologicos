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

!(Frecuencia_LPU83_WT.png)

!(Frecuencia_LPU83_0308.png)

!(Frecuencia_LPU83_1066.png)

!(Frecuencia_LPU83_1088.png)

!(Frecuencia_LPU83_1729.png)

A partir de estas imagenes creo estar seguro de que los datos del grupo LPU83_WT tengan una distribución normal, y que los grupos LPU83_1088 y LPU83_1729 no tengan una distribución normal; mientras que los datos de los grupos LPU83_0308 y LPU83_1066 no estan claros. Independientemente de mi interpretación, más adelante en este trabajo se realizó un test para evaluar la normalidad de la distribuicion de los datos (se aplicó el test de Pearson).

Seguido a esto, se procedió con el cálculo de ciertos parámetros como la media, mediana, moda, RI (percentil 25 - 75%), Desviación Típica y Varianza. Los resultados obtenidos se pueden observar en la siguiente tabla:
```python
 Tratamiento         Media      Mediana                  Moda            RI  Desviación típica      Varianza
0    LPU83_WT  5.867778e+07   57900000.0   [75200000.00000022]  2.422500e+07       1.950652e+07  3.805042e+14
1  LPU83_0308  2.006556e+08   93600000.0   [28700000.00000004]  2.550250e+08       2.205973e+08  4.866319e+16
2  LPU83_1066  4.346667e+08  416000000.0  [115000000.00000027]  3.357500e+08       2.314527e+08  5.357035e+16
3  LPU83_1088  2.957889e+07   19900000.0  [3980000.0000000033]  4.659500e+07       2.420043e+07  5.856606e+14
4  LPU83_1729  2.435778e+07   11220000.0  [1350000.0000000026]  3.102000e+07       2.736516e+07  7.488520e+14
```

A continuación se hizo un análsisi de asimetría y un análisis de Curtósis. El analsisi de asimetría nos permitirá determianr si la frecuencia de los datos al rededor de la media estan distribuidos de manera equidistante de un lado y otro, o de manera asimétrica. Para ello se utiliza el coeficiente de fisher. Valores negativos indica que la variable toma más valores hacia la izquierda de la media (asimetría negativa), un valor 0 indica simetría perfecta y valores positivos indica que la variable toma con mayor frecuencia valores a la derecha de la media (asimetría positiva). Por otro lado el coeficiente de Curtosis nos indica como esos datos estan agrupados al rededor de la media. Valores negativos indican un agrupamiento tipo platicúrtica (una forma mas aplanada), valor 0 indica un tipo mesocúrtica (correspondiente a una perfecta campana de Gaus), y valores positivo indican un agrupamiento tipo leptocúrtica (una forma mas puntiaguda alrededor de la media). El resultado de ambos test lo vemos en la siguiente tabla:

Tratamiento   Asimetría Fisher    Curtosis
0    LPU83_WT   -0.636196         0.123657
1  LPU83_0308    1.088271        -0.187134
2  LPU83_1066    0.361716        -0.745575
3  LPU83_1088    0.304704        -1.820472
4  LPU83_1729    1.422748         1.198298

Vemos que LPU83_0308 y LPU83_1729 presentan una clara asimetría positiva, mientras que LPU83_1066 y LPU83_1088 presentan una leve asimetría positiva. En el caso de LPU83_WT presenta una asimetría leve hacia la izquierda (negativa). El test de curtosis muestra una forma clarametne leptocúrtica para la distribucion de datos en LPU83_1729, una forma claramente platicúrtica para LPU83_1088. En los casos de LPU83_0308 y LPU83_1066, presentan una leve forma platicúrtica, mientras que LPU83_WT presenta una forma levemente leptocúrtica.

Luego, se ha realizado un analisis de intervalo de confianza 95% (IC 95%). Este analsisi nos permite decir con un 95% de confianza que la media debe encotrarse comprendida dentro de tal rango de valores. Este analisis brindó lo siguientes resultados:

  Tratamiento         Media  IC 95% Inferior  IC 95% Superior
0    LPU83_WT  5.867778e+07     4.897742e+07     6.837814e+07
1  LPU83_0308  2.006556e+08     9.095508e+07     3.103560e+08
2  LPU83_1066  4.346667e+08     3.195679e+08     5.497654e+08
3  LPU83_1088  2.957889e+07     1.754430e+07     4.161348e+07
4  LPU83_1729  2.435778e+07     1.074940e+07     3.796615e+07

Con el fin de determinar si luego podemos analizar los datos de manera paramétrica o no paramétricamente, se realizo un contraste de hipótesis. En esta seccion se analizo si la distribucion de los datos para cada caso siguen una distribución normal, y si sus varianzas son o no muy diferentes entre sí (homocedasticidad o heterocedasticidad, respectivamente). 

Para el analsis de la normalidad se realizó el test de normalidad (normal test en python). En este caso se deben plantear las siguientes dos hipótesis:
H0 = los datos se distribuyen normlamente
H1 = los datos no se distribuyen normalmente.
Si el p-value del test es >0.05 entocnes H0 será aceptada y H1 rechazada. En caso que p-value < 0.05, H0 sera rechazada y H1 aceptada.

Para el analsisi de varianza (homocedasticidad o heterocedasticidad) se aplicó el test de Levene. Para este también se plantean dos hipótesis:
H0 = las varianzadas son similares
H1 = las varianzan son significativamente diferentes
Si el p-value del test es >0.05 entocnes H0 será aceptada y H1 rechazada. En caso que p-value < 0.05, H0 sera rechazada y H1 aceptada.

Los resultados para tales test se resumen en la siguiente tabla:
