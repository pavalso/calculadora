#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys

def sumar(valor1, valor2):
        return valor1 + valor2

def restar(valor1, valor2):
        return valor1 - valor2

def multiplicar(valor1, valor2):
        return valor1 * valor2

def dividir(valor1, valor2):
        return valor1 / valor2

def potencia(valor1, valor2):
        return pow(valor1, valor2)

def raiz_enesima(valor1, valor2):
        return valor1 ** (1 / float(valor2))

def borrar():
        os.system("cls")

def salir():
        sys.exit(0)

def menu():
        print("** ::::::::::::::::::::::::: **")
        print(":: Seleccione una operanción ::")
        print("** ::::::::::::::::::::::::: **")
        print("-------------------------------")
        print("| Suma:             ->  1     |")
        print("| Resta:            ->  2     |")
        print("| Multiplicación:   ->  3     |")
        print("| División:         ->  4     |") 
        print("| Potencia:         ->  5     |")
        print("| Raiz enesima:     ->  6     |")
        print("| Borrar:           ->  b     |")
        print("| Salir:            ->  s     |")
        print("-------------------------------")
        print("** ::::::::::::::::::::::::: **") 
        print("\n")

def elegir_Opcion():
        return input("Elige una opcíon:\n")[0]

def obtener_Valores():
        valor1 = int(input("Primer valor:"))
        valor2 = int(input("Segundo valor:"))
        return valor1, valor2

def nueva_Operacion():
        reiniciar = input("¿Quiere realizar una nueva operación? [S/N]\n")[0]
        return True if reiniciar == "S" or reiniciar == "s" else False

opciones = {
        "1":sumar,
        "2":restar,
        "3":multiplicar,
        "4":dividir,
        "5":potencia,
        "6":raiz_enesima,
}

opciones_shell = {
        "b":borrar,
        "s":salir,
        "B":borrar,
        "S":salir,
}

if __name__ == "__main__":
        while True:
                menu()
                opcion = elegir_Opcion()
                funcion = opciones.get(opcion)
                if funcion:
                        try:
                                valor1, valor2 = obtener_Valores()
                                print(funcion(valor1, valor2))
                        except:
                                print("Se ha introducido un valor incorrecto")
                else:
                        try:
                                funcion = opciones_shell[opcion]
                                funcion()
                        except:
                                print("Operación desconocida '%s'" % opcion)
                if not nueva_Operacion():
                        salir()
