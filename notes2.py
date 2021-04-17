import sys

print(f"Número de parametros: {len(sys.argv)}")

for n, p in enumerate(sys.argv):
    print(f"Parametro {n + 1} = {p}")