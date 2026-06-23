# Reto semana 12: SoundWave Analytics Dashboard

Este reto consiste en el diseño e implementación de un motor analítico avanzado y modular hecho para la consolidación, fusión y reestructuración multidimensional de flujos de datos provenientes de la plataforma de streaming "SoundWave". El objetivo es integrar múltiples DataFrames independientes mediante uniones complejas, evaluar patrones de consumo de usuarios mediante métricas agregadas por cohorte y generar reportes ejecutivos estructurados en formato de matriz para la toma de decisiones estratégicas en el negocio de la música digital.

---

## Arquitectura

El pipeline de datos y la organización de los módulos analíticos para la plataforma de streaming se distribuyen bajo el siguiente esquema:

```text
RETO SEMANA 12/
├── reto_12_analizador_streaming.ipynb  # Motor analítico y transformaciones avanzadas
├── README.md                           # Documentación del sistema
└── .gitignore                          # Archivos omitidos en el control de versiones
```

---

## Procesamiento y mdulos desarrollados

En el cuaderno se implementaron las siguientes 5 etapas de procesamiento avanzado y el bloque analítico de cierre:

- **Parte 1 (`pd.concat`):** Consolidación eficiente de logs mensuales fragmentados (`streams_enero` y `streams_febrero`) en una única estructura maestra sin perder consistencia en los índices.

- **Parte 2 (`pd.merge`):** Fusión relacional multitabla vinculando los registros consolidados con los catálogos de usuarios y canciones mediante sus respectivas llaves primarias (`user_id`, `song_id`).

- **Parte 3 (`.groupby`):** Computación de métricas acumuladas por artista y género musical para aislar el volumen total de streams y el conteo de oyentes únicos.

- **Parte 4 (`.pivot_table`):** Construcción de matrices dinámicas cruzadas para evaluar las preferencias de géneros musicales según el tipo de suscripción (`Premium` vs `Free`).

- **Parte 5 (`.melt` — BONUS):** Reestructuración de reportes anchos (género × país) hacia formatos largos optimizados para series temporales y herramientas de BI.

- **Desafío Final:** Análisis integral de consumo combinando filtros booleanos avanzados y ordenamientos jerárquicos para identificar las canciones líderes, el género con mejor engagement, el país con mayor volumen de streams, la comparativa Premium vs Free y el artista con mayor crecimiento mensual.

---

## Especificación de variables clave

| Variable | Descripción |
|---|---|
| `user_id` / `song_id` | Identificadores relacionales para los cruces de tablas. |
| `streams_count` | Métrica numérica usada para los agregados de popularidad. |
| `subscription_type` | Variable categórica de segmentación de mercado. |

---

## Cómo ejecutar

1. Abrir `reto_12_analizador_streaming.ipynb` en Jupyter Notebook o JupyterLab.
2. Seleccionar **Kernel → Restart & Run All**.
3. Verificar que todas las celdas se ejecuten sin errores y muestren los resultados.

---

## Autor

Dominguez Chimal Alan Eduardo
