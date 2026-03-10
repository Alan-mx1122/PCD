# Reto Semana 1: Calculadora de sumas

El primer reto de la materia consiste en una calculadora que lee datos desde la terminal (stdin). Lo que hace es recibir líneas de texto con números separados por comas, los limpia de cualquier "basura" (como letras o símbolos) y luego los suma. El programa sigue el patrón ETL: Extract (lee los datos de alguna fuente), Transform (limpia datos sucios que contienen caracteres no válidos, espacios extra o líneas vacías, y trunca los decimales) y Load (imprime los resultados en pantalla).

---

## Características de procesamiento
1. Si la línea no tiene nada: El programa imprime un 0.
2. Si hay decimales: El programa quita los decimales (no los redondea, los trunca) antes de sumar. Por ejemplo, 1.9 se convierte en 1.
3. Si hay letras o símbolos: El código los ignora y se queda solo con los números y signos.
4. Espacios: No importa si hay muchos espacios entre las comas, el programa los limpia.

---

## ¿Cómo usarlo?
### Desde un Archivo
-Windows (PowerShell):
```PowerShell
Get-Content entrada.txt | python main.py
```
-Windows (CMD):
```PowerShell
type entrada.txt | python main.py
```
-Linux/Mac:
```bash
python main.py < entrada.txt
```
o:
```bash
cat entrada.txt | python main.py
```
### Guardar la Salida
Guardar resultado en archivo
```bash
python main.py < entrada.txt > salida.txt
```
-Ver y guardar al mismo tiempo
```bash
python main.py < entrada.txt | tee salida.txt
```
### Entrada Manual (para pruebas)
```python
python main.py
```
Escribe lineas manualmente
Presiona Ctrl+D (Linux/Mac) o Ctrl+Z (Windows) para terminar

---

## Ejemplo de entrada y salida:
**Entrada** (archivo `entrada.txt`):
```


-999,353,542,181,130,-841,389,668,-313,654,547,-812,-777,-564
 51   ,43, 36   , -33   ,-75     , -54,   17    ,  -34    
-339,-505,886
-25.966,19.4788,-53.7,-46.81,50.8714,-97.3481,-81.0464
-4,-562,614,-263,980,-459,230
2X92@c,944%&,774[,Y200,89M6

284
```
**Salida:**
```
0
0
-842
-49
42
-233
536
3106
0
284
```

---

## Autor:
Domínguez Chimal Alan Eduardo

