\# Comparación de candidatos



\## Candidato A — Dataset utilizado en LAB01



\*\*Breast Cancer Wisconsin Diagnostic\*\*



\### Identificación y procedencia



\- \*\*Procedencia:\*\* `sklearn.datasets`, mediante la función `load\_breast\_cancer`.

\- \*\*Fuente original:\*\* UCI Machine Learning Repository — Breast Cancer Wisconsin (Diagnostic).

\- \*\*Ficha técnica:\*\* https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic

\- \*\*Documentación utilizada en LAB01:\*\* https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load\_breast\_cancer.html

\- \*\*Dominio:\*\* Salud / clasificación diagnóstica.

\- \*\*Unidad de análisis:\*\* muestra diagnóstica de tejido mamario.

\- \*\*Filas:\*\* 569.

\- \*\*Variables predictoras:\*\* 30 características numéricas.

\- \*\*Target:\*\* diagnóstico del tumor, con dos clases.

\- \*\*Ausentes:\*\* no presenta valores ausentes en la versión utilizada.

\- \*\*Tipo de tarea:\*\* clasificación binaria.

\- \*\*Uso en LAB01:\*\* clasificación mediante Máquinas de Vectores de Soporte (SVM).



\### Licencia y condiciones de uso



El conjunto utilizado en LAB01 se distribuye mediante `scikit-learn` y corresponde a una copia del conjunto Breast Cancer Wisconsin (Diagnostic) procedente de UCI. La documentación de scikit-learn identifica explícitamente la fuente original y las características del conjunto.



\*\*Nota:\*\* la licencia del software scikit-learn no debe confundirse con la licencia o condiciones de uso de los datos originales de UCI. Por esta razón, para la comparación se conserva la referencia a la fuente original.



\### Riesgo de fuga



El riesgo de fuga es bajo si las 30 características se mantienen separadas del target y el procesamiento se ajusta únicamente sobre los datos de entrenamiento.



\---



\## Candidato B — Dataset seleccionado para LAB02



\*\*Estadísticas de Pruebas Nacionales, 2016-2024\*\*



\### Identificación y procedencia



\- \*\*Procedencia:\*\* Portal de Datos Abiertos de la República Dominicana / Ministerio de Educación (MINERD).

\- \*\*Fuente institucional:\*\* Ministerio de Educación de la República Dominicana.

\- \*\*Autor:\*\* Dirección General de Evaluación y Control de la Calidad Educativa.

\- \*\*Ficha del conjunto de datos:\*\* https://datos.gob.do/dataset/c99df9fc-6d99-4cb3-8f2b-81d5753d51b7

\- \*\*Fuente institucional:\*\* http://www.ministeriodeeducacion.gob.do/

\- \*\*Última actualización registrada:\*\* 2 de abril de 2025.

\- \*\*Periodicidad:\*\* anual.

\- \*\*Licencia:\*\* Open Data Commons Open Database License (ODbL).

\- \*\*Dominio:\*\* Educación.

\- \*\*Filas:\*\* 57,586.

\- \*\*Columnas:\*\* 16.

\- \*\*Unidad de análisis:\*\* registro agregado de resultados educativos por período, convocatoria, centro educativo y nivel/modalidad.

\- \*\*Target:\*\* predominio de estudiantes promovidos frente a estudiantes aplazados.

\- \*\*Tipo de tarea:\*\* clasificación binaria.



\### Archivos disponibles



El Portal de Datos Abiertos ofrece el conjunto en formatos XLSX, CSV y ODS.



\*\*Descarga reproducible:\*\* el archivo CSV utilizado en este proyecto se conserva en:



`data/raw/pruebas\_nacionales\_2016\_2024.csv`



La ruta de descarga oficial se documenta también en la sección de descarga reproducible del proyecto.



\### Ausentes y particularidades



El conjunto presenta valores ausentes, principalmente en variables relacionadas con resultados, convocatoria y cantidad de aplazados.



El año 2020 requiere un tratamiento especial debido a la suspensión de las Pruebas Nacionales en el contexto de la pandemia. Por esta razón, los registros de 2020 se excluyen del conjunto utilizado para la modelización.



\### Riesgo de fuga



El riesgo de fuga es alto en variables que representan directamente resultados de las pruebas o cantidades utilizadas para construir el target.



Por esta razón:



\- `Cantidad Promovidos` no se utiliza como predictor.

\- `Cantidad Aplazados` no se utiliza como predictor.

