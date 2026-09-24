# INF8239_U01 — Clasificación con SVM

## U01.LAB01 — SVM con pipeline, búsqueda de parámetros y evaluación

**Asignatura:** INF-8239 Ciencia de Datos II
**Unidad:** 01 - Modelos avanzados, reducción dimensional y Green AI
**Estudiante:** Laudys Jerusi Zapata

---

## 1. Descripción del proyecto

Este proyecto implementa un modelo de clasificación mediante **Máquinas de Vectores de Soporte (SVM)** utilizando el conjunto de datos **Breast Cancer Wisconsin**, disponible mediante `scikit-learn`.

El objetivo es construir una línea base y una SVM utilizando un flujo de trabajo reproducible, evitando fuga de información durante el preprocesamiento y evaluando diferentes configuraciones de los hiperparámetros `C` y `gamma`.

> El ejercicio tiene fines académicos y el modelo no constituye una herramienta de diagnóstico médico.

## 2. Pregunta de análisis

¿Es posible clasificar el diagnóstico de tumores de mama utilizando las características numéricas disponibles en el conjunto de datos Breast Cancer Wisconsin mediante un modelo SVM?

## 3. Datos

El conjunto de datos contiene:

- **569 observaciones**
- **30 variables predictoras numéricas**
- **2 clases**
- Variable objetivo: diagnóstico (`target`)

Antes del modelado se realiza una auditoría básica de los datos para revisar tipos, valores ausentes, valores únicos, duplicados y posibles problemas relacionados con la variable objetivo.

## 4. Metodología

El conjunto de datos se divide en entrenamiento y prueba utilizando:

- `test_size=0.20`
- `random_state=42`
- `stratify=y`

El escalado se realiza dentro de un `Pipeline` mediante `StandardScaler`, seguido de una SVM con kernel RBF.

La configuración base utiliza:

- `C=1`
- `gamma="scale"`
- `kernel="rbf"`

También se utiliza una `DummyClassifier` como línea base.

## 5. Búsqueda de hiperparámetros

Los hiperparámetros se comparan mediante `GridSearchCV` y validación cruzada estratificada de 5 particiones.

Se evalúan:

- `C`: 0.1, 1 y 10
- `gamma`: `scale`, 0.01 y 0.1

La métrica utilizada para seleccionar la configuración es **F1-macro**.

La búsqueda se realiza únicamente sobre el conjunto de entrenamiento, manteniendo separado el conjunto de prueba para la evaluación final.

## 6. Evaluación

El modelo se evalúa utilizando:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Matriz de confusión

Los resultados detallados de la búsqueda de parámetros se almacenan en:

`reports/svm_cv_results.csv`

El modelo seleccionado se guarda en:

`reports/svm_best.joblib`

## 7. Código reutilizable

La construcción del modelo SVM se encuentra en:

`src/inf8239_u01/models.py`

La función principal es:

`build_svm(C=1.0, gamma="scale")`

Esta función construye un pipeline que incluye el escalado y el clasificador SVM.

## 8. Pruebas

El proyecto incorpora pruebas automatizadas mediante `pytest`.

Las pruebas verifican, entre otros aspectos:

- que el modelo produzca una predicción por cada fila;
- que se rechacen valores no positivos de `C`;
- que el pipeline contenga correctamente las etapas de escalado y modelado.

Para ejecutar las pruebas:

```powershell
set PYTHONPATH=src
python -m pytest -q
```

## 9. Estructura del proyecto

```text
INF8239_U01/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── 00_verificacion.ipynb
│   └── 01_svm_guiada.ipynb
│
├── reports/
│   ├── svm_best.joblib
│   └── svm_cv_results.csv
│
├── src/
│   └── inf8239_u01/
│       ├── __init__.py
│       ├── environment.py
│       └── models.py
│
└── tests/
    ├── test_environment.py
    └── test_models.py
```

## 10. Reproducibilidad

Se recomienda utilizar un entorno virtual de Python.

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\Activate
```

Configurar el directorio `src` para las pruebas:

```powershell
set PYTHONPATH=src
```

Ejecutar las pruebas:

```powershell
python -m pytest -q
```

El notebook principal es:

`notebooks/01_svm_guiada.ipynb`

## 11. Repositorio

El código fuente y los archivos de la práctica se encuentran disponibles en el repositorio de GitHub:

`https://github.com/jerusizapata-dot/INF8239_U01`

## 12. Conclusión

La práctica permitió implementar un flujo completo de clasificación con SVM, desde la auditoría inicial de los datos hasta la evaluación del modelo y la búsqueda de hiperparámetros. La utilización de un `Pipeline` permite integrar el escalado con el clasificador y evita realizar el ajuste del transformador utilizando información del conjunto de prueba.

La línea base proporciona una referencia sencilla para interpretar el comportamiento del modelo. Posteriormente, la SVM con kernel RBF permite evaluar configuraciones diferentes de `C` y `gamma` mediante validación cruzada estratificada. La selección se realiza utilizando F1-macro, evitando elegir hiperparámetros a partir de los resultados del conjunto de prueba.

La matriz de confusión y las métricas de clasificación permiten analizar los aciertos y errores de cada clase, mientras que ROC-AUC complementa la evaluación del comportamiento discriminativo. Además, los resultados de la validación cruzada se almacenan en formato CSV y el modelo seleccionado se conserva como archivo serializado para facilitar su reutilización.

Finalmente, la separación del código reutilizable en `src`, las pruebas automatizadas y el archivo de requisitos contribuyen a que el experimento sea reproducible y verificable. El ejercicio también refuerza la importancia de prevenir la fuga de información y de mantener el conjunto de prueba separado hasta la evaluación final.
