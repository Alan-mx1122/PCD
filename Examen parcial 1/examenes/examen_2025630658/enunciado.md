# Examen Parcial 1 - Programación para Ciencia de Datos

## Sistema de Control de Muestras de Laboratorio

**Matrícula:** `2025630658`
**Fecha límite de entrega:** (por definir)
**Valor:** 100 puntos

---

## Contexto

Un laboratorio de análisis clínicos recibe muestras con volúmenes registrados en onzas líquidas (equipos importados) y mililitros (equipos nacionales). Necesitan unificar a ml, clasificar muestras por tamaño y generar reportes por tipo de análisis.

---

## Datos de Entrada

El archivo `datos/muestras_lab.csv` contiene registros con las siguientes columnas:

| Columna | Tipo esperado | Descripción |
|---------|---------------|-------------|
| `id_muestra` | texto | Código de muestra |
| `paciente` | texto | Nombre del paciente |
| `volumen` | numérico (decimal) | Volumen de la muestra |
| `unidad` | texto (`fl_oz` o `ml`) | Unidad (fl_oz o ml) |
| `tipo_analisis` | texto | Tipo de análisis |

**Unidades posibles:** `fl_oz` (Onzas líquidas (fl_oz)) y `ml` (Mililitros (ml))

**Importante:** El archivo contiene aproximadamente 1000 registros. Algunos registros
contienen errores intencionales (valores no numéricos, unidades inválidas, columnas
faltantes o sobrantes, líneas vacías). Tu programa debe manejar estos casos sin
detenerse.

### Huella de integridad de los datos

El archivo de datos proporcionado tiene el siguiente hash SHA-256:

```
7a09c0758837336e25a6f89e48cfd9690a1a898e13d04ff56e8c6401693f079c
```

**No modifiques el archivo de datos.** Este hash se verificará automáticamente al
calificar tu examen. Si el hash no coincide, se considerará que los datos fueron
alterados y se penalizará la calificación.

> Para verificar el hash de tu archivo puedes usar:
> ```python
> import hashlib
> with open("datos/muestras_lab.csv", "r", encoding="utf-8") as f:
>     print(hashlib.sha256(f.read().encode("utf-8")).hexdigest())
> ```

---

## Reglas de Procesamiento

### 1. Lectura del archivo
Lee el archivo CSV desde `datos/muestras_lab.csv`. El archivo usa comas (`,`) como
separador. La primera línea es el encabezado con los nombres de las columnas.

**¿Cómo leerlo?** Abre el archivo con `open()`, lee todas las líneas, separa la
primera línea (header) del resto. Para cada línea de datos, usa `.split(",")` para
obtener los valores individuales.

### 2. Validación de cada fila
Para cada fila del archivo (después del header), verifica que sea válida. Una fila
es **inválida** y debe ignorarse si cumple cualquiera de estas condiciones:

- **Línea vacía:** la línea no contiene texto (o solo espacios en blanco)
- **Número incorrecto de columnas:** al separar por coma, no resultan exactamente
  5 valores
- **Valor no numérico:** el campo `volumen` no se puede convertir a `float`
  (usa `try/except ValueError`)
- **Unidad no reconocida:** el campo `unidad` no es ni `fl_oz` ni `ml`
  (la comparación es sensible a mayúsculas/minúsculas)

**Importante:** Tu programa no debe detenerse ni mostrar errores cuando encuentre
filas inválidas; simplemente las ignora y continúa con la siguiente.

### 3. Conversión de unidades
Para los registros válidos, convierte los valores que están en `fl_oz` a `ml`
usando la fórmula:

```
ml = fl_oz × 29.5735
```

En Python:
```python
ml = fl_oz * 29.5735
```

Los valores que **ya están en `ml`** se mantienen sin cambio alguno.

Después de la conversión, redondea el resultado a **1 decimal**
usando la función `round()`.

### 4. Clasificación
Clasifica cada registro según el valor **ya convertido** a `ml`:

| Categoría | Rango (ml) | Regla |
|-----------|------|-------|
| Micro | < 10.6 | `valor < 10.6` |
| Pequeña | 10.6 - 52.7 | `10.6 <= valor < 52.7` |
| Mediana | 52.7 - 151.3 | `52.7 <= valor < 151.3` |
| Grande | 151.3 - 349.3 | `151.3 <= valor < 349.3` |
| Extra grande | >= 349.3 | `valor >= 349.3` |


> **Convención de límites:** Los límites inferiores son **inclusivos** (`>=`) y los
> superiores son **exclusivos** (`<`), excepto en la última categoría donde solo hay
> límite inferior inclusivo.

### 5. Generación de archivos de salida

