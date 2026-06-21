# Examen parcial 1

---

## Sistema de Control de Muestras de Laboratorio

El proyecto consiste en un sistema para procesar registros de muestras de un laboratorio de análisis clínicos. El programa se encarga de validar la integridad de cada registro, después estandariza (unifica) los volúmenes de las muestras (pasando de onzas líquidas a mililitros) y clasifica las muestras según su tamaño final para generar dos reportes CSV por tipo de análisis.

---

## Características de procesamiento
* **Limpieza de datos basura:** Filtra registros con valores no numéricos, unidades inválidas o columnas incompletas.
* **Estandarización:** Unifica las muestras de `fl_oz` a `ml` usando el factor de conversión 29.5735.
* **Clasificación:** Asigna categorías (Micro, Pequeña, Mediana, Grande, Extra grande) basándose en los umbrales definidos por nuestra variante del laboratorio.
* **Generación de Reportes:** 
   * `reporte_detalle.csv`: Este archivo contiene un registro por cada fila válida del archivo de entrada, con el valor ya convertido y su clasificación.
    * `reporte_resumen.csv`: Este archivo contiene una fila por cada grupo (`tipo_analisis`), con métricas agregadas calculadas a partir de los registros válidos.

---

## Estructura del proyecto

```
examen_2025630658/
├── main.py                    # Punto de entrada: orquesta todo el proceso
├── models/
│   ├── __init__.py            # Puede estar vacío o exportar la clase
│   └── muestra.py        # Definición de la clase Muestra
├── utils/
│   ├── __init__.py            # Puede estar vacío o exportar funciones
│   ├── io_helpers.py          # Funciones para leer CSV y escribir reportes
│   └── validators.py          # Funciones para validar filas del CSV
├── datos/
│   └── muestras_lab.csv      # Archivo de entrada (proporcionado, NO modificar)
└── salidas/
    ├── reporte_detalle.csv    # Generado por el programa
    └── reporte_resumen.csv    # Generado por el programa
```

---

## ¿Cómo usarlo?

1. Primero se debe verificar que el archivo de entrada esté en la ruta `datos/muestras_lab.csv`.
2. Ejecución
    * **Ejecución estándar:**
    Después, desde la terminal, ubícarse en la carpeta `examen_2025630658` y ejecutar:
        ```bash
        python3 main.py
        ```
    * **Para ejecutar el proceso usando redirección de entrada:**
        -Linux/Mac:
        ```bash
        python3 main.py < datos/muestras_lab.csv
        ```

3.  Los resultados se generarán automáticamente en la carpeta `salidas`.

---

## Autor:
* **Elaboró:** Domínguez Chimal Alan Eduardo

* **Matrícula:** 2025630658

* **Materia:** Programación para Ciencia de Datos

