from basic import suma, resta, multiplicacion, division
from advanced import potencia, raiz
from utils import pedir_numero, mostrar_menu


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            a = pedir_numero("Número 1: ")
            b = pedir_numero("Número 2: ")
            print("Resultado:", suma(a, b))

        elif opcion == "2":
            a = pedir_numero("Número 1: ")
            b = pedir_numero("Número 2: ")
            print("Resultado:", resta(a, b))

        elif opcion == "3":
            a = pedir_numero("Número 1: ")
            b = pedir_numero("Número 2: ")
            print("Resultado:", multiplicacion(a, b))

        elif opcion == "4":
            a = pedir_numero("Número 1: ")
            b = pedir_numero("Número 2: ")
            print("Resultado:", division(a, b))

        elif opcion == "5":
            base = pedir_numero("Base: ")
            exp = pedir_numero("Exponente: ")
            print("Resultado:", potencia(base, exp))

        elif opcion == "6":
            num = pedir_numero("Número: ")
            ind = pedir_numero("Índice: ")
            print("Resultado:", raiz(num, ind))

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()