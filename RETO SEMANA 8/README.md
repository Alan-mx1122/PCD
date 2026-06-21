# Reto Semana 8: MeteoSense Analytics

Este octavo reto consiste en el desarrollo de un script de análisis numérico optimizado para procesar flujos de datos ambientales provenientes de una red de sensores distribuidos en la Ciudad de México. El objetivo principal es estructurar un flujo modular que permita auditar la calidad de la información, aislar comportamientos anómalos y compilar métricas agregadas de manera eficiente.

---

## Arquitectura

El flujo de trabajo y la organización de los módulos de análisis para la red meteorológica se estructuran de la siguiente manera:

```text
RETO SEMANA 8/
├── reto_08_metricas_sensores.ipynb  # Cuaderno principal con el motor de análisis
├── README.md                         # Documentación del sistema
└── .gitignore                        # Archivos omitidos en el control de versiones
```

## Características de procesamiento

Para garantizar que el sistema sea robusto, escalable y con rendimiento profesional ante matrices masivas de datos, se implementaron las siguientes reglas de diseño:

- **Procesamiento Estadístico Tolerante a Fallos:** Uso exclusivo de operaciones vectorizadas y manejo explícito de valores ausentes (NaN) mediante la librería NumPy para garantizar consistencia sin penalizar el rendimiento con loops iterativos.
- **Clasificación Bioclimática Automatizada:** Segmentación multidimensional de registros en tiempo real mediante máscaras booleanas basadas en el cálculo del Índice de Confort Térmico (ICT).
- **Detección Dinámica de Anomalías:** Aislamiento y conteo automático de registros que superan los umbrales de tolerancia estadística estipulados por el criterio de dispersión estándar ($\mu \pm 2\sigma$).

## Especificación de variables procesadas

El motor numérico procesa matrices tridimensionales estructuradas bajo los ejes (estaciones, días, horas). Cada variable cuenta con sus propios criterios de control:

| Variable | Unidad | Descripción y Comportamiento Esperado |
|---|---|---|
| Temperatura | °C | Oscilación térmica típica entre 10°C y 35°C, afectada por ciclos diurnos/nocturnos simulados. |
| Humedad Relativa | % | Intervalos restringidos mediante acotamiento dinámico (clip) dentro del rango válido de [20%, 95%]. |
| Dióxido de Carbono (CO2) | ppm | Concentración base por zona urbana con picos paramétricos inducidos en horarios de alta afluencia vehicular. |

## Estructura del reporte

Tras la consideración y el filtrado de las matrices de datos, el bloque bonus condensa los indicadores macro de la red de monitoreo en la Ciudad de México:

- **Estadísticos de Control:** Promedios integrales de las variables y conteo de pérdidas de sincronización de datos (valores faltantes NaN).
- **Rankings de Estaciones:** Identificación de extremos locales para clasificar las zonas más cálidas, húmedas o con mejor calidad de aire del entorno.
- **Patrones Horarios Críticos:** Detección exacta de las horas del día que registran mayor degradación ambiental y estrés térmico acumulado.

## Cómo ejecutar

1. Abrir `reto_08_metricas_sensores.ipynb` en Jupyter Notebook o JupyterLab.
2. Seleccionar **Kernel → Restart & Run All**.
3. Verificar que todas las celdas se ejecuten sin errores y muestren los resultados.

## Autor:

Domínguez Chimal Alan Eduardo
