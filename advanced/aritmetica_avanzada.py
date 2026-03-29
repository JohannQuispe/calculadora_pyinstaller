def potencia(base, exponente):
    return base ** exponente

def raiz(numero, indice):
    if numero < 0 and indice % 2 == 0:
        return "Error: raíz par de número negativo"
    return numero ** (1 / indice)