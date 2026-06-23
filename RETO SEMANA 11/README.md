# Reto Semana 11: Sistema de Gestión de Calificaciones

Este reto consiste en el diseño e implementación de un sistema modular de control escolar y analítica académica optimizado para el procesamiento de estructuras bidimensionales utilizando Pandas DataFrames. El objetivo es consolidar un pipeline robusto que permita la ingesta de registros estudiantiles y actas de evaluación, la ejecución de uniones relacionales complejas, el cálculo de métricas de rendimiento por cohorte y la identificación automatizada de alumnos en situación de riesgo académico.

---

## Arquitectura

El flujo de procesamiento y la organización de los componentes del sistema de gestión de calificaciones se estructuran de la siguiente manera:

```text
RETO SEMANA 11/
├── reto_11_gestor_estudiantes.ipynb # Motor analítico y pipeline de datos
├── README.md                        # Documentación técnica del sistema
├── .gitignore                       # Archivos excluidos del control de versiones
├── kardex_estudiante.csv            # Reporte individual en formato estructurado
└── kardex_estudiante.json           # Reporte individual en formato semiestructurado
```

---

## Características de procesamiento

Para garantizar un rendimiento profesional y escalabilidad ante bases de datos masivas de Control Escolar, el sistema se diseñó bajo las siguientes reglas de computación científica:

**Consolidación relacional** Uso exclusivo de uniones vectorizadas (`.merge`) para vincular los catálogos de alumnos con sus respectivas asignaturas, mitigando la duplicidad de memoria.

**Agregación multidimensional:** Implementación de agrupamientos optimizados (`.groupby`) y funciones de agregación compuesta (`.agg`) para calcular estadísticas descriptivas (medias, desviaciones y aprobaciones) por cohorte y periodo académico en una sola pasada de ejecución.

**Aislamiento de perfiles de piesgo:** Algoritmos de filtrado basados en lógica booleana indexada para identificar promedios deficientes e índices críticos de reprobación, clasificando de forma condicional a los alumnos vulnerables sin penalizar los tiempos de cómputo.

---

## Especificación de variables procesadas

El motor académico opera sobre estructuras bidimensionales integradas, evaluando el comportamiento de las siguientes métricas clave:

| Variable | Unidad | Descripción y Criterio Estadístico |
|---|---|---|
| Calificación | Escalar (0-100) | Nota numérica por asignatura. Se utiliza para determinar los estatus de acreditación y promedios generales. |
| Promedio General | Flotante | Métrica acumulada calculada mediante la media aritmética por boleta, filtrando valores fuera de rango o registros huérfanos. |
| Índice de Riesgo | Alerta / Estatus | Variable categórica generada de forma condicional cuando un alumno acumula múltiples asignaturas reprobadas o promedios críticos. |

---

## Estructura del Reporte Académico Completo

Tras la ejecución del pipeline relacional, el bloque de integración condensa los indicadores institucionales:

**Métricas de aprovechamiento:** Reporte consolidado de promedios por unidad de aprendizaje y tasas de rendimiento general por semestre.

**Auditoría de vulnerabilidad:** Listado priorizado de estudiantes en situación de riesgo para facilitar la asignación automatizada de tutorías preventivas.

**Pipeline de exportación:** Serialización dinámica de estructuras hacia formatos portables (CSV/JSON) manteniendo la integridad relacional de los identificadores únicos (boletas).

---

## Funciones implementadas

### Parte 1 — Carga y exploración
```python
cargar_datos()          # → (df_estudiantes, df_calificaciones, df_materias)
info_general(...)       # totales, semestres y materias con registros
validar_datos(...)      # nulos y calificaciones fuera de rango
```

### Parte 2 — Consultas y filtros
```python
buscar_estudiante(...)        # por boleta, nombre (parcial) o semestre
obtener_kardex(...)           # kardex completo con promedios y créditos
filtrar_por_rendimiento(...)  # estudiantes por rango de promedio
```

### Parte 3 — Cálculos y estadísticas
```python
calcular_promedio_materia(...)    # estadísticas por materia
ranking_estudiantes(...)          # top N por promedio
estadisticas_por_semestre(...)    # agregaciones por semestre
```

### Parte 4 — Riesgo y reportes
```python
identificar_estudiantes_riesgo(...)  # criterios de bajo promedio / reprobadas
generar_reporte_academico(...)       # reporte integrado
exportar_kardex(...)                 # exporta a CSV o JSON
```

### Bonus
```python
predecir_riesgo_proximo_semestre(...)  # tendencia decreciente de calificaciones
comparar_estudiantes(...)              # comparación de dos estudiantes
```

---

## Cómo ejecutar

1. Abrir `reto_11_gestor_estudiantes.ipynb` en Jupyter Notebook o JupyterLab.
2. Seleccionar **Kernel → Restart & Run All**.
3. Verificar que todas las celdas se ejecuten sin errores y muestren los resultados.
4. Al ejecutarse, se generan los archivos de kardex en CSV y JSON.

---

## Autor

Domínguez Chimal Alan Eduardo
