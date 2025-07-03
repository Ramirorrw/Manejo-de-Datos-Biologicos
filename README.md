# Manejo-de-Datos-Biologicos
#
Marco teórico:


Para este trabajo final de la materia “Manejo de datos en biología computacional. Herramientas de estadística” he propuesto estudiar el sistema biológico el cual me encuentro estudiando en el marco de mi doctorado. Este sistema es la bacteria Rizhobium favelukesii LPU83. R. favelkesii es una alfa proteo-bacteria capaz de llevar a cabo un proceso de simbiosis con su par simbionte Alfalfa (donde se produce un nuevo órgano denominado nódulo) y capaz de sobrevivir a pH ácidos moderados (pH 4.6). Estas características lo hacen un interesante objeto de estudio de los mecanismos de tolerancia a la acidez. Dado esto, es que en nuestro laboratorio se hicieron estudios transcriptómicos (RNA-seq) y proteómicos de R. favelukesii en condiciones de acidez. A partir de estos ensayos se filtraron aquellos genes diferencialmente expresados en condiciones de pH ácido (pH4.6) respecto de pH neutro (pH7) y se seleccionaron los siguientes genes: LPU83_0308, LPU83_1066, LPU83_1088 y LPU83_1729. Dichos genes fueron interrumpidos por simple inserción de vector, generando así cepas mutantes donde el correcto plegamiento de los productos de dichos genes se ve afectado y, por ende, también su funcionalidad. Estos mutantes fueron sometidos a diferentes ensayos. Entre ellos, el que se presentará en este trabajo: estudiar recuento de viables obtenidos a partir de nodulos. Este ensayo nos permitirá poder profundizar sobre el estudio de estos genes y su importancia, en este caso, para la proliferación o no, de las bacterias dentro de los nódulos.
#
Descripción del ensayo:


Para este ensayo, 18 plantas fueron inoculadas con una misma cantidad de bacterias vivas, y crecidas en las mismas condiciones. Las cepas utilizadas fueron LPU83_WT, que funcionó como control positivo, y los cuatro mutantes generados LPU83_0308, LPU83_1066, LPU83_1088 y LPU83_1729, como cepas a evaluar. Pasados los 45 días post inoculación, se cortaron y pesaron el total de nódulos por planta. Dichos nodulos fueron esterilizados superficialmente, y triturados en solución fisiológica para extraer todas las bacterias internas. Luego dichas extraciones fueron diluidas en forma seriada, y de cada dilucion se colocaron 10 gotas de 10ults en placa con medio de cultivo para hacer los recuentos de viables.
#
De esta manera entonces se obtiene una tabla:


variable = Supervivencia_(ufc_mg_nodulos)


Primero se graficó la distribucion de las frecuencias de las medidas para cada grupo (LPU83_WT, LPU83_0308, LPU83_1066, LPU83_1088 y LPU83_1729).
Tales graficos se presentan en los archivos:

