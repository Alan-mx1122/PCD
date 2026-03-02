import sys

def clean(value):
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no validos
    - Retorna el numero limpio como string
    """
    value = value.strip()
    valid_characters = "0123456789.-"
    result = ''
    for char in value:
        if char in valid_characters:
            result += char
    pass

def process_line(line):
    pass

def main():
