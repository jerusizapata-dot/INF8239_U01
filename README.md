\# INF8239\_U01 — Clasificación con SVM



\## U01.LAB02 — Clasificación con SVM, auditoría de datos y evaluación



\*\*Asignatura:\*\* INF-8239 Ciencia de Datos II  

\*\*Unidad:\*\* 01 - Modelos avanzados, reducción dimensional y Green AI  

\*\*Estudiante:\*\* Laudys Jerusi Zapata



\---



\## 1. Descripción del proyecto



Este proyecto desarrolla una tarea de clasificación mediante \*\*Máquinas de Vectores de Soporte (SVM)\*\* utilizando información agregada de las \*\*Pruebas Nacionales de la República Dominicana, período 2016–2024\*\*.



La unidad de análisis corresponde a un registro agregado de Pruebas Nacionales identificado por período, convocatoria, centro educativo y nivel/modalidad.



\### Pregunta de análisis



¿Es posible clasificar si en un registro de Pruebas Nacionales predomina la cantidad de estudiantes promovidos sobre la cantidad de estudiantes aplazados utilizando variables disponibles al momento de realizar la predicción?



El proyecto incluye la selección y auditoría del dataset, definición del target, prevención de fuga de información, preprocesamiento mediante pipelines, comparación con un modelo baseline y evaluación de un modelo SVM.



La métrica principal utilizada para la comparación es \*\*F1 macro\*\*, complementada con Accuracy, Precision, Recall, matriz de confusión y reporte de clasificación.



\---



\## 2. Dataset utilizado



\*\*Nombre:\*\* Estadísticas de Pruebas Nacionales, 2016–2024



\*\*Fuente:\*\* Portal de Datos Abiertos de la República Dominicana / Ministerio de Educación de la República Dominicana (MINERD).



El archivo utilizado localmente es:



```text

data/raw/pruebas\_nacionales\_2016\_2024.csv

```



El dataset contiene información agregada sobre los resultados de las Pruebas Nacionales, incluyendo período, convocatoria, regional, distrito, nivel/modalidad, centro educativo, resultados por área y cantidades de estudiantes promovidos y aplazados.



El archivo CSV utiliza:



\- separador: `;`

\- codificación: `latin1`



La documentación relacionada con la selección y procedencia del dataset se encuentra en:



```text

docs/ficha\_dataset.md

docs/comparacion\_datasets.md

```



El diccionario de datos se encuentra en:



```text

docs/diccionario\_datos.md

```



\---



\## 3. Selección y aceptación del dataset



Como parte del proceso de selección se comparó el dataset de \*\*Pruebas Nacionales 2016–2024\*\* con el dataset utilizado en LAB01, \*\*Breast Cancer Wisconsin Diagnostic\*\*.



La comparación consideró criterios relacionados con:



\- procedencia;

\- licencia;

\- cantidad de registros y variables;

\- definición del target;

\- valores ausentes;

\- riesgo de fuga de información;

\- disponibilidad de las variables al momento de realizar la predicción;

\- posibilidad de ejecución en CPU.



La documentación de esta comparación se encuentra en:



```text

docs/comparacion\_datasets.md

```



\---



\## 4. Unidad de análisis



La unidad de análisis corresponde a un \*\*registro agregado de Pruebas Nacionales por período, convocatoria, centro educativo y nivel/modalidad\*\*.



Por tanto, el modelo no realiza una predicción individual sobre estudiantes. La clasificación se realiza sobre registros agregados de resultados educativos.



\---



\## 5. Construcción del target



El target se construye a partir de la relación entre la cantidad de estudiantes promovidos y la cantidad de estudiantes aplazados.



La codificación utilizada es:



\- `1` → Promovidos > Aplazados

\- `0` → Promovidos < Aplazados



Los registros donde la cantidad de promovidos es igual a la cantidad de aplazados se excluyen debido a que representan un empate y no corresponden naturalmente a ninguna de las dos clases.



El target representa, por tanto, el \*\*predominio de promoción frente a aplazamiento\*\* dentro de cada registro agregado.



\---



\## 6. Preparación y limpieza de los datos



Antes del modelado se aplicaron criterios de calidad y consistencia:



1\. Se excluyeron los registros correspondientes al año 2020 debido a sus características estructurales particulares.

2\. Se eliminaron registros con valores faltantes en `Cantidad Promovidos` o `Cantidad Aplazados`.

3\. Se eliminaron duplicados exactos.

4\. Se verificó la consistencia entre:

&#x20;  

