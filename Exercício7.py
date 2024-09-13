def calculo(alt, base):
    return round(alt * base)

alt = float(input("INFORME A MEDIDA LATERAL DO TERRENO: "))
base = float(input("INFORME A BASE DO TERRENO: "))

print(f"Area = {calculo(alt, base)}, referentes as medidas: {alt}, {base}")

