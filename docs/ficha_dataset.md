\# Ficha del dataset



\- Dominio: Educación y evaluación del rendimiento académico en la República Dominicana.

\- Unidad de análisis: Registro agregado de resultados de Pruebas Nacionales por período, convocatoria, centro educativo y nivel/modalidad.

\- Decisión: Identificar si en un registro agregado predomina la cantidad de estudiantes promovidos sobre la cantidad de estudiantes aplazados.

\- Target: Predominio de promoción. Clase 1 si Cantidad Promovidos > Cantidad Aplazados y clase 0 si Cantidad Promovidos < Cantidad Aplazados. Los empates se excluyen del modelado.

\- Error más costoso: Clasificar como predominio de promoción un registro donde realmente predominan los estudiantes aplazados, porque podría generar una interpretación excesivamente favorable del rendimiento observado.

\- Usuario: Analistas de datos, investigadores y responsables de análisis educativo que requieran explorar patrones agregados de promoción en los registros de Pruebas Nacionales.

