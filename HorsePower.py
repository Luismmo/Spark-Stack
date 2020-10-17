import os
from io import open 
import codecs
from Armeria import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import subprocess
import time

class SparkStack(object):
    def __init__(self):
        self.automatas = []
        self.gramaticas = []
    
    def clrscr(self):
        os.system("cls")
    def Inicio(self):        
        self.clrscr()
        for a in range(6):
            print("Spark Stack en Ejecución ")
            print("\n____________________________________")
            print("Desarrollador: Luis Amilcar Morales Xón \nCarnet: 201701059")
            print("-------------------------------------> " + str(a*20)+"%")
            print("Tiempo restante para la ejecución del programa: "+str(5-a))
            time.sleep(1)
            self.clrscr()
        self.Menu() 

    def Menu(self):
        salida = True
        while salida:
            self.clrscr()
            print("************** Módulo principal **************\n")
            print("1- Modulo gramática libre de contexto")
            print("2- Módulo autómatas de pila")
            print("3- Salir")
            opcion = int(input("\nIngrese una opcion: "))
            if opcion==1:
                self.ModuloGramaticas()
            elif opcion == 2:
                self.ModuloAutomatas()
            elif opcion == 3:                
                salida = False
                self.clrscr()
    
    def ModuloGramaticas(self):
        salida2 =True
        while salida2:
            self.clrscr()
            print("******** Módulo de gramaticas libres de contexto ********\n")
            print("1- Cargar archivo")
            print("2- Mostrar información general")
            print("3- Árbol de derivación")
            print("4- Generar autómata de pila equivalente")
            print("5- Volver al módulo principal")
            opcion = int(input("\nIngrese una opción: "))
            if opcion == 1:
                print("cargar archivo")
                time.sleep(1)
            elif opcion == 2:
                print("mostrando información")
                time.sleep(1)
            elif opcion == 3:
                print("sacando arbol")
                time.sleep(1)
            elif opcion == 4:
                print("generando equivalente")
                time.sleep(1)
            elif opcion == 5:
                salida2 = False                

    def ModuloAutomatas(self):
        salida3 =True
        while salida3:
            self.clrscr()
            print("******** Módulo de autómatas de pila ********\n")
            print("1- Cargar archivo")
            print("2- Mostrar información general")
            print("3- Validar una cadena")
            print("4- Ruta de validación")
            print("5- Recorrido paso a paso")
            print("6- Validar cadena en una pasada")
            print("7- Volver al módulo principal")
            opcion = int(input("\nIngrese una opción: "))
            if opcion == 1:
                print("cargar archivo")
                time.sleep(1)
            elif opcion == 2:
                print("mostrando información")
                time.sleep(1)
            elif opcion == 3:
                print("sacando arbol")
                time.sleep(1)
            elif opcion == 4:
                print("generando equivalente")
                time.sleep(1)
            elif opcion == 5:
                print("recorrido paso a paso")
                time.sleep(1)
            elif opcion == 6:
                print("de una pasada")
                time.sleep(1)
            elif opcion == 7:
                salida3 = False                