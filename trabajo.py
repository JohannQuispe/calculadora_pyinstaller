from basic.suma import suma
from advanced.potencia import potencia
from utils.imprimir import imprimir_resultado

def main():
    a, b = 5, 3
    suma_result = suma(a, b)
    potencia_result = potencia(a, b)
    imprimir_resultado(suma_result)
    imprimir_resultado(potencia_result)

if __name__ == "__main__":
    main()