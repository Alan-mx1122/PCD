import sys
from models import Producto
from utils import validar_producto, leer_inventario, escribir_reporte

# Configuracion de archivos
ARCHIVO_INVENTARIO = "data/inventario.csv"
ARCHIVO_REPORTE = "outputs/reporte_inventario.csv"

def crear_productos(datos_raw):
    """Convierte lista de diccionarios en objetos Producto. Ignora registros invalidos."""
    productos = []

    for datos in datos_raw:
        sku = datos.get('sku')
        nombre = datos.get('nombre')
        categoria = datos.get('categoria')
        precio = datos.get('precio')
        stock = datos.get('stock')
        stock_minimo = datos.get('stock_minimo')

        es_valido, error = validar_producto(sku, nombre, categoria, precio, stock, stock_minimo)

        if not es_valido:
            print(f"Advertencia: Ignorando registro invalido - {error}")
            continue

        producto = Producto(
            sku=sku,
            nombre=nombre,
            categoria=categoria,
            precio=float(precio),
            stock=int(stock),
            stock_minimo=int(stock_minimo)
        )
        productos.append(producto)

    return productos

def filtrar_necesitan_reorden(productos):
    """Filtra productos que necesitan reorden."""
    return [p for p in productos if p.necesita_reorden()]

def ordenar_por_faltantes(productos):
    """Ordena por unidades faltantes (descendente)."""
    return sorted(productos, key=lambda p: p.unidades_faltantes(), reverse=True)

def main():
    print("-" * 50)
    print("SISTEMA DE INVENTARIO")
    print("-" * 50)

    try:
        # 1. Leer el inventario desde archivo
        datos_raw = leer_inventario(ARCHIVO_INVENTARIO)

        # 2. Validar y crear objetos Producto
        productos = crear_productos(datos_raw)

        # 3. Filtrar y ordenar los que necesitan reorden
        necesitan_reorden = filtrar_necesitan_reorden(productos)
        necesitan_reorden = ordenar_por_faltantes(necesitan_reorden)

        # 4. Escribir reporte a archivo
        if necesitan_reorden:
            escribir_reporte(necesitan_reorden, ARCHIVO_REPORTE)
            print(f"\nProceso exitoso:")
            print(f"-> Productos analizados: {len(productos)}")
            print(f"-> Productos a reordenar: {len(necesitan_reorden)}")
            print(f"-> Reporte: {ARCHIVO_REPORTE}")
        else:
            print("\nInventario completo: No hay productos con stock bajo.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ARCHIVO_INVENTARIO}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
    