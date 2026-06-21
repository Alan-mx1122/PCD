def validar_fila(fila):
    # Se verifica que las filas tenga 5 campos
    if len(fila) != 5:
        return False

    # El volumen está en la fila 2, intentamos convertirlo
    volumen = fila[2]
    try:
        volumen_num = float(volumen)
    except ValueError:
        # Si no se puede convertir, el dato está mal
        return False

    # No debe haber volumenes negativos
    if volumen_num < 0:
        return False

    # Solo se aceptan estas dos unidades
    if fila[3] not in ["fl_oz", "ml"]:
        return False

    # Si pasó todo lo anterior, la fila es válida
    return True

