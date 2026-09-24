\# Comparación de candidatos



\## Candidato A — Dataset utilizado en LAB01



\*\*Breast Cancer Wisconsin Diagnostic\*\*



\- Procedencia: `sklearn.datasets`, basado en el Wisconsin Diagnostic Breast Cancer dataset.

\- Dominio: Salud / clasificación de diagnóstico.

\- Filas: 569.

\- Variables predictoras: 30 características numéricas.

\- Target: diagnóstico del tumor, con dos clases.

\- Ausentes: no presenta valores ausentes en la versión utilizada.

\- Licencia/procedencia: dataset distribuido a través de scikit-learn para fines de aprendizaje y experimentación.

\- Riesgo de fuga: bajo, siempre que las variables utilizadas correspondan exclusivamente a características disponibles para la clasificación y el target permanezca separado.

\- Uso en LAB01: clasificación binaria mediante SVM.



\## Candidato B — Dataset seleccionado para LAB02



\*\*Estadísticas de Pruebas Nacionales, 2016-2024\*\*



\- Procedencia: Portal de Datos Abiertos de la República Dominicana / Ministerio de Educación.

\- Dominio: Educación.

\- Filas: 57,586.

\- Columnas: 16.

\- Target tentativo: predominio de estudiantes promovidos frente a estudiantes aplazados.

\- Ausentes: existen valores ausentes, principalmente asociados a los resultados y a la convocatoria.

\- Riesgo de fuga: alto en las variables que representan resultados de las pruebas o cantidades utilizadas directamente para construir el target.

\- Tratamiento: se excluyen las variables de resultados y las variables que definen directamente el target. También se excluyen identificadores de centro y variables redundantes.

\- Uso en LAB02: clasificación binaria de registros agregados de resultados educativos.



\## Tabla comparativa



| Criterio | Candidato A: Breast Cancer Wisconsin | Candidato B: Pruebas Nacionales |

|---|---|---|

| Procedencia | scikit-learn / Wisconsin Diagnostic Breast Cancer | Portal de Datos Abiertos / MINERD |

| Dominio | Salud | Educación |

| Filas | 569 | 57,586 |

| Columnas | 30 predictoras + target | 16 |

| Target | Diagnóstico binario | Predominio de promoción |

| Clases | 2 | 2 |

| Ausentes | No | Sí |

| Riesgo de fuga | Bajo | Requiere auditoría y exclusiones |

| Unidad de análisis | Paciente/muestra diagnóstica | Registro agregado educativo |

| Compatibilidad con CPU | Alta | Alta, con preprocesamiento adecuado |



\## Criterios de aceptación



Ambos candidatos cumplen el requisito mínimo de cantidad de observaciones y permiten una tarea de clasificación binaria.



El dataset de Pruebas Nacionales presenta una unidad de análisis agregada y requiere un tratamiento específico de los registros de 2020, valores ausentes, duplicados, inconsistencias entre cantidades y diferencias en las variables de resultado.



Para evitar fuga de información, no se utilizan como predictores `Cantidad Promovidos` ni `Cantidad Aplazados`, porque ambas variables participan directamente en la construcción del target. También se excluyen las variables de resultados de las áreas evaluadas, los identificadores del centro educativo y las variables de sexo por redundancia con la cantidad total de estudiantes.



El dataset de Pruebas Nacionales fue seleccionado para LAB02 porque permite formular una pregunta de análisis distinta a la de LAB01, cuenta con un volumen suficiente de observaciones y ofrece una problemática real de clasificación sobre información educativa agregada.



\## Decisión de selección



\*\*Dataset seleccionado para LAB02:\*\* Estadísticas de Pruebas Nacionales, 2016-2024.



La selección se fundamenta en la disponibilidad de documentación, el volumen de observaciones, la existencia de variables observables antes del proceso de clasificación y la posibilidad de construir un problema de clasificación reproducible después de aplicar las reglas de auditoría y prevención de fuga.

