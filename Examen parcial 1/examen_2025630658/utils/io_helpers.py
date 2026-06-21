import csv

# Función para cargar los datos desde el CSV
def cargar_csv(ruta_archivo):
    datos = []

    # Abrimos el archivo en modo lectura con codificación utf-8
    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    lector = csv.reader(archivo)

    # La primera fila es el encabezado, entonces la guardamos aparte
    encabezado = next(lector)

    for fila in lector:
        # Salto de filas vacías
        if len(fila) == 0:
            continue
        datos.append(fila)

    archivo.close()
    return encabezado, datos

# Función para guardar los resultados en la carpeta 'salidas'
def exportar_csv(ruta_salida, encabezado, filas):
    archivo = open(ruta_salida, 'w', encoding='utf-8', newline='')
    escritor = csv.writer(archivo)

    # Para escribir primero el encabezado, luego fila por fila de los datos procesados
    escritor.writerow(encabezado)
    for fila in filas:
        escritor.writerow(fila)

    archivo.close()
    