&#x20;  `Cantidad de estudiantes = Cantidad Promovidos + Cantidad Aplazados`



5\. Se excluyeron los registros que no cumplían dicha relación.

6\. Se excluyeron los empates entre promovidos y aplazados.

7\. Finalmente se construyó la variable binaria `target`.



Después de estas reglas de preparación, el conjunto utilizado para el modelado contiene:



\*\*46,992 registros.\*\*



Distribución del target:



| Clase | Interpretación | Registros | Proporción |

|---|---|---:|---:|

| 0 | Aplazados predominan | 9,763 | 20.78 % |

| 1 | Promovidos predominan | 37,229 | 79.22 % |



\---



\## 7. Prevención de fuga de información



La prevención de fuga de información constituye una parte fundamental del diseño del experimento.



Las variables:



```text

Cantidad Promovidos

Cantidad Aplazados

```



no se utilizan como predictores porque ambas participan directamente en la construcción del target.



También se excluyeron las variables:



```text

Español

Matemáticas

Sociales

Naturales

```



debido a que corresponden a resultados de las evaluaciones y podrían incorporar información asociada al resultado que se pretende clasificar.



Las variables:



```text

Código de Centro

Nombre de Centro

```



se excluyeron para reducir el riesgo de que el modelo memorice identificadores específicos de centros educativos y para favorecer una mejor generalización.



Las variables:



```text

Cantidad Femenino

Cantidad masculino

```



también fueron excluidas debido a su carácter redundante respecto de `Cantidad de estudiantes`.



\---



\## 8. Variables predictoras



Las variables utilizadas finalmente como predictores son:



\- `Período`

\- `Convocatoria`

\- `Regional`

\- `Distrito`

\- `Nivel/Modalidad`

\- `Cantidad de estudiantes`



Estas variables representan información estructural y agregada que puede utilizarse para caracterizar el registro sin utilizar directamente las variables que definen el resultado objetivo.



El detalle de las variables, significado, tipo, disponibilidad y riesgos se encuentra en:



```text

docs/diccionario\_datos.md

```



\---



\## 9. Preprocesamiento



El preprocesamiento se realiza dentro de un \*\*Pipeline\*\*, evitando realizar transformaciones utilizando información del conjunto de prueba.



\### Variables numéricas



Para las variables numéricas se utiliza:



\- `SimpleImputer(strategy="median")`

\- `StandardScaler()`



\### Variables categóricas



Para las variables categóricas se utiliza:



\- `SimpleImputer(strategy="most\_frequent")`

\- `OneHotEncoder(handle\_unknown="ignore")`



El procesamiento se integra mediante `ColumnTransformer`.



Esta estructura permite que las transformaciones sean ajustadas únicamente con los datos de entrenamiento durante el proceso de modelado.



\---



\## 10. División entrenamiento-prueba



Los datos se dividen utilizando:



\- \*\*80 %\*\* para entrenamiento;

\- \*\*20 %\*\* para prueba;

\- división estratificada según el target;

\- `random\_state=42`.



La misma partición entrenamiento-prueba se utiliza para el baseline y para el modelo SVM, permitiendo realizar una comparación bajo las mismas condiciones.



\---



\## 11. Modelo baseline



Como referencia se utiliza:



```python

DummyClassifier(strategy="most\_frequent")

```



Este modelo asigna siempre la clase mayoritaria.



Su propósito es establecer un punto de referencia que permita determinar si el modelo SVM aporta un comportamiento diferente al de una estrategia trivial basada exclusivamente en la distribución de clases.



La métrica principal para la comparación es \*\*F1 macro\*\*, ya que considera el desempeño de las dos clases y evita que la clase mayoritaria domine completamente la interpretación.



\---



\## 12. Modelo SVM



Se utiliza una \*\*Máquina de Vectores de Soporte (SVM)\*\* integrada dentro de un pipeline de preprocesamiento.



El clasificador utiliza un kernel RBF y los parámetros establecidos para la práctica.



La estructura general es:



```text

Preprocesamiento

&#x20;      ↓

ColumnTransformer

&#x20;      ↓

SVM

&#x20;      ↓

Predicción

&#x20;      ↓

Evaluación

```



El modelo se evalúa utilizando exactamente la misma partición de entrenamiento y prueba empleada para el baseline.



\---



\## 13. Evaluación



La evaluación considera diferentes métricas:



\- Accuracy;

\- Precision;

\- Recall;

\- F1;

\- F1 macro;

\- matriz de confusión;

\- reporte de clasificación.



La métrica principal es \*\*F1 macro\*\* debido al desbalance existente entre las clases.



