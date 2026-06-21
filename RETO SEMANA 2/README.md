# Reto Semana 2: Clasificador de Temperaturas

Este segundo reto consiste en un programa de procesamiento de datos meteorológicos que unifica reportes de ciudades globales. El programa lee datos en formatos mixtos (Celsius y Fahrenheit), los estandariza y los clasifica según su rango térmico.

---

## Características de Procesamiento

El script sigue estas reglas para limpiar los datos antes de generar el reporte:

* **Filtro de entrada**: Se usa `sys.stdin` para procesar el flujo de datos. El programa detecta la primera línea y la ignora para no intentar procesar los nombres de las columnas como números.
* **Estandarización**: No importa si la unidad viene como 'c' o 'C'; el código aplica `.upper()` y `.strip()` para normalizarla antes de decidir si aplica la conversión de Fahrenheit.
* **Conversión**: Se aplica la fórmula $(F - 32) * 5 / 9$ solo si se detecta la bandera `F`. Si la unidad es `C`, el valor pasa directo.
* **Manejo de errores**: 
    - Si una fila tiene menos de 3 columnas (datos incompletos), la salta.
    - Se usa un bloque `try-except` para atrapar valores que no son números (como 'abc' o símbolos) y descartar la línea sin que el programa se rompa.
* **Formateo de salida**: Al imprimir, se fuerza el uso de `: .1f` para asegurar que todas las temperaturas tengan exactamente un decimal.

---

## Tabla de Clasificación

El sistema utiliza los siguientes rangos para categorizar las temperaturas:

| Temperatura (°C) | Clasificación |
| :--- | :--- |
| < 0 | **Congelante** |
| 0 a 15 | **Frío** |
| 16 a 25 | **Templado** |
| 26 a 35 | **Cálido** |
| > 35 | **Extremo** |

---

## Instrucciones de Uso

### Generar datos de prueba
Para crear un archivo de entrada con 1000 registros aleatorios:
```bash
python3 generar_entrada.py 1000 > test/entrada.csv

```
### Ejecución del clasificador
Para procesar el archivo generado y obtener el reporte estandarizado, ejecuta el script principal redirigiendo la entrada y la salida:
```bash
python3 main.py < test/entrada.csv > test/reporte_final.csv

```

---

## Autor:
Domínguez Chimal Alan Eduardo
