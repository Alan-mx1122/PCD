# Reto Semana 9: SecureBank Fraud Detection

Este noveno reto consiste en el desarrollo de un motor estadístico optimizado para el análisis de riesgos y detección de anomalías en flujos de transacciones financieras dentro de un entorno bancario digital. El objetivo principal es estructurar un pipeline modular con NumPy para auditar patrones de gasto, aislar potenciales fraudes mediante criterios robustos de dispersión (IQR) y clasificar alertas de alta prioridad mediante puntuaciones estandarizadas (Z-Score).

---

## Arquitectura

El flujo de procesamiento y la organización de los módulos de análisis para la detección de fraudes bancarios se estructuran de la siguiente manera:

```text
RETO SEMANA 9/
├── reto_09_fraud_detection.ipynb  # Cuaderno principal con el motor de análisis
├── README.md                      # Documentación del sistema
└── .gitignore                     # Archivos omitidos en el control de versiones
```

## Características de procesamiento

Para garantizar un rendimiento óptimo ante matrices de transacciones masivas, el script se diseñó bajo las siguientes reglas de computación científica:

- **Filtrado Multidimensional Avanzado:** Segmentación de transacciones y cómputo de límites críticos por categoría mercantil sin recurrir a iteraciones costosas, optimizando el uso de memoria.
- **Aislamiento Estadístico de Outliers (IQR):** Detección de desviaciones en compras diarias mediante el rango intercuartílico ($IQR$) para controlar la dispersión central de forma robusta ante valores extremos.
- **Cómputo Normalizado de Riesgo (Z-Score):** Estandarización de anomalías basada en desviaciones estándar ($\mu \pm 3\sigma$) para aislar e identificar transacciones atípicas de alta prioridad (montos sospechosamente altos o pruebas de tarjeta).

## Especificación de variables procesadas

El motor numérico procesa matrices consolidadas que agrupan los montos transaccionales por categoría de comercio, evaluando su comportamiento frente a las siguientes métricas:

| Variable | Unidad | Descripción y Comportamiento Esperado |
|---|---|---|
| Monto de Transacción | Pesos ($) | Flujo monetario registrado en comercios. Se evalúan mínimos y máximos absolutos para auditar la dispersión. |
| Rango Intercuartílico (IQR) | Escalar | Medida de dispersión estadística del 50% central de los datos, utilizada para establecer las barreras de corte de fraude. |
| Z-Score | Desviaciones | Puntuación estándar que mide la distancia de un monto individual respecto a la media de su categoría de comercio. |

## Estructura del Reporte de Transacciones Sospechosas

Tras la consolidación y el filtrado de las matrices de datos, el bloque final condensa los indicadores macro de riesgo para SecureBank:

- **Estadísticos de Control:** Resumen global de medias, medianas y desviaciones estándar por tipo de comercio para auditar la salud del ecosistema financiero.
- **Detección Cruzada de Fraude:** Cruce de alertas de ambos métodos estadísticos (IQR y Z-Score) para clasificar incidentes de alta prioridad y reducir falsos positivos.
- **Análisis de Correlación Intermercantil:** Matriz de dependencias calculada para evaluar la similitud de comportamientos de consumo entre las distintas categorías de comercio analizadas.

## Cómo ejecutar

1. Abrir `reto_09_detector_anomalias.ipynb` en Jupyter Notebook o JupyterLab.
2. Seleccionar **Kernel → Restart & Run All**.
3. Verificar que todas las celdas se ejecuten sin errores y muestren los resultados.

## Autor:

Dominguez Chimal Alan Eduardo

