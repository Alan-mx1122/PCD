from models.muestra import Muestra
from utils.io_helpers import cargar_csv, exportar_csv
from utils.validators import validar_fila


def main():

    # Se usa y carga el archivo con nuestros datos del laboratorio 
    encabezado, filas = cargar_csv('datos/muestras_lab.csv')

    muestras = []

    # Se revisa cada fila y solo se usan las que son válidas
    for fila in filas:
        if not validar_fila(fila):
            continue  

        id_m, paciente, vol_str, unidad, tipo_analisis = fila
        volumen = float(vol_str)

        # Si la unidad es fl_oz, la convertimos a ml
        if unidad == "fl_oz":
            volumen = volumen * 29.5735

        volumen = round(volumen, 1)

        # Se crea el objeto Muestra con los datos ya limpios
        muestra = Muestra(id_m, paciente, volumen, tipo_analisis)
        muestras.append(muestra)


    # REPORTE DETALLE
    # Se ordenan por ID antes de escribirlos en el archivo
    muestras.sort(key=lambda m: m.id)

    cols_detalle = ["id_muestra", "paciente", "tipo_analisis", "volumen_ml", "tamano_muestra"]
    filas_detalle = []

    for m in muestras:
        # m.clasificar() usa los umbrales definidos en muestra.py
        fila = [m.id, m.paciente, m.tipo, f"{m.volumen:.1f}", m.clasificar()]
        filas_detalle.append(fila)

    exportar_csv('salidas/reporte_detalle.csv', cols_detalle, filas_detalle)


    # REPORTE RESUMEN
    # Se agrupan por tipo_analisis: guardamos suma, conteo y máximo
    agrupado = {}

    for m in muestras:
        if m.tipo not in agrupado:
            agrupado[m.tipo] = [0.0, 0, 0.0]

        agrupado[m.tipo][0] += m.volumen
        agrupado[m.tipo][1] += 1

        # Se actualiza el máximo si encontramos uno mayor
        if m.volumen > agrupado[m.tipo][2]:
            agrupado[m.tipo][2] = m.volumen

    cols_resumen = ["tipo_analisis", "conteo", "promedio", "maximo"]
    filas_resumen = []

    for tipo, valores in agrupado.items():
        suma, conteo, maximo = valores
        promedio = round(suma / conteo, 1)
        filas_resumen.append([tipo, conteo, f"{promedio:.1f}", f"{maximo:.1f}"])

    #  Se ordenan de mayor a menor
    filas_resumen.sort(key=lambda x: (x[1], x[0]), reverse=True)

    exportar_csv('salidas/reporte_resumen.csv', cols_resumen, filas_resumen)

    print("Listo, los reportes quedaron en la carpeta 'salidas/'")


if __name__ == "__main__":
    main()