![Frecuencia_LPU83_WT](https://github.com/user-attachments/assets/1f54d88b-61a4-4d29-b035-39c61bb1444d)
![Frecuencia_LPU83_0308](https://github.com/user-attachments/assets/04f2deec-946c-40e2-8c03-bd0e68270d0c)
![Frecuencia_LPU83_1066](https://github.com/user-attachments/assets/01c14fac-2133-45ec-a092-8f915b352d8f)
![Frecuencia_LPU83_1088](https://github.com/user-attachments/assets/3e9c4a55-f451-4cf3-a984-b9c0c309510a)
![Frecuencia_LPU83_1729](https://github.com/user-attachments/assets/7b926ab0-d37b-48fd-87a9-9118a69b58a3)


####
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
######
A continuación se hizo un análsisi de asimetría y un análisis de Curtósis. El analsisi de asimetría nos permitirá determianr si la frecuencia de los datos al rededor de la media estan distribuidos de manera equidistante de un lado y otro, o de manera asimétrica. Para ello se utiliza el coeficiente de fisher. Valores negativos indica que la variable toma más valores hacia la izquierda de la media (asimetría negativa), un valor 0 indica simetría perfecta y valores positivos indica que la variable toma con mayor frecuencia valores a la derecha de la media (asimetría positiva). Por otro lado el coeficiente de Curtosis nos indica como esos datos estan agrupados al rededor de la media. Valores negativos indican un agrupamiento tipo platicúrtica (una forma mas aplanada), valor 0 indica un tipo mesocúrtica (correspondiente a una perfecta campana de Gaus), y valores positivo indican un agrupamiento tipo leptocúrtica (una forma mas puntiaguda alrededor de la media). El resultado de ambos test lo vemos en la siguiente tabla:

```python
Tratamiento   Asimetría Fisher    Curtosis
0    LPU83_WT   -0.636196         0.123657
1  LPU83_0308    1.088271        -0.187134
2  LPU83_1066    0.361716        -0.745575
3  LPU83_1088    0.304704        -1.820472
4  LPU83_1729    1.422748         1.198298
```

Vemos que LPU83_0308 y LPU83_1729 presentan una clara asimetría positiva, mientras que LPU83_1066 y LPU83_1088 presentan una leve asimetría positiva. En el caso de LPU83_WT presenta una asimetría leve hacia la izquierda (negativa). El test de curtosis muestra una forma clarametne leptocúrtica para la distribucion de datos en LPU83_1729, una forma claramente platicúrtica para LPU83_1088. En los casos de LPU83_0308 y LPU83_1066, presentan una leve forma platicúrtica, mientras que LPU83_WT presenta una forma levemente leptocúrtica.
######
Luego, se ha realizado un analisis de intervalo de confianza 95% (IC 95%). Este analsisi nos permite decir con un 95% de confianza que la media debe encotrarse comprendida dentro de tal rango de valores. Este analisis brindó lo siguientes resultados:

```python
  Tratamiento         Media  IC 95% Inferior  IC 95% Superior
0    LPU83_WT  5.867778e+07     4.897742e+07     6.837814e+07
1  LPU83_0308  2.006556e+08     9.095508e+07     3.103560e+08
2  LPU83_1066  4.346667e+08     3.195679e+08     5.497654e+08
3  LPU83_1088  2.957889e+07     1.754430e+07     4.161348e+07
4  LPU83_1729  2.435778e+07     1.074940e+07     3.796615e+07
```
######
A continuación se realizo un analsis de tamaño de muestra:


Este ensayo nos permite determinar la cantidad de muestras mínimas que debemos analizar para que nuestros análisis, con las distribuciones y valores de media, varianza, etc, tengan validez. Para este item del trabajo, solo calculé el tamaño de mmuestra miníma necesaria para la comparación LPU83_WT vs LPU83_1066 dado que intuí una posible diferencia significativa. Igualmente el analisis de diferencia signifivativa, lo realicé más adelante luego de analizar otros parámetros necesarios.
```python
LPU83_WT vs LPU83_1066:
Tamaño de muestra recomendado: 5.0 muestras por grupo.
```
######
Con el fin de determinar si luego podemos analizar los datos de manera paramétrica o no paramétricamente, se realizo un contraste de hipótesis. En esta seccion se analizo si la distribucion de los datos para cada caso siguen una distribución normal, y si sus varianzas son o no muy diferentes entre sí (homocedasticidad o heterocedasticidad, respectivamente). 

Para el analsis de la normalidad se realizó el test de normalidad (normal test en python). En este caso se deben plantear las siguientes dos hipótesis:
```python
H0 = los datos se distribuyen normlamente.
H1 = los datos no se distribuyen normalmente.
```
Si el p-value del test es >0.05 entocnes H0 será aceptada y H1 rechazada. En caso que p-value < 0.05, H0 sera rechazada y H1 aceptada.

Para el analsisi de varianza (homocedasticidad o heterocedasticidad) se aplicó el test de Levene. Para este también se plantean dos hipótesis:
```python
H0 = las varianzadas son similares.
H1 = las varianzan son significativamente diferentes.
```
Si el p-value del test es >0.05 entocnes H0 será aceptada y H1 rechazada. En caso que p-value < 0.05, H0 sera rechazada y H1 aceptada.

Los resultados para tales test se resumen a continuación:
```python
Test de Normalidad

Tratamiento: LPU83_WT
  Estadístico = 1.62
  p-valor = 0.4439
 Se acepta H0: Se asume distribución normal.

Tratamiento: LPU83_0308
  Estadístico = 3.98
  p-valor = 0.1366
 Se acepta H0: Se asume distribución normal.

Tratamiento: LPU83_1066
  Estadístico = 1.03
  p-valor = 0.5979
 Se acepta H0: Se asume distribución normal.

Tratamiento: LPU83_1088
  Estadístico = 12.30
  p-valor = 0.0021
 Se rechaza H0: No sigue distribución normal.

Tratamiento: LPU83_1729
  Estadístico = 7.73
  p-valor = 0.0210
 Se rechaza H0: No sigue distribución normal.
```
```python
Test de Levene para homocedasticidad

Estadístico = 15.99
p-valor = 0.0000
 Se rechaza H0: Hay evidencia de heterocedasticidad (varianzas diferentes).
 ```
Podemos ver que los datos en LPU83_1088 y LPU83_1729 no siguen una distribucion normal, y que no hay homocedasticidad en la varianza entres los tratamientos. Por ende para poder evaluar si hay diferencia significativa en el recuento de viables de las cepas mutantes respecto de la cepa salvaje (LPU83_WT), se debera hacer un analisis no-paramétrico. Dado que nuestro n < 30 y queremos comparar de a pares relizamos dos test independientes para ver si hay o no concordancia entre ellos. Los test a relizar son: Welch y Mann-Whitney.
```python
Comparación               Mann-Whitney U    p-valor MW    t de Welch    p-valor Welch
LPU83_WT vs LPU83_0308        122.0        2.113414e-01   -2.719976       0.014412
LPU83_WT vs LPU83_1066         0.0         3.222224e-07   -6.867712       0.000003
LPU83_WT vs LPU83_1088        262.5        1.554740e-03    3.971797       0.000371
LPU83_WT vs LPU83_1729        274.5        3.941362e-04    4.332794       0.000146
```
Podemos concluir a partir de estos analisis, que la unica cepa que no presenta diferencia significativa respecto la cepa salvaje es LPU83_0308. Mientras que el resto de las cepas si lo hacen.

#####
Por ultimo se hizo un analisis de correlacion de variables:


Dado que estamos fente a una situacion no paramétrica, con variables numericas, se utilizó el test de Spearman. Este test nos permitirá evaluar si existe o no una relacion entre dos variables. El resultado del mismo nos arrojará un coeficient rho (-1 < rho < 1) y un p-value. Un coeficiente -1 indica una correlación negativa perfecta, 0 indica ausencia de correlación, y 1 indica una correlación positiva perfecta. Y solo será significativo si el p-value < 0.05.

 ```python
variable_1 = "supervivencia bacteriana / mg de nodulo por planta"
variable_2 = "mg total de nodulo por planta"

  Cepa        Coeficiente rho (Spearman)   p-valor
LPU83_WT               0.395661            0.104107
LPU83_0308             0.203407            0.418201
LPU83_1066             0.183884            0.465139
LPU83_1088             0.106405            0.674321
LPU83_1729             -0.377457           0.122535
```
Como resultado no hay una correlacion entre las variables.
#####
A modo de conclusión de este trabajo, podemos decir que el mutante LPU83_1066 exibhe un mayor recuento de viables desde nódulo cuando las plantas son inoculadas con la misma cantidad de bacteria y crecidas en las mismas condiciones. Esto no es un resultado que esperabamos ver, dado que el proceso de simbiosis implica, entre otros estreses, un estrés ácido para la bacteria. Con lo cual si nosotros estamos mutando un gen, que por trasncriptómica y proteómica vimos que esta sobre-expresado en acidez, era de esperar un empeoramiento o no-change en la viabilidad de las baceterias dentro del nódulo. Sin embargo, esto es un resultado interesante para seguir ondando y profundizando en su estudio mediante otros ensayos y sus posteriores análisis estadísticos. Por otro lado, respecto al mutante LPU83_0308 podemos decir que no hay diferencias significativas en la viabilidad respecto la cepa salvaje. Y en cuente a los mutantes LPU83_1088 y LPU83_1729, a priori habría una diferencia estadísitica, semejante al caso del mutante LPU83_1066. Pero quedaría realizar el analisis de tamaño de muestra para poder aseguranos que estamos analizando la cantidad mínima de muestras para observar dicha diferencia.