Tu programa debe generar **dos archivos CSV** en la carpeta `salidas/`. A continuación
se describe cada uno en detalle.

---

## Archivo de Salida 1: `salidas/reporte_detalle.csv`

Este archivo contiene **un registro por cada fila válida** del archivo de entrada,
con el valor ya convertido y su clasificación.

### Columnas del archivo

| # | Columna | Tipo | Descripción | Ejemplo |
|---|---------|------|-------------|---------|
| 1 | `id_muestra` | texto | ID original, copiado tal cual de la entrada | `MX-0001` |
| 2 | `paciente` | texto | Nombre original, copiado tal cual de la entrada | (varía) |
| 3 | `tipo_analisis` | texto | Grupo/categoría original | (varía) |
| 4 | `volumen_ml` | decimal | Valor convertido a ml, con 1 decimal | `37.5` |
| 5 | `tamano_muestra` | texto | Clasificación asignada según los umbrales | (varía) |

### Reglas del archivo
- **Primera línea (header):** `id_muestra,paciente,tipo_analisis,volumen_ml,tamano_muestra`
- **Ordenamiento:** ascendente por `id_muestra` (orden alfabético/numérico del ID)
- **Separador:** coma (`,`), sin espacios alrededor
- **Decimales:** los valores en `volumen_ml` deben tener exactamente
  1 decimal (usa f-string: `f"{valor:.1f}"`)
- **Sin filas inválidas:** solo aparecen registros que pasaron la validación

### Cómo generarlo paso a paso
1. Filtra solo los registros válidos (los que pasaron la validación del paso 2)
2. Para cada registro: convierte el valor (paso 3), clasifícalo (paso 4)
3. Almacena los resultados en una lista
4. Ordena la lista por ID ascendente
5. Escribe el header seguido de cada registro, una línea por registro

---

## Archivo de Salida 2: `salidas/reporte_resumen.csv`

Este archivo contiene **una fila por cada grupo** (`tipo_analisis`), con métricas
agregadas calculadas a partir de los registros válidos.

### Columnas del archivo

| # | Columna | Tipo | Descripción | Cómo calcularlo |
|---|---------|------|-------------|-----------------|
| 1 | `tipo_analisis` | texto | Nombre del grupo | La clave del diccionario de agrupación |
| 2 | `conteo` | entero | Cantidad de registros válidos en ese grupo | Contar cuántos registros pertenecen al grupo |
| 3 | `promedio` | decimal | Promedio del valor convertido, 1 decimal | Suma de valores / conteo |
| 4 | `maximo` | decimal | Valor máximo convertido, 1 decimal | El mayor valor del grupo |

### Reglas del archivo
- **Primera línea (header):** `tipo_analisis,conteo,promedio,maximo`
- **Ordenamiento principal:** descendente por `conteo` (el grupo con más registros primero)
- **Desempate:** si dos grupos tienen el mismo conteo, orden alfabético por `tipo_analisis`
- **Decimales:** `promedio` y `maximo` con exactamente 1 decimal
- **`conteo`** es un entero (sin decimales)

### Cómo generarlo paso a paso
1. Usa un **diccionario** para agrupar: la clave es el valor de `tipo_analisis`, el valor
   es otro diccionario con `conteo`, `suma` y `maximo`
2. Recorre todos los registros válidos (ya procesados en el detalle):
   - Si el grupo no existe en el diccionario, créalo con conteo=0, suma=0.0, maximo=-infinito
   - Incrementa el conteo, suma el valor convertido, actualiza el máximo si corresponde
3. Calcula el promedio: `promedio = suma / conteo`
4. Ordena por conteo descendente (y alfabético en caso de empate)
5. Escribe el header seguido de cada grupo

---

## Estructura del Proyecto Requerida

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
    ├── reporte_detalle.csv    # Generado por tu programa
    └── reporte_resumen.csv    # Generado por tu programa
