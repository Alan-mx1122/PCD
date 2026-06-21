import sys

def convertir_f_a_c(f):
    '''Función que transforma grados Fahrenheit a Celsius.'''
    '''Aplicamos la formula estandar para la conversion (F-32) * 5/9 '''
    return (f - 32) * 5 / 9

def clasificar_categoria(celsius):
    '''Determina la categoria segun la tabla de clasificacion'''
    if celsius < 0:
        return 'Congelante'
    elif celsius <= 15:
        return 'Frio'
    elif celsius <= 25:
        return 'Templado'
    elif celsius <= 35:
        return 'Calido'
    else:
        return 'Extremo'
    

def main():
    '''Leer y descartar encabezado de entrada'''
    es_cabecera = True

    '''Encabezado de salida'''
    print("ciudad,temperatura_celsius,clasificacion")
    
    for linea in sys.stdin:
        linea = linea.strip()
        
        '''Salta la primera linea del CSV de entrada'''
        if es_cabecera:
            es_cabecera = False
            continue
            
        if not linea:
            continue
            
        '''Separar campos'''
        info = linea.split(',')
        if len(info) != 3:
            continue
            
        ciudad, valor_str, escala = info
        escala = escala.strip().upper()

        '''Convertir temperatura'''
        try:
            temp_num = float(valor_str)
        except ValueError:
            continue
        
        '''Validar unidad'''
        if escala not in ['C', 'F']:
            continue 
            
        '''Conversion si es necesario'''
        if escala == 'F':
            celsius = convertir_f_a_c(temp_num)
        else:
            celsius = temp_num
            
        clima = clasificar_categoria(celsius)
        
        # Salida con 1 decimal exacto
        print(f"{ciudad},{celsius:.1f},{clima}")

if __name__ == "__main__":
    main()
    
