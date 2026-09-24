# INF8239_U01 — Clasificación con SVM

## Práctica Guiada — LAB02

**Estudiante:** Laudys Jerusi Zapata  
**Programa:** Maestría en Ciencia de Datos e Inteligencia Artificial  
**Asignatura:** INF8239 — Ciencia de Datos e Inteligencia Artificial  
**Institución:** Universidad Autónoma de Santo Domingo (UASD)

---

## 1. Descripción del proyecto

Este proyecto corresponde a la integración de LAB01 y LAB02 de la asignatura INF8239. Se desarrolla un modelo de clasificación utilizando **Support Vector Machine (SVM)** para analizar información agregada de las Pruebas Nacionales de la República Dominicana.

El análisis utiliza exclusivamente los datos correspondientes al **año 2024**, con el propósito de clasificar los registros de centros educativos según su nivel de promoción.

### Pregunta de análisis

¿Es posible clasificar los registros de centros educativos según su nivel de promoción utilizando características estructurales y administrativas disponibles antes de considerar directamente las cantidades de estudiantes promovidos y aplazados?

### Unidad de análisis

Registro agregado de centro educativo.

### Variable objetivo

La variable objetivo es `target_promocion`, construida a partir de la tasa de promoción:

```text
tasa_promocion = Cantidad Promovidos / Cantidad de estudiantes
```

Se utilizó como punto de corte la mediana de la tasa de promoción:

```text
0.8037
```

La clasificación se definió de la siguiente manera:

- **1 — Alto nivel de promoción:** tasa de promoción mayor o igual a 0.8037.
- **0 — Bajo nivel de promoción:** tasa de promoción menor que 0.8037.

El resultado produce dos clases balanceadas:

| Clase | Cantidad | Proporción |
|---|---:|---:|
| 0 — Bajo nivel de promoción | 1,737 | 50.00% |
| 1 — Alto nivel de promoción | 1,737 | 50.00% |
| **Total** | **3,474** | **100%** |

---

## 2. Dataset utilizado

El archivo original contiene información de las Pruebas Nacionales para el período 2016–2024. Para este proyecto se seleccionaron únicamente los registros correspondientes a **2024**.

Archivo utilizado:

```text
data/raw/pruebas_nacionales_2016_2024.csv
```

### Características del dataset

- Registros correspondientes a 2024: **3,474**
- Variables originales: **16**
- Fuente: datos de Pruebas Nacionales de la República Dominicana.
- Período analizado: **2024**

---

## 3. Variables utilizadas

Después de realizar la auditoría y el análisis de posibles fugas de información (*data leakage*), se utilizaron como variables predictoras:

```text
Regional
Distrito
Nivel/Modalidad
Cantidad de estudiantes
```

### Variables categóricas

```text
Regional
Distrito
Nivel/Modalidad
```

Estas variables fueron procesadas mediante imputación de valores faltantes y codificación *One-Hot Encoding*.

### Variable numérica

```text
Cantidad de estudiantes
```

Esta variable fue procesada mediante imputación por mediana y estandarización.

---

## 4. Prevención de fuga de información

Para evitar que el modelo utilizara información directamente relacionada con la construcción del objetivo, se excluyeron variables como:

```text
Período
Convocatoria
Código de Centro
Nombre de Centro
Cantidad Promovidos
Cantidad Aplazados
Cantidad Femenino
Cantidad masculino
Español
Matemáticas
Sociales
Naturales
tasa_promocion
```

La variable `tasa_promocion` se utiliza exclusivamente para construir `target_promocion` y no se entrega como predictor al modelo.

También se excluyeron `Cantidad Promovidos` y `Cantidad Aplazados`, debido a que participan directamente en la definición del nivel de promoción.

---

## 5. División de los datos

Los datos se dividieron utilizando una partición estratificada:

- **80% entrenamiento:** 2,779 registros.
- **20% prueba:** 695 registros.
- `random_state = 42`.

La estratificación permite conservar aproximadamente la misma proporción de las dos clases en los conjuntos de entrenamiento y prueba.

---

## 6. Preprocesamiento

Se construyó un pipeline reproducible mediante `ColumnTransformer` y `Pipeline`.

Para la variable numérica:

1. Imputación de valores faltantes mediante la mediana.
2. Estandarización mediante `StandardScaler`.

Para las variables categóricas:

1. Imputación de valores faltantes mediante la categoría más frecuente.
2. Codificación mediante `OneHotEncoder(handle_unknown="ignore")`.

Este procedimiento permite que el preprocesamiento forme parte del flujo del modelo y evita aplicar transformaciones utilizando información del conjunto de prueba.

---

## 7. Modelo baseline

Como referencia se utilizó un `DummyClassifier` con estrategia:

```text
most_frequent
```

El resultado obtenido fue:

| Modelo | F1 macro |
|---|---:|
| DummyClassifier — baseline | **0.3330** |

Este baseline proporciona un punto de comparación para evaluar el comportamiento del modelo SVM.

---

## 8. Modelo SVM

Se utilizó un modelo **Support Vector Machine (SVM)** con:

```text
kernel = RBF
random_state = 42
```

El modelo fue integrado dentro del pipeline junto con el preprocesamiento.

