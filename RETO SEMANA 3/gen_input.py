import random
import sys

# Genera 100 filas por defecto o las que pidas
cantidad = int(sys.argv[1]) if len(sys.argv) > 1 else 100
productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Audifonos"]

print("fecha,producto,cantidad,precio_unitario")
for _ in range(cantidad):
    fecha = f"2026-03-{random.randint(1, 30):02d}"
    p = random.choice(productos)
    c = random.randint(1, 20)
    pr = round(random.uniform(200, 20000), 2)
    print(f"{fecha},{p},{c},{pr}")
