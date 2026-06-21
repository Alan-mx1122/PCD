import sys
import math

def main():
    es_primera = True
    cositas = {}

    for renglon in sys.stdin:
        renglon = renglon.strip()

        if es_primera:
            es_primera = False
            continue

        if not renglon:
            continue

        cachitos = renglon.split(',')

        if len(cachitos) != 4:
            continue

        articulo = cachitos[1].strip()

        if not articulo:
            continue

        try:
            cuantos = int(cachitos[2].strip())
            cuanto_cuesta = float(cachitos[3].strip())
        except (ValueError, TypeError):
            continue

        # Validar cantidad positiva
        if cuantos <= 0:
            continue

        # Validar precio no negativo y no corrupto (inf, nan)
        if cuanto_cuesta < 0 or math.isinf(cuanto_cuesta) or math.isnan(cuanto_cuesta):
            continue

        if articulo not in cositas:
            cositas[articulo] = {"cuantos": 0, "lana": 0.0}

        cositas[articulo]["cuantos"] += cuantos
        cositas[articulo]["lana"] += cuantos * cuanto_cuesta

    # Calcular precio promedio
    for articulo in cositas:
        cuantos = cositas[articulo]["cuantos"]
        lana = cositas[articulo]["lana"]
        cositas[articulo]["promedio"] = lana / cuantos if cuantos > 0 else 0

    # Ordenar por lana descendente
    lista_acomodada = sorted(cositas.items(), key=lambda x: x[1]["lana"], reverse=True)

    # Generar salida CSV
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for articulo, info in lista_acomodada:
        print(f"{articulo},{info['cuantos']},{info['lana']:.2f},{info['promedio']:.2f}")

if __name__ == "__main__":
    main()
    