### Resultados del modelo SVM

| Métrica | Resultado |
|---|---:|
| Accuracy | **0.6187** |
| Precision | **0.6273** |
| Recall | **0.5821** |
| F1 macro | **0.6182** |
| ROC-AUC | **0.6813** |

### Comparación con el baseline

| Modelo | F1 macro |
|---|---:|
| DummyClassifier — baseline | **0.3330** |
| SVM RBF | **0.6182** |

El F1 macro del SVM es superior al obtenido por el baseline, lo que permite observar una diferencia entre un clasificador trivial y el modelo entrenado con las variables seleccionadas.

---

## 9. Matriz de confusión

La matriz de confusión obtenida fue:

```text
[[228, 120],
 [145, 202]]
```

Interpretación:

- 228 registros de la clase 0 fueron clasificados correctamente.
- 120 registros de la clase 0 fueron clasificados como clase 1.
- 145 registros de la clase 1 fueron clasificados como clase 0.
- 202 registros de la clase 1 fueron clasificados correctamente.

---

## 10. Reporte de clasificación

Los principales resultados por clase fueron:

| Clase | Precision | Recall | F1-score |
|---|---:|---:|---:|
| 0 — Bajo nivel de promoción | 0.61 | 0.66 | 0.63 |
| 1 — Alto nivel de promoción | 0.63 | 0.58 | 0.60 |

El modelo presenta resultados relativamente próximos entre ambas clases, aunque existen diferencias entre precision y recall.

---

## 11. Estructura del proyecto

```text
INF8239_U01/
│
├── data/
│   └── raw/
│       └── pruebas_nacionales_2016_2024.csv
│
├── notebooks/
│   └── 01_svm_lab02.ipynb
│
├── src/
│   └── inf8239_u01/
│       ├── __init__.py
│       ├── data.py
│       └── environment.py
│
├── tests/
│   ├── test_data.py
│   └── test_environment.py
│
├── docs/
│   ├── ficha_dataset.md
│   ├── comparacion_datasets.md
│   └── diccionario_datos.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 12. Pruebas

Las pruebas automatizadas se ejecutaron mediante:

```text
python -m pytest -q
```

Resultado:

```text
3 passed in 0.71s
```

Las pruebas verifican aspectos relacionados con la carga de datos, validación de entradas y funcionamiento del módulo de entorno.

---

## 13. Reproducibilidad

Para reproducir el proyecto se recomienda utilizar un entorno virtual de Python.

Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

Ejecutar las pruebas:

```powershell
python -m pytest -q
```

El notebook principal se encuentra en:

```text
notebooks/01_svm_lab02.ipynb
```

El análisis puede ejecutarse utilizando el entorno virtual configurado para el proyecto.

---

## 14. Rama de entrega

La rama utilizada para la entrega de LAB02 es:

```text
INF8239_U01_LAB02
```

El repositorio corresponde a:

```text
INF8239_U01
```

---

## 15. Conclusión

El proyecto permitió integrar las actividades desarrolladas durante LAB01 y LAB02 mediante un flujo reproducible de preparación de datos, construcción de una variable objetivo, prevención de fuga de información, preprocesamiento y entrenamiento de un modelo SVM. Para el análisis se utilizaron exclusivamente los registros correspondientes al año 2024 de las Pruebas Nacionales de la República Dominicana, con 3,474 registros y una clasificación binaria basada en la mediana de la tasa de promoción.

La variable objetivo `target_promocion` se construyó a partir de la relación entre estudiantes promovidos y cantidad total de estudiantes. Para evitar que el modelo recibiera información directamente relacionada con la construcción del objetivo, se excluyeron las variables `Cantidad Promovidos`, `Cantidad Aplazados` y `tasa_promocion`, además de otras variables identificadoras y académicas. Finalmente, se conservaron cuatro predictores: `Regional`, `Distrito`, `Nivel/Modalidad` y `Cantidad de estudiantes`.

El conjunto de datos se dividió de forma estratificada en entrenamiento y prueba, utilizando un 80% y 20%, respectivamente. Como referencia se implementó un `DummyClassifier`, que obtuvo un F1 macro de 0.3330. Posteriormente se entrenó un SVM con kernel RBF integrado en un pipeline de preprocesamiento. El modelo obtuvo un Accuracy de 0.6187, Precision de 0.6273, Recall de 0.5821, F1 macro de 0.6182 y ROC-AUC de 0.6813.

Estos resultados muestran que el modelo SVM logró una capacidad de clasificación superior al baseline utilizado como referencia, aunque todavía presenta errores de clasificación en ambas categorías. La matriz de confusión registró 228 verdaderos negativos, 120 falsos positivos, 145 falsos negativos y 202 verdaderos positivos. Por tanto, los resultados deben interpretarse dentro del alcance de las variables disponibles y de la definición agregada del objetivo.

Finalmente, la incorporación de pruebas automatizadas, documentación, estructura modular y un notebook ejecutable permite que el análisis sea reproducible y verificable. El proyecto constituye así una integración de los principales componentes trabajados en LAB01 y LAB02, desde la preparación y auditoría de los datos hasta la evaluación de un modelo de aprendizaje supervisado.