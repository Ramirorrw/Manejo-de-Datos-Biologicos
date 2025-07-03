# Importar librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
import statsmodels.api as sm
import statsmodels.stats.power as smp

# Ruta y hoja
ruta = r"C:\Doctorado TODO\Especializacion_bioinformatica\MANEJO DE DATOS EN BIOLOGÍA COMPUTACIONAL. HERRAMIENTAS DE ESTADÍSTICA (2024)\Trabajo_Final\Supervivencia_sobre_mg_nodulosXplanta.xlsx"
hoja = "Supervivencia_(ufc_mg_nodulos)"

# Leer archivo
supervivencia_nodulos = pd.read_excel(ruta, sheet_name=hoja)

print("Columnas en el archivo:", supervivencia_nodulos.columns.tolist())

# Diccionario para guardar series purgadas
datos_finales = {}
resumen = []

# GRAFICOS DE DISTRIBUCIÓN

for col in supervivencia_nodulos.columns:
    if supervivencia_nodulos[col].dtype in [np.float64, np.int64]:

        print(f"\n=== Variable: {col} ===")

        # Purgar datos en blanco
        supervivencia_final = supervivencia_nodulos[col].dropna()

        # Guardar para usar fuera del for
        datos_finales[col] = supervivencia_final

        # Distribución de frecuencia
        plt.figure(figsize=(8, 5))
        sns.histplot(supervivencia_final, kde=True, bins=10, color="skyblue")
        plt.title(f"{col}")
        plt.xlabel(f"Recuento Bacteriano UFC/mg Nódulo")
        plt.ylabel("Frecuencia")
        plt.grid(True)
        plt.show()

        # Medidas
        media = np.mean(supervivencia_final)
        mediana = np.median(supervivencia_final)
        moda_obj = ss.mode(supervivencia_final, keepdims=False)
        moda = (
            moda_obj.mode.tolist()
            if isinstance(moda_obj.mode, np.ndarray)
            else [moda_obj.mode]
        )
        ri = np.percentile(supervivencia_final, 75) - np.percentile(
            supervivencia_final, 25
        )
        desviacion = np.std(supervivencia_final, ddof=1)
        varianza = np.var(supervivencia_final, ddof=1)

        resumen.append(
            {
                "Tratamiento": col,
                "Media": media,
                "Mediana": mediana,
                "Moda": moda,
                "RI": ri,
                "Desviación típica": desviacion,
                "Varianza": varianza,
            }
        )

# DataFrame resumen
df_resumen = pd.DataFrame(resumen)

print("\n=== Resumen descriptivo general ===")
print(df_resumen)

# ANALISIS DE SIMETRÍA Y KURTOSIS

skew_kurt_resumen = []

for col, serie in datos_finales.items():
    skewness = serie.skew(axis=0, skipna=True, numeric_only=True)
    curtosis = serie.kurt(axis=0, skipna=True, numeric_only=True)

    skew_kurt_resumen.append(
        {"Tratamiento": col, "Asimetría Fisher": skewness, "Curtosis": curtosis}
    )

df_skew_kurt = pd.DataFrame(skew_kurt_resumen)

print("\n=== Resumen de asimetría y curtosis ===")
print(df_skew_kurt)

# INTERVALOS DE CONFIANZA

ic_resumen = []

for col, serie in datos_finales.items():
    n = len(serie)
    media = np.mean(serie)
    sem = ss.sem(serie)
    ci = ss.t.interval(0.95, df=n - 1, loc=media, scale=sem)

    ic_resumen.append(
        {
            "Tratamiento": col,
            "Media": media,
            "IC 95% Inferior": ci[0],
            "IC 95% Superior": ci[1],
        }
    )

df_ic = pd.DataFrame(ic_resumen)

print("\n=== Resumen de intervalos de confianza al 95% ===")
print(df_ic)

# TAMAÑO MUESTRAL

print("\n=== Tamaño de muestra específico para comparaciones significativas ===")


def calcular_effect_size(grupo1, grupo2):
    mean_diff = np.abs(np.mean(grupo1) - np.mean(grupo2))
    pooled_sd = np.sqrt(
        ((np.std(grupo1, ddof=1) ** 2) + (np.std(grupo2, ddof=1) ** 2)) / 2
    )
    d = mean_diff / pooled_sd
    return d


wt = datos_finales["LPU83_WT"]
mut1066 = datos_finales["LPU83_1066"]

effect_size_1066 = calcular_effect_size(wt, mut1066)
n_1066 = smp.tt_ind_solve_power(
    effect_size=effect_size_1066, alpha=0.05, power=0.8, alternative="two-sided"
)

print(f"\nLPU83_WT vs LPU83_1066:")
print(f"  Effect size (d): {effect_size_1066:.2f}")
print(f"  Tamaño de muestra recomendado: {np.ceil(n_1066)} muestras por grupo.")

# TEST DE NORMALIDAD PEARSON

print("\n\nTest de normalidad")

for col, serie in datos_finales.items():
    if len(serie) >= 8:
        stat, p_val = ss.normaltest(serie, axis=0, nan_policy="propagate")
        print(f"\nTratamiento: {col}")
        print(f"  Estadístico = {stat:.2f}")
        print(f"  p-valor = {p_val:.4f}")
        if p_val > 0.05:
            print(" Se acepta H0: Se asume distribución normal.")
        else:
            print(" Se rechaza H0: No sigue distribución normal.")

