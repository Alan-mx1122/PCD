import sys

def clean(dirty_values):
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no validos
    - Retorna el numero limpio como string
    """
    line = line.strip()
    if line == '':
        return 0
    valid_characters = "0123456789.-"
    pure_values = ''
    for char in dirty_values:
        if char in valid_characters:
            pure_values += char
    return pure_values

def process_line(line):
    """
    Procesa una linea completa:
    - Separa por comas
    - Limpia cada valor
    - Trunca a entero
    - Suma todos
    - Retorna el resultado
    """
    elements == line.split(',')
    result = 0
    pass

def main():