La matriz de confusión permite observar directamente la cantidad de predicciones correctas e incorrectas para cada clase.



El reporte de clasificación permite analizar Precision, Recall y F1 de manera separada para las clases 0 y 1.



\---



\## 14. Pruebas automatizadas



El proyecto incorpora pruebas automatizadas mediante `pytest`.



El archivo de pruebas es:



```text

tests/test\_data\_contract.py

```



Actualmente se verifican, entre otros aspectos:



\- que el dataset no esté vacío;

\- que existan las columnas requeridas;

\- que el target no tenga valores faltantes;

\- que el target contenga al menos dos clases.



Las pruebas se ejecutan mediante:



```cmd

python -m pytest -q

```



Resultado obtenido durante la verificación:



```text

3 passed

```



\---



\## 15. Descarga reproducible



El código reutilizable para la descarga y carga del dataset se encuentra en:



```text

src/inf8239\_u01/data.py

```



El módulo incluye funciones para:



\- descargar un archivo CSV desde una URL;

\- guardar el archivo en una ruta determinada;

\- cargar el dataset con el separador y codificación correspondientes;

\- validar que el archivo exista y no esté vacío.



La importación del módulo fue verificada correctamente dentro del entorno virtual.



\---



\## 16. Ejecución del proyecto



\### Activar el entorno virtual



En Windows:



```cmd

.venv\\Scripts\\activate

```



\### Configurar el código fuente



En PowerShell:



```powershell

$env:PYTHONPATH="src"

```



\### Ejecutar las pruebas



```cmd

python -m pytest -q

```



\### Ejecutar el análisis



El análisis principal se encuentra en:



```text

notebooks/

```



El notebook debe ejecutarse de principio a fin para reproducir las etapas de carga, auditoría, preparación, modelado y evaluación.



\---



\## 17. Estructura del proyecto



```text

INF8239\_U01/

│

├── data/

│   └── raw/

│       └── pruebas\_nacionales\_2016\_2024.csv

│

├── docs/

│   ├── ficha\_dataset.md

│   ├── comparacion\_datasets.md

│   └── diccionario\_datos.md

│

├── notebooks/

│

├── reports/

│

├── src/

│   └── inf8239\_u01/

│       └── data.py

│

├── tests/

│   └── test\_data\_contract.py

│

├── .gitignore

├── requirements.txt

└── README.md

```



\---



\## 18. Control de versiones



El proyecto utiliza Git para registrar cambios significativos.



Hasta el momento se han realizado los siguientes commits:



```text

abd342d — docs: documenta dataset, diccionario y contrato de datos



0b3319a — feat: agrega descarga reproducible del dataset

```



Estos commits permiten mantener trazabilidad sobre la documentación inicial y la incorporación del código reutilizable para la descarga del dataset.



\---



\## 19. Conclusión



El desarrollo de este LAB02 permitió construir una tarea de clasificación a partir de información agregada de las Pruebas Nacionales de la República Dominicana. El proceso comenzó con la definición del dominio, la unidad de análisis y la decisión que se busca apoyar, antes de proceder con la selección y revisión del conjunto de datos. Esta etapa permitió establecer una pregunta de análisis concreta y criterios para evaluar la utilidad del dataset.



La construcción del target se realizó a partir de la comparación entre la cantidad de estudiantes promovidos y aplazados en cada registro agregado. Se excluyeron los empates y los registros que presentaban inconsistencias entre la cantidad total de estudiantes y la suma de promovidos y aplazados. También se excluyeron los registros del año 2020 por sus características estructurales particulares.



Una consideración fundamental fue la prevención de fuga de información. Las cantidades de promovidos y aplazados no se utilizaron como variables predictoras debido a que intervienen directamente en la definición del target. Asimismo, se excluyeron los resultados por área de evaluación, los identificadores de los centros educativos y variables redundantes relacionadas con el sexo de los estudiantes.



Para el modelado se estableció una partición estratificada de entrenamiento y prueba y se utilizó la misma división para el baseline y el modelo SVM. El preprocesamiento se integró mediante `ColumnTransformer` y `Pipeline`, permitiendo realizar la imputación, estandarización y codificación categórica dentro del flujo de entrenamiento.



La evaluación utiliza F1 macro como métrica principal, acompañada de Accuracy, Precision, Recall, matriz de confusión y reporte de clasificación. Finalmente, el proyecto incorpora pruebas automatizadas, documentación del dataset, diccionario de variables, código reutilizable y control de versiones, fortaleciendo la reproducibilidad y trazabilidad del análisis.