# TEST DE HOMOCEDASTICIDAD (LEVENE)

print("\n\nTest de Levene para homocedasticidad")

listas_datos = [serie for serie in datos_finales.values() if len(serie) >= 2]
stat, p_val = ss.levene(*listas_datos, center="median")

print(f"Estadístico = {stat:.2f}")
print(f"p-valor = {p_val:.4f}")
if p_val > 0.05:
    print(" Se acepta H0: Se asume homocedasticidad (varianzas iguales).")
else:
    print(" Se rechaza H0: Hay evidencia de heterocedasticidad (varianzas diferentes).")

# DADO QUE NO TODAS LAS MUESTRAS TIENEN DISTRIBUCION NORMLA Y QUE NO HAY HOMOCEDASTICIDAD SE DEBE HACER UN ANALISIS NO PARAMÉTRICO DE LAS MADIAS
# METODO NO PARAMÉTRICO DE MANN-WHITNEY Y MÉTODO NO PARAMÉTRICO DE WELCH

cepas_comparar = ["LPU83_0308", "LPU83_1066", "LPU83_1088", "LPU83_1729"]
resultados = []

print("\n\nComparaciones LPU83_WT vs mutantes (Mann-Whitney y Welch)")

for col in cepas_comparar:
    if col in supervivencia_nodulos.columns and supervivencia_nodulos[col].dtype in [
        np.float64,
        np.int64,
    ]:

        grupo = supervivencia_nodulos[col].dropna()

        # Mann-Whitney
        u_stat, p_val_mw = ss.mannwhitneyu(wt, grupo, alternative="two-sided")

        # t-test de Welch
        t_stat, p_val_welch = ss.ttest_ind(
            wt, grupo, equal_var=False, nan_policy="omit"
        )

        resultados.append(
            {
                "Comparación": f"LPU83_WT vs {col}",
                "Mann-Whitney U": u_stat,
                "p-valor MW": p_val_mw,
                "t de Welch": t_stat,
                "p-valor Welch": p_val_welch,
            }
        )

df_comparaciones = pd.DataFrame(resultados)

print("\nTabla resumen de comparaciones")
print(df_comparaciones)

# Leer hoja de pesos de nódulos
peso_nodulos_total = pd.read_excel(
    r"C:\Doctorado TODO\Especializacion_bioinformatica\MANEJO DE DATOS EN BIOLOGÍA COMPUTACIONAL. HERRAMIENTAS DE ESTADÍSTICA (2024)\Trabajo_Final\Supervivencia_sobre_mg_nodulosXplanta.xlsx",
    sheet_name="peso_nódulos_mg_planta",
)

print("\nColumnas en hoja de pesos:", peso_nodulos_total.columns.tolist())

print("\n=== Correlación Spearman entre recuento viable y peso total de nódulo ===")

correlaciones = []

for col in supervivencia_nodulos.columns:
    if col in peso_nodulos_total.columns:
        serie_supervivencia = supervivencia_nodulos[col]
        serie_peso = peso_nodulos_total[col]

        # Combinar evitando NaNs
        temp_df = pd.concat([serie_supervivencia, serie_peso], axis=1).dropna()

        if len(temp_df) > 1:
            rho, p_val = ss.spearmanr(temp_df.iloc[:, 0], temp_df.iloc[:, 1])
            correlaciones.append(
                {"Cepa": col, "Coeficiente rho (Spearman)": rho, "p-valor": p_val}
            )
            print(f"\nCepa: {col}")
            print(f"  Coeficiente rho = {rho:.2f}")
            print(f"  p-valor = {p_val:.4f}")
        else:
            print(f"\nCepa: {col}")
            print("  No hay suficientes datos para calcular correlación.")

# Convertir en DataFrame resumen
df_corr = pd.DataFrame(correlaciones)

print("\n=== Resumen de correlaciones ===")
print(df_corr)


# PERSPECTIVAS
# TAMAÑO MUESTRAL

print(
    "\n=== Tamaño de muestra específico para comparaciones LPU83_1088 y LPU83_1729 ==="
)


def calcular_effect_size(grupo1, grupo2):
    mean_diff = np.abs(np.mean(grupo1) - np.mean(grupo2))
    pooled_sd = np.sqrt(
        ((np.std(grupo1, ddof=1) ** 2) + (np.std(grupo2, ddof=1) ** 2)) / 2
    )
    d = mean_diff / pooled_sd
    return d


wt = datos_finales["LPU83_WT"]
mut1088 = datos_finales["LPU83_1088"]
mut1729 = datos_finales["LPU83_1729"]

effect_size_1088 = calcular_effect_size(wt, mut1088)
n_1088 = smp.tt_ind_solve_power(
    effect_size=effect_size_1088, alpha=0.05, power=0.8, alternative="two-sided"
)

effect_size_1729 = calcular_effect_size(wt, mut1729)
n_1729 = smp.tt_ind_solve_power(
    effect_size=effect_size_1729, alpha=0.05, power=0.8, alternative="two-sided"
)

print(f"\nLPU83_WT vs LPU83_1088:")
print(f"  Effect size (d): {effect_size_1088:.2f}")
print(f"  Tamaño de muestra recomendado: {np.ceil(n_1088)} muestras por grupo.")

print(f"\nLPU83_WT vs LPU83_1729:")
print(f"  Effect size (d): {effect_size_1729:.2f}")
print(f"  Tamaño de muestra recomendado: {np.ceil(n_1729)} muestras por grupo.")
