# Reto Semana 10: StockMetrics Analyzer

Este décimo reto consiste en el desarrollo de un motor analítico modular optimizado para el procesamiento, auditoría y evaluación técnica de series de tiempo financieras utilizando Pandas Series. El objetivo principal es estructurar un pipeline eficiente que permita calcular métricas de rendimiento compuesto, modelar indicadores de dispersión dinámica (Bandas de Bollinger), aislar puntos críticos de inflexión en el mercado y compilar un sistema automatizado de señales de trading para la toma de decisiones financieras a gran escala.

---

## Arquitectura

El flujo de procesamiento y la organización de los componentes analíticos para el monitor de activos financieros se estructuran de la siguiente manera:

```text
RETO SEMANA 10/
├── reto_10_analizador_acciones.ipynb  # Motor principal de análisis y señales
├── README.md                          # Documentación del sistema
└── .gitignore                         # Archivos omitidos en el control de versiones
```

## Características de procesamiento

Para garantizar un rendimiento profesional y escalabilidad ante series históricas masivas de precios, el sistema se diseñó bajo las siguientes reglas de computación científica:

- **Cómputo vectorizado:** Uso exclusivo de métodos nativos de Pandas para calcular variaciones porcentuales logarítmicas y acumuladas en tiempo real, eliminando el overhead de iteraciones manuales.
- **Modelado de volatilidad dinámica:** Implementación de ventanas móviles (.rolling) para el cálculo de medias y desviaciones estándar, permitiendo la construcción adaptativa de Bandas de Bollinger ante fluctuaciones de mercado.
- **Algoritmo de señales condicionales:** Filtros optimizados mediante máscaras booleanas y vectorización para clasificar alertas de trading (Compra/Venta) y categorizar la estabilidad del activo sin penalizar la memoria del sistema.

## Especificación de variables procesadas

El motor financiero opera sobre estructuras unidimensionales (Pandas Series) indexadas por fechas, evaluando el comportamiento de las siguientes métricas clave:

| Variable | Unidad | Descripción y Criterio Estadístico |
|---|---|---|
| Precio de Cierre | Moneda ($) | Valor de registro diario del activo. Funciona como la serie base para cualquier transformación matemática posterior. |
| Media Móvil (SMA) | Moneda ($) | Indicador de tendencia central calculado sobre una ventana paramétrica móvil para suavizar el ruido del mercado. |
| Volatilidad Histórica | Porcentaje (%) | Desviación estándar móvil de los rendimientos, utilizada como el umbral de riesgo para clasificar la estabilidad del activo. |

## Estructura del reporte

Tras la consolidación del pipeline analítico, el bloque de integración condensa las métricas macro para la toma de decisiones sobre las acciones evaluadas:

- **Métricas de retorno:** Reporte consolidado de rendimientos totales, ganancias acumuladas y precios extremos (máximos y mínimos históricos).
- **Diagnóstico de tendencias:** Clasificación automatizada del comportamiento del mercado (Alcista, Bajista, Lateral) con base en la posición del precio respecto a sus soportes móviles.
- **Matriz de elertas técnicas:** Registro indexado de momentos de cruce de umbrales críticos para mitigar falsos positivos en órdenes de compra o venta.

## Funciones implementadas

```python
estadisticas_basicas(precios)        # precio actual, mín, máx, promedio, mediana, std, rango
calcular_rendimientos(precios)       # rendimiento diario en %
analisis_rendimientos(rendimientos)  # mejor/peor día, días positivos/negativos, volatilidad
media_movil(precios, ventana)        # media móvil simple
bandas_bollinger(precios, ...)       # banda superior, media e inferior
detectar_maximos_minimos(precios)    # máximos y mínimos locales
clasificar_tendencia(precios, ma)    # ALCISTA / BAJISTA / LATERAL
generar_senales_trading(ma_c, ma_l)  # COMPRA / VENTA / MANTENER
alertas_precio(rendimientos, umbral) # alertas de subida/caída
clasificar_volatilidad(std)          # BAJA / MEDIA / ALTA / MUY ALTA
generar_reporte_completo(...)        # reporte integrado de la acción
```

### Bonus

```python
calcular_rsi(precios)                # Índice de Fuerza Relativa
backtest_estrategia(precios, ...)    # simulación de estrategia de trading
```

## Cómo ejecutar

1. Abrir `reto_10_analizador_acciones.ipynb` en Jupyter Notebook o JupyterLab.
2. Seleccionar **Kernel → Restart & Run All**.
3. Verificar que todas las celdas se ejecuten sin errores y muestren los resultados.

## Autor:

Dominguez Chimal Alan Eduardo
