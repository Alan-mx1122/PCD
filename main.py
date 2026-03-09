import sys

def clean(dirty_values):
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no validos
    - Retorna el numero limpio como string
    """
    dirty_values = dirty_values.strip()
    if dirty_values == '':
        return ''
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
   if not line:
    elements = line.split(',')
    result = 0
    for number in elements:
        add_value = clean(number)
        if add_value == "" or add_value == "." or add_value == "-":
            continue
        try:
            number_truncate = int(float(add_value))
            result += number_truncate
        except ValueError:
            continue
    return result

def main():
    """
    Lee de stdin linea por linea
    Procesa cada linea
    Imprime el resultado
    """
    for linesys in sys.stdin:
        total = process_line(linesys)
        print(total)

if __name__ == "__main__":
    main()