```

### Descripción de cada archivo

**`main.py`** — Punto de entrada. Al ejecutar `python main.py` desde la raíz del
proyecto, debe:
1. Leer el archivo de datos usando funciones de `utils/io_helpers.py`
2. Validar cada fila usando funciones de `utils/validators.py`
3. Crear objetos `Muestra` para cada registro válido
4. Generar el reporte de detalle y escribirlo en `salidas/reporte_detalle.csv`
5. Generar el reporte de resumen y escribirlo en `salidas/reporte_resumen.csv`

**`models/muestra.py`** — Contiene la clase `Muestra` (ver sección siguiente).

**`utils/io_helpers.py`** — Contiene al menos:
- Una función para **leer** el archivo CSV y retornar las filas como lista de listas o diccionarios
- Una función para **escribir** un archivo CSV a partir de una lista de datos

**`utils/validators.py`** — Contiene al menos:
- Una función para **validar** si una fila del CSV es válida (número correcto de
  columnas, valor numérico, unidad reconocida)
- Debe retornar `True`/`False` o una tupla `(es_valido, mensaje_error)`

---

## Clase Requerida: `Muestra`

La clase `Muestra` en `models/muestra.py` debe incluir:

- **`__init__(self, ...)`**: Recibe y almacena como atributos: `id_muestra`,
  `paciente`, el valor ya convertido a ml, y `tipo_analisis`
- **`clasificar(self)`**: Método que retorna un string con la clasificación según
  los umbrales definidos (ej: `"Micro"`, `"Pequeña"`, etc.)
- **`__str__(self)`**: Retorna una representación legible para el usuario
  (ej: `"MX-0001 - NombreEjemplo (tipo_analisis: GrupoEjemplo) - 37.5 ml"`)
- **`__repr__(self)`**: Retorna una representación técnica para depuración
  (ej: `"Muestra(id='MX-0001', valor=37.5, clase='Normal')"`)

---

## Ejemplo

### Entrada (primeras filas de `datos/muestras_lab.csv`):
```csv
id_muestra,paciente,volumen,unidad,tipo_analisis
MX-0001,Mariana Rosas,8.52,fl_oz,Hematología
MX-0002,Iván Molina,310.37,ml,Hematología
MX-0003,Jorge Montes,190.32,ml,Microbiología
MX-0004,Miguel Sánchez,217.76,ml,Inmunología
MX-0005,Fernanda Lara,46.46,ml,Química Sanguínea
```

### Salida detalle esperada (`salidas/reporte_detalle.csv`):
```csv
id_muestra,paciente,tipo_analisis,volumen_ml,tamano_muestra
MX-0001,Mariana Rosas,Hematología,252.0,Grande
MX-0002,Iván Molina,Hematología,310.4,Grande
MX-0003,Jorge Montes,Microbiología,190.3,Grande
MX-0004,Miguel Sánchez,Inmunología,217.8,Grande
MX-0005,Fernanda Lara,Química Sanguínea,46.5,Pequeña
```

### Salida resumen esperada (`salidas/reporte_resumen.csv`):
```csv
tipo_analisis,conteo,promedio,maximo
Química Sanguínea,124,308.6,596.9
Coagulación,124,290.3,596.9
Hematología,120,299.3,599.2
Inmunología,120,275.1,587.6
Hormonas,120,295.6,592.9
```

---

## Criterios de Evaluación

| Criterio | Puntos | Detalle |
|----------|--------|---------|
| Estructura del proyecto | 15 | Carpetas, archivos, `__init__.py`, imports correctos |
| Clase `Muestra` | 20 | `__init__`, `clasificar()`, `__str__`, `__repr__` |
| Validación de datos | 10 | Manejo correcto de filas inválidas |
| Conversión de unidades | 15 | Fórmula correcta, precisión decimal |
| Clasificación | 10 | Umbrales correctos, categorías asignadas |
| Agrupación y métricas | 15 | Conteo, promedio, máximo por grupo |
| Formato de salida | 10 | CSVs con columnas, orden y formato correctos |
| Git | 5 | Mínimo 5 commits descriptivos, `.gitignore` |
| **Total** | **100** | |

> **Nota:** Se verificará automáticamente que el hash SHA-256 del archivo de datos
> coincida con `7a09c0758837336e25a6f89e48cfd9690a1a898e13d04ff56e8c6401693f079c`. Si el archivo fue modificado, se aplicará una
> penalización.

---

## Instrucciones de Entrega

1. Crea un repositorio en GitHub llamado `examen1_pcd`
2. Desarrolla tu solución siguiendo la estructura indicada
3. Asegúrate de que tu programa funciona ejecutando: `python main.py`
4. Tu programa debe leer de `datos/muestras_lab.csv` y escribir en `salidas/`
5. Haz **mínimo 5 commits** con mensajes descriptivos
6. Incluye un `.gitignore` apropiado
7. **NO modifiques** el archivo `datos/muestras_lab.csv` (se verificará su integridad)
8. Entrega el enlace a tu repositorio antes de la fecha límite

## Restricciones

- **NO** uses pandas, numpy ni librerías externas (solo biblioteca estándar de Python)
- **NO** copies código de otros compañeros (cada examen tiene datos y umbrales únicos)
- **NO** modifiques el archivo de datos proporcionado
- Tu código debe funcionar con **cualquier** archivo que siga el formato descrito,
  no solo con los datos proporcionados
