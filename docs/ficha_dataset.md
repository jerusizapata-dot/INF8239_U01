\# Ficha del dataset



\- \*\*Dominio:\*\* Educación y evaluación del rendimiento académico en la República Dominicana.



\- \*\*Unidad de análisis:\*\* Registro agregado de resultados de Pruebas Nacionales correspondiente a un período, convocatoria, centro educativo y nivel/modalidad.



\- \*\*Decisión apoyada:\*\* Identificar si, en un registro agregado, predomina la cantidad de estudiantes promovidos sobre la cantidad de estudiantes aplazados.



\- \*\*Target:\*\* Predominio de promoción. Se define la clase 1 cuando `Cantidad Promovidos > Cantidad Aplazados` y la clase 0 cuando `Cantidad Promovidos < Cantidad Aplazados`. Los registros donde ambas cantidades son iguales se excluyen del modelado para evitar asignar arbitrariamente una clase a un empate.



\- \*\*Tipo de tarea:\*\* Clasificación binaria supervisada.



\- \*\*Momento de predicción:\*\* La clasificación se plantea utilizando únicamente variables disponibles en el registro antes de considerar las cantidades de promovidos y aplazados y los resultados de las áreas evaluadas. Las variables utilizadas directamente para construir el target no se incorporan como predictores.



\- \*\*Error más costoso:\*\* Clasificar como predominio de promoción un registro donde realmente predominan los estudiantes aplazados. Este error podría producir una interpretación excesivamente favorable del rendimiento observado en el registro agregado.



\- \*\*Usuario:\*\* Analistas de datos, investigadores y responsables de análisis educativo que requieran explorar patrones agregados de promoción en los registros de Pruebas Nacionales.



\- \*\*Propósito del análisis:\*\* Desarrollar un modelo de clasificación reproducible que permita estudiar la separación entre registros con predominio de promoción y registros con predominio de aplazamiento, aplicando auditoría de datos, prevención de fuga de información y evaluación mediante métricas de clasificación.