\- `Español`, `Matemáticas`, `Sociales` y `Naturales` se excluyen porque representan resultados contemporáneos al fenómeno que se pretende clasificar.

\- `Código de Centro` y `Nombre de Centro` se excluyen para reducir el riesgo de memorizar centros específicos y favorecer la generalización.

\- `Cantidad Femenino` y `Cantidad masculino` se excluyen por redundancia con `Cantidad de estudiantes` y por las inconsistencias detectadas en la auditoría.



\---



\## Tabla comparativa



| Criterio | Candidato A: Breast Cancer Wisconsin | Candidato B: Pruebas Nacionales |

|---|---|---|

| Uso previo | LAB01 | LAB02 |

| Procedencia | scikit-learn / UCI | Portal de Datos Abiertos / MINERD |

| Dominio | Salud | Educación |

| Filas | 569 | 57,586 |

| Variables | 30 predictoras + target | 16 columnas originales |

| Target | Diagnóstico binario | Predominio de promoción |

| Clases | 2 | 2 |

| Ausentes | No | Sí |

| Unidad de análisis | Muestra diagnóstica | Registro educativo agregado |

| Riesgo de fuga | Bajo | Requiere auditoría y exclusiones |

| Compatibilidad con CPU | Alta | Alta con preprocesamiento adecuado |

| Pregunta de análisis | Diagnóstico de tumor | Clasificación de predominio de promoción/aplazamiento |

| Documentación | Disponible | Disponible |

| Licencia/procedencia | Fuente UCI y distribución mediante scikit-learn | ODbL / MINERD |



\---



\## Criterios de aceptación



Los dos candidatos permiten formular tareas de clasificación y cuentan con documentación de procedencia.



El candidato utilizado en LAB01 tiene 569 observaciones y 30 variables predictoras, mientras que el conjunto de Pruebas Nacionales contiene 57,586 registros y 16 variables originales. Por tanto, ambos superan el requisito mínimo de 500 observaciones establecido para la selección del conjunto de LAB02.



El dataset de Pruebas Nacionales presenta una unidad de análisis agregada y requiere una auditoría específica de valores ausentes, duplicados, registros del año 2020, consistencia entre cantidades y diferencias entre variables de resultado.



Para evitar fuga de información, no se utilizan como predictores `Cantidad Promovidos` ni `Cantidad Aplazados`, debido a que ambas variables participan directamente en la construcción del target. También se excluyen las variables correspondientes a resultados de las áreas evaluadas, los identificadores del centro educativo y las variables de sexo por las razones documentadas en la auditoría.



El conjunto seleccionado permite formular una pregunta diferente a la utilizada en LAB01 y trabajar con información educativa real de la República Dominicana.



\---



\## Decisión de selección



\*\*Dataset seleccionado para LAB02:\*\* Estadísticas de Pruebas Nacionales, 2016-2024.



La selección se fundamenta en:



1\. La disponibilidad de una fuente institucional documentada.

2\. La existencia de una licencia explícita para datos abiertos.

3\. Un volumen de observaciones superior al mínimo establecido.

4\. La existencia de una unidad de análisis claramente identificable.

5\. La posibilidad de definir un target binario observable.

6\. La disponibilidad de variables que pueden utilizarse como predictores después de aplicar reglas de auditoría y prevención de fuga.

7\. La posibilidad de ejecutar el procesamiento y la clasificación utilizando recursos computacionales compatibles con CPU.

8\. La formulación de una pregunta de análisis diferente a la desarrollada en LAB01.



La selección no implica que el dataset de LAB01 sea inadecuado. Ambos conjuntos son técnicamente utilizables; el conjunto de Pruebas Nacionales se selecciona para LAB02 porque permite desarrollar el ejercicio sobre un dominio educativo distinto y aplicar explícitamente las etapas de auditoría, prevención de fuga, preprocesamiento y clasificación exigidas en la práctica.



\---



\## Fuentes



\- Portal de Datos Abiertos de la República Dominicana. \*\*Estadísticas de Pruebas Nacionales, 2016-2024\*\*.  

&#x20; https://datos.gob.do/dataset/c99df9fc-6d99-4cb3-8f2b-81d5753d51b7



\- Ministerio de Educación de la República Dominicana.  

&#x20; http://www.ministeriodeeducacion.gob.do/



\- scikit-learn. \*\*load\_breast\_cancer\*\*.  

&#x20; https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load\_breast\_cancer.html



\- UCI Machine Learning Repository. \*\*Breast Cancer Wisconsin (Diagnostic)\*\*.  

&#x20; https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic

