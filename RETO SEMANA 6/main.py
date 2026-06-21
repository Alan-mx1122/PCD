#!/usr/bin/env python3
import sys
import re

# Diccionarios de configuración global para validación semántica
REQUISITOS = {
    "DEPARTAMENTOS": {"VEN", "ADM", "TEC", "LOG", "RHH"},
    "SERIES": {"A", "B", "C", "D", "E"},
    "RANGOS_FECHA": {
        "ANIO_MIN": 2020,
        "ANIO_MAX": 2030,
        "MES_MIN": 1,
        "MES_MAX": 12,
        "DIA_MIN": 1,
        "DIA_MAX": 31
    }
}


def detectar_tipo(codigo: str) -> str:
    """
    Analiza la estructura macro del código usando expresiones regulares
    para identificar a qué entidad pertenece.
    """
    # Patrones estructurales iniciales (Regla 1)
    patrones_macro = {
        "producto": r'^[A-Za-z]{3}-\d{4}-[A-Za-z]{2}$',
        "envio": r'^ENV-\d{4}-\d{2}-\d{2}-\d{6}$',
        "empleado": r'^EMP-[A-Za-z]{3}-\d{4}$',
        "factura": r'^FAC-[A-Za-z]-\d{6}$'
    }
    
    for tipo, expresion in patrones_macro.items():
        if re.match(expresion, codigo):
            return tipo
            
    return "desconocido"


def validar_producto(codigo: str) -> bool:
    """Verifica que el identificador de categoría y el país estén en mayúsculas."""
    # Estructura rígida: 3 letras mayúsculas - 4 dígitos - 2 letras mayúsculas
    patron_estricto = r'^[A-Z]{3}-\d{4}-[A-Z]{2}$'
    return bool(re.match(patron_estricto, codigo))


def validar_envio(codigo: str) -> bool:
    """Evalúa que los componentes cronológicos se ubiquen dentro de los límites de la empresa."""
    patron_captura = r'^ENV-(\d{4})-(\d{2})-(\d{2})-\d{6}$'
    match = re.match(patron_captura, codigo)
    
    if not match:
        return False
        
    # Extracción de componentes temporales
    str_anio, str_mes, str_dia = match.groups()
    anio, mes, dia = int(str_anio), int(str_mes), int(str_dia)
    
    limites = REQUISITOS["RANGOS_FECHA"]
    
    # Validación lógica de rangos
    valido_anio = limites["ANIO_MIN"] <= anio <= limites["ANIO_MAX"]
    valido_mes = limites["MES_MIN"] <= mes <= limites["MES_MAX"]
    valido_dia = limites["DIA_MIN"] <= dia <= limites["DIA_MAX"]
    
    return valido_anio and valido_mes and valido_dia


def validar_empleado(codigo: str) -> bool:
    """Comprueba pertenencia a departamentos oficiales y restricción de dígito inicial."""
    patron_captura = r'^EMP-([A-Za-z]{3})-(\d{4})$'
    match = re.match(patron_captura, codigo)
    
    if not match:
        return False
        
    depto, identificador = match.groups()
    
    # Validaciones específicas: departamento existente y número no inicia con '0'
    depto_valido = depto in REQUISITOS["DEPARTAMENTOS"]
    num_valido = not identificador.startswith('0')
    
    return depto_valido and num_valido


def validar_factura(codigo: str) -> bool:
    """Valida que la serie pertenezca al rango clasificado A-E y sea mayúscula."""
    patron_captura = r'^FAC-([A-Za-z])-\d{6}$'
    match = re.match(patron_captura, codigo)
    
    if not match:
        return False
        
    serie = match.group(1)
    return serie in REQUISITOS["SERIES"]


def validar_codigo(codigo: str) -> tuple:
    """Orquesta la clasificación y la posterior evaluación estricta del código."""
    tipo = detectar_tipo(codigo)
    
    # Mapeo de funciones de evaluación para evitar estructuras 'if-elif' densas
    evaluadores = {
        "producto": validar_producto,
        "envio": validar_envio,
        "empleado": validar_empleado,
        "factura": validar_factura
    }
    
    if tipo in evaluadores:
        es_valido = evaluadores[tipo](codigo)
        return tipo, es_valido
        
    return "desconocido", False


def main():
    # Encabezado obligatorio del formato CSV requerido
    print("codigo,tipo,valido")
    
    # Procesamiento eficiente de flujo desde stdin (línea por línea)
    for linea in sys.stdin:
        codigo = linea.strip()
        
        # Omitir registros vacíos de manera silenciosa
        if not codigo:
            continue
            
        tipo, es_valido = validar_codigo(codigo)
        estado_texto = "VALIDO" if es_valido else "INVALIDO"
        
        print(f"{codigo},{tipo},{estado_texto}")


if __name__ == "__main__":
    main()

