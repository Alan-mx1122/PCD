# Reto semana 4: Sistema de inventario modular

Este cuarto reto consiste en una herramienta de gestión de suministros diseñada bajo un esquema modular. Se busca procesar inventarios tecnológicos, validar la integridad de los datos y generar reportes de reabastecimiento priorizados.

---

## Arquitectura
El sistema está organizado en módulos para facilitar su mantenimiento y escalabilidad, siguiendo el patrón ETL (Extract, Transform, Load):

```text
reto_semana_04/
├── main.py                    # Punto de entrada
├── README.md                  # Documentación
├── .gitignore                 # Archivos a ignorar
│
├── models/                    # Clases de dominio
│   ├── __init__.py            
│   └── producto.py            # Clase Producto
│
├── utils/                     # Utilidades
│   ├── __init__.py            
│   ├── io.py                  # Funciones de lectura/escritura
│   └── validators.py          # Funciones de validación
│
├── data/                      # Datos de entrada
│   └── inventario.csv         
│
└── outputs/                   # Resultados
    └── reporte_inventario.csv 

```

---

## Características de procesamiento
Para garantizar que el sistema sea robusto y profesional, se implementaron las siguientes reglas:
* **Validación modular**: Se verifica que cada registro cuente con las 6 columnas requeridas. Se descartan líneas con precios o stocks no numéricos.
* **Gestión de dtock**: El sistema identifica automáticamente productos cuyo stock es inferior al mínimo permitido.
* **Priorización de compra**: El reporte de salida se ordena de forma descendente según las unidades faltantes, permitiendo al usuario ver qué urge comprar primero.

---

## Especificación de entrada
El sistema procesa archivos en formato CSV ubicados en `data/inventario.csv`. Cada registro debe contener exactamente 6 columnas:

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| **sku** | String | Identificador único del producto. |
| **nombre** | String | Nombre comercial del artículo. |
| **categoria** | String | Clasificación (Electrónica, Accesorios, etc.). |
| **precio** | Float | Precio unitario (debe ser mayor o igual a 0). |
| **stock** | Int | Cantidad física disponible en almacén. |
| **stock_minimo** | Int | Umbral de alerta para reabastecimiento. |

## Especificación de salida
Tras la validación y el análisis, el sistema genera un reporte en `outputs/reporte_inventario.csv`. Este archivo incluye los productos que requieren compra urgente, ordenados de mayor a menor prioridad (por unidades faltantes):

| Columna | Descripción |
| :--- | :--- |
| **sku** | Identificador del producto. |
| **nombre** | Nombre del producto. |
| **categoria** | Clasificación del producto. |
| **stock_actual** | Cantidad que queda en almacén. |
| **stock_minimo** | El límite que disparó la alerta. |
| **unidades_faltantes** | Diferencia exacta para alcanzar el stock mínimo. |
| **valor_inventario** | Valor monetario del stock actual (Precio * Stock). |


---

## Instrucciones de uso
1. **Generación de datos**: Para generar un archivo de inventario con errores aleatorios para probar la robustez de los validadores:
    ```bash
    python3 generar_entrada.py 500 10 > data/inventario.csv
    ```
2. **Ejecución del sistema**: Desde la raíz del proyecto, ejecutar el orquestador principal:
    ```bash
    python3 main.py
    ```

3. **Salida de Datos**: El reporte final se generará en la carpeta outputs/ con el siguiente formato:
sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario

---

## Autor: 
Domínguez Chimal Alan Eduardo