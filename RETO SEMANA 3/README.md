# Reto Semana 3: Analizador de Ventas

El tercer reto de la materia consiste en un programa que funciona como un analizador de transacciones de ventas leídas desde la terminal (stdin). Lo que hace el programa es recibir un archivo CSV con ventas individuales, las procesa para agruparlas por producto y genera un reporte consolidado. Sigue el patrón ETL: Extract (lee las ventas desde stdin), Transform (limpia líneas mal escritas, ignora datos no numéricos, agrupa por nombre de producto y calcula promedios e ingresos totales) y Load (imprime el reporte final ordenado de mayor a menor ingreso). El programa muestra:

1. Cuantas unidades se vendieron de cada producto
2. Cual fue el ingreso total por producto
3. Cual fue el precio promedio de venta

---

## Características de procesamiento
1. **Agrupación:** Todas las ventas que tengan el mismo nombre se suman en una sola fila.
2. **Cálculo:** Para cada producto se obtiene el total de unidades vendidas, el dinero total generado (ingreso) y el precio promedio de venta.
3. **Ordenamiento:** El reporte final siempre muestra primero los productos que generaron más dinero.
4. **Formato:** Los valores de dinero e ingresos se muestran con 2 decimales, mientras que las unidades se muestran como números enteros.
5. **Manejo de Errores:** Si una línea tiene letras donde debería haber números, está incompleta o tiene menos de 4 columnas, el programa la ignora y continúa con la siguiente.

---

## ¿Cómo usarlo?
### Desde un Archivo
-Windows (PowerShell):
```PowerShell
Get-Content tests/entrada1.txt | python main.py
```

-Windows (CMD):
```PowerShell
type tests/entrada1.txt | python main.py
```

-Linux / WSL / Mac:
```bash
python3 main.py < tests/entrada1.txt
```

-o:
```bash
cat tests/entrada1.txt | python3 main.py
```

### Guardar la Salida
Guardar resultado en un archivo nuevo:
```bash
python3 main.py < tests/entrada1.txt > reporte_final.csv
```

Ver el resultado y guardarlo al mismo tiempo:
```bash
python3 main.py < tests/entrada1.txt | tee reporte_final.csv
```

Entrada Manual (para pruebas rápidas):
```python
python3 main.py
```

---

## Ejemplo de entrada y salida:
**Entrada** (archivo `tests/entrada1.txt`):

```
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
2026-01-03,Laptop,1,14500.00
2026-01-04,Teclado,5,800.00
2026-01-05,Mouse,8,250.00
```
**Salida:**
```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44500.00,14833.33
Mouse,18,4500.00,250.00
Teclado,5,4000.00,800.00
```

---

## Autor: 
Domínguez Chimal Alan Eduardo
