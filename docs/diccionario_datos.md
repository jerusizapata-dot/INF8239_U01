\# Diccionario de datos



\## Identificación de la fuente



\- Dataset: Estadísticas de Pruebas Nacionales, 2016-2024.

\- Procedencia: Portal de Datos Abiertos de la República Dominicana / Ministerio de Educación.

\- Dominio: Educación.

\- Archivo utilizado: `data/raw/pruebas\_nacionales\_2016\_2024.csv`.

\- Registros originales: 57,586.

\- Variables originales: 16.

\- Unidad de análisis: registro agregado por período, convocatoria, centro educativo y nivel/modalidad.

\- Uso: académico y análisis de datos.

\- Momento de disponibilidad: información correspondiente a resultados agregados de las convocatorias de Pruebas Nacionales de los períodos incluidos en el archivo.



\## Variables



| Variable | Tipo | Significado | Unidad | Disponibilidad | Transformación prevista | Riesgo |

|---|---|---|---|---|---|---|

| Período | Numérica | Año/período de la evaluación | Año | Antes de la clasificación | Se conserva como variable numérica | Cambios metodológicos entre períodos |

| Convocatoria | Categórica | Convocatoria de la evaluación | Categoría | Antes de la clasificación | One-hot encoding | Valores ausentes |

| Regional | Categórica | Código de la regional educativa | Código | Antes de la clasificación | One-hot encoding | Es un identificador geográfico |

| Distrito | Categórica | Código del distrito educativo | Código | Antes de la clasificación | One-hot encoding | Es un identificador geográfico |

| Nivel/Modalidad | Categórica | Nivel o modalidad educativa | Categoría | Antes de la clasificación | One-hot encoding | Diferencias entre modalidades |

| Código de Centro | Identificador | Código del centro educativo | Código | Antes de la clasificación | Excluida del modelo | Riesgo de memorización |

| Nombre de Centro | Texto/identificador | Nombre del centro educativo | Texto | Antes de la clasificación | Excluida del modelo | Riesgo de identificación y memorización |

| Español | Numérica | Resultado agregado en Español | Puntaje | Resultado de la evaluación | Excluida del modelo | Posible fuga conceptual |

| Matemáticas | Numérica | Resultado agregado en Matemáticas | Puntaje | Resultado de la evaluación | Excluida del modelo | Posible fuga conceptual |

| Sociales | Numérica | Resultado agregado en Ciencias Sociales | Puntaje | Resultado de la evaluación | Excluida del modelo | Posible fuga conceptual |

| Naturales | Numérica | Resultado agregado en Ciencias de la Naturaleza | Puntaje | Resultado de la evaluación | Excluida del modelo | Posible fuga conceptual |

| Cantidad de estudiantes | Numérica | Cantidad total de estudiantes del registro | Estudiantes | Disponible en el registro | Se conserva y se escala | Puede presentar valores extremos |

| Cantidad Femenino | Numérica | Cantidad de estudiantes de sexo femenino | Estudiantes | Disponible en el registro | Excluida por redundancia | Alta correlación con el total |

| Cantidad masculino | Numérica | Cantidad de estudiantes de sexo masculino | Estudiantes | Disponible en el registro | Excluida por redundancia | Alta correlación con el total |

| Cantidad Promovidos | Numérica | Cantidad de estudiantes promovidos | Estudiantes | Resultado del proceso | Excluida; participa en el target | Fuga directa |

| Cantidad Aplazados | Numérica | Cantidad de estudiantes aplazados | Estudiantes | Resultado del proceso | Excluida; participa en el target | Fuga directa |



\## Construcción del target



El target utilizado para el modelado no representa el resultado individual de cada estudiante. Representa el \*\*predominio de promoción dentro de cada registro agregado\*\*.



\- Clase `1`: `Cantidad Promovidos > Cantidad Aplazados`.

\- Clase `0`: `Cantidad Promovidos < Cantidad Aplazados`.

\- Empates entre promovidos y aplazados: excluidos del modelado.



Se excluyen `Cantidad Promovidos` y `Cantidad Aplazados` de las variables predictoras porque ambas intervienen directamente en la construcción del target.



\## Reglas de limpieza aplicadas



1\. Se excluyen los registros del período 2020 por presentar un comportamiento estructuralmente diferente y ausencia de resultados normales.

2\. Se eliminan registros con valores faltantes en `Cantidad Promovidos` o `Cantidad Aplazados`.

3\. Se eliminan únicamente duplicados exactos.

4\. Se conservan registros que comparten una misma combinación de período, convocatoria, centro y modalidad cuando presentan información diferente.

5\. Se conservan únicamente registros donde:



&#x20;  `Cantidad de estudiantes = Cantidad Promovidos + Cantidad Aplazados`



6\. Se excluyen los empates entre promovidos y aplazados.

7\. Se excluyen variables de resultados y variables que generan fuga de información.

8\. Se excluyen las variables de sexo por redundancia con `Cantidad de estudiantes`.



\## Resultado del conjunto para modelado



Después de aplicar las reglas de limpieza y construcción del target:



\- Registros finales: \*\*46,992\*\*.

\- Variables predictoras: \*\*6\*\*.

\- Clase 0: \*\*9,763 registros (20.78%)\*\*.

\- Clase 1: \*\*37,229 registros (79.22%)\*\*.



\### Variables predictoras finales



\- `Período`

\- `Convocatoria`

\- `Regional`

\- `Distrito`

\- `Nivel/Modalidad`

\- `Cantidad de estudiantes`



\## Nota metodológica



Las variables categóricas se transforman mediante One-Hot Encoding y las variables numéricas se estandarizan dentro de un `Pipeline`. De esta manera, el preprocesamiento se ajusta únicamente con los datos de entrenamiento y se evita utilizar información del conjunto de prueba durante el entrenamiento.

