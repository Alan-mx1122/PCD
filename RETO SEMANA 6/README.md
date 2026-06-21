# Reto semana 6: Validador de códigos con expresiones regulares

Este sexto reto implementa un sistema automatizado para la clasificación y validación estricta de códigos corporativos (productos, envíos, empleados y facturas). La solución está desarrollada en Python y fundamentada en el uso de expresiones regulares (`re`) para optimizar los procesos de auditoría logística en la cadena de suministro.

---

## Estructura del Proyecto

El repositorio mantiene una organización clara y modular para separar el entorno productivo del ambiente de pruebas:

```text
RETO SEMANA 6/
├── .gitignore          # Archivos y cachés excluidos del control de versiones
├── README.md           # Documentación técnica del sistema
├── main.py             # Script principal de procesamiento por lotes (stdin -> stdout)
└── tests/              # Carpeta contenedora de datos de control
    ├── entrada.txt     # Set de datos con 1,000 registros de prueba
    └── salida.csv      # Reporte final generado en formato CSV estructurado

```

---

## Características de Procesamiento
* **Procesamiento de flujos**: El script está diseñado para leer desde la entrada estándar línea por línea. Esto permite procesar volúmenes masivos de datos consumiendo el mínimo de memoria RAM.
* **Mapeo dinámico**: En lugar de utilizar estructuras condicionales anidadas (if-elif densos), el código implementa un diccionario de funciones evaluadoras, lo que mejora la legibilidad, escalabilidad y eficiencia de ejecución del programa.
* **Tratamiento de líneas vacías**: El sistema descarta silenciosamente cualquier línea en blanco o que contenga únicamente espacios, evitando la generación de registros basura en la salida.

---

## Reglas de Validación
El sistema aplica dos filtros jerárquicos de negocio:
1. Detección de Tipo (Estructura General)
El tipo de código se asigna en función de su prefijo y máscara de caracteres:
producto: Cualquier combinación de 3 letras (mayúsculas o minúsculas) + - + 4 dígitos + - + 2 letras.
    *   envio: Debe iniciar estrictamente con el prefijo ENV- seguido de la máscara temporal y un consecutivo numérico.
    *   empleado: Debe iniciar estrictamente con el prefijo EMP- seguido de 3 letras y 4 dígitos.
    *   factura: Debe iniciar estrictamente con el prefijo FAC- seguido de una letra de serie y 6 dígitos.
    *   desconocido: Cualquier cadena que no cumpla con las estructuras anteriores.
2. Validación Estricta
Una vez detectado el tipo, se evalúan los siguientes criterios:
    * Productos: Los bloques de caracteres de la categoría (primeras 3 letras) y del país (últimas 2 letras) deben estar obligatoriamente en mayúsculas.
    *    Envíos: Los rangos cronológicos deben ser lógicos y válidos para la empresa: Año entre 2020 y 2030, Mes entre 01 y 12, Día entre 01 y 31.
    *   Empleados: El código de departamento debe pertenecer al catálogo autorizado: VEN, ADM, TEC, LOG, RHH. Además, el número secuencial de 4 dígitos no puede iniciar con cero (0).
    *   Facturas: La serie de facturación del segundo bloque debe ser una letra en mayúscula comprendida únicamente entre la A y la E.

---

## Especificaciones de Formatos
1. Entrada (stdin)
* Un código alfanumérico por línea.
* Codificación estándar de texto sin formato.
* Ejemplo:
    | Código de Entrada | 
    | :--- | :--- |
    | `ENV-2029-06-06-231413` | 
    | `EMP-VEN-0926` | 
    | `hog-4516-CO` |
    | `ELE-002-FR` |

2. Salida (stdout)
* Formato de texto plano estructurado como valores separados por comas (CSV).
* La primera línea contiene de manera obligatoria los encabezados: codigo,tipo,valido.
* Columnas de salida:
    * codigo: Cadena original recibida en la entrada.
    * tipo: Clasificación obtenida (producto, envio, empleado, factura o desconocido).
    * valido: Dictamen final (VALIDO o INVALIDO). Los tipos desconocido siempre serán INVALIDO.
* Ejemplo:
    | codigo | tipo | valido | 
    | :--- | :--- | :--- | :--- |
    | `ENV-2029-06-06-231413` | `envio` | **`VALIDO`** | 
    | `EMP-VEN-0926` | `empleado` | **`INVALIDO`** | 
    | `hog-4516-CO` | `producto` | **`INVALIDO`** | 
    | `ELE-002-FR` | `desconocido` | **`INVALIDO`** |

---

## Instrucciones de uso
1. Ejecución estándar y visualización en consola: Para procesar el archivo de pruebas y observar el resultado directamente en la pantalla de la terminal:
    ```bash
    python main.py < tests/entrada.txt
    ```

2. Redirección y almacenamiento de resultados: 
    ```bash
    python main.py < tests/entrada.txt > tests/salida.csv
    ```

3. Salida de Datos: El reporte final se generará en la carpeta test/ con el siguiente formato:
codigo,tipo,valido

---

## Autor: 
Domínguez Chimal Alan Eduardo