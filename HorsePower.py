import os
from io import open 
import codecs
from Armeria import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import subprocess
import time
from graphviz import Digraph

class SparkStack(object):
    def __init__(self):
        self.automatas = []
        self.gramaticas = []                
    
    def clrscr(self):
        os.system("cls")

    def verificarGR(self, nombre):
        bandera = False
        for a in range(len(self.gramaticas)):
            if nombre == self.gramaticas[a].getName():
                bandera=True
        return bandera

    def verificarAP(self, nombre):
        bandera = False
        for a in range(len(self.automatas)):
            if nombre == self.automatas[a].getName():
                bandera=True
        return bandera

    def Inicio(self):        
        self.clrscr()
        for a in range(6):
            print("Spark Stack en Ejecución ")
            print("\n____________________________________")
            print("Desarrollador: Luis Amilcar Morales Xón \nCarnet: 201701059")
            print("-------------------------------------> " + str(a*20)+"%")
            print("Tiempo restante para la ejecución del programa: "+str(5-a))
            time.sleep(0.1)
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
    
    #**************************************************************
    #Aqui en adelante viene lo de las gramaticas libres de contexto
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
                self.cargarArchivo()
                time.sleep(1)
            elif opcion == 2:
                self.MostrarInformacion()
                time.sleep(1)
            elif opcion == 3:
                self.generarArbol()
                time.sleep(1)
            elif opcion == 4:
                print("generando equivalente")
                time.sleep(1)
            elif opcion == 5:
                salida2 = False
        
    def CrearNoTerminal(self,nome,NT):
        terminator = noTerminal(NT)
        for a in range(len(self.gramaticas)):                    
            if nome == self.gramaticas[a].getName():
                if self.gramaticas[a].getNoTerms():    
                    flag = 0                                                                                
                    for i in range(len(self.gramaticas[a].getNoTerms())):                                
                        if NT == self.gramaticas[a].getNoTerms()[i].getName():                                    
                            flag+=1

                    if flag == 0:
                        self.gramaticas[a].getNoTerms().append(terminator)                                
                    else:
                        print("El No Terminal ya existe, no puede haber dos No Terminales con el mismo nombre.")                                
                else:                    
                    self.gramaticas[a].getNoTerms().append(terminator)
    
    def AgregarTerminales(self,nome,zona4):
        for a in range(len(self.gramaticas)):
            if nome == self.gramaticas[a].getName():
                #viendo si podemos agregar el terminal
                bandera = 0
                for k in range(len(self.gramaticas[a].getNoTerms())):
                    if zona4 == self.gramaticas[a].getNoTerms()[k].getName():
                        bandera+=1
                if bandera == 0:
                    #podemos agregar la terminal
                    if self.gramaticas[a].getTerminales():    
                        flag = 0                                                                                
                        for i in range(len(self.gramaticas[a].getTerminales())):
                            if zona4 == self.gramaticas[a].getTerminales()[i]:                                    
                                flag+=1

                        if flag == 0:
                            self.gramaticas[a].getTerminales().append(zona4)
                        else:
                            print("El Terminal ya existe para la Gramatica.")
                    else:
                        self.gramaticas[a].getTerminales().append(zona4)                    
                    
                else:
                    input("El terminal que se quiere agregar a la lista ya está como un No Terminal.\nNo se puede realizar la operacion.")

    def AsignarNoTerminalInicial(self,nome,dato):
        flag = 0
        for i in range(len(self.gramaticas)):
            if nome == self.gramaticas[i].getName():
                if self.gramaticas[i].getNoTerms():                                        
                    for b in range(len(self.gramaticas[i].getNoTerms())):
                        if self.gramaticas[i].getNoTerms()[b].getName()==dato:                                                    
                            flag+=1
                            self.gramaticas[i].getNoTerms()[b].setInicio(True)
                    if flag==0:                                            
                        input("El no terminal no existe.\nIntente de nuevo.") 
                else:
                    input("El AFD al que intenta asignar un estado inicial no cuenta con ningun estado todavia.")
    
    def CrearProducciones(self,nome,produc):
        #try:
            frag = produc.split('>')
                    #  0  , 1
            #Frag = ["A","0 B"]
            #estados = ["0","B"]
            frag2 = frag[1].split(' ')            
            for i in range(len(self.gramaticas)):
                if nome == self.gramaticas[i].getName():
                    estructura = ""
                    for a in range(len(frag2)):
                        for k in range(len(self.gramaticas[i].getNoTerms())):
                            if frag2[a]==self.gramaticas[i].getNoTerms()[k].getName():
                                estructura += "NoTerminal"
                        for l in range(len(self.gramaticas[i].getTerminales())):
                            if frag2[a]==self.gramaticas[i].getTerminales()[l]:
                                estructura+="Terminal"
                    #print(estructura)
                    #time.sleep(0.5)
                    produccion = Produccion(str(frag[0]),str(frag[1]))
                    self.gramaticas[i].getProducciones().append(produccion)
                    if estructura != "Terminal" and estructura != "TerminalNoTerminal" and estructura != "NoTerminalTerminal":
                        self.gramaticas[i].setTipo3(True)
        #except:
         #   pass

    def cargarArchivo(self):
        self.clrscr()
        nombre = str(input("Ingrese el nombre del archivo: "))
        archivo = open(nombre,'r')
        bailemos = archivo.read()
        archivo.close()
        #separamos las gramaticas
        primeraRonda = bailemos.split('%')
        try:
            primeraRonda.remove('')            
        except:
            pass        
        #ciclo for para extraer los datos de cada Gramatica, 
        # ponerlos en una lista de listas y eliminar elementos en blanco
        for a in range(len(primeraRonda)):
            gramatica = primeraRonda[a].split('\n')
            try:
                gramatica.remove('')
                gramatica.remove('')
            except:
                pass
            
            name = str(gramatica[0])
            print(name)
            #verificamos que no se repitan nombres
            flag = self.verificarGR(name)
            if flag == False: #no se repite
                GT3 = Gramatica(name)
                self.gramaticas.append(GT3)

                #creamos y agregamos los No Terminales a la gramatica
                noTerminales = gramatica[1].split(',')
                for i in range(len(noTerminales)):
                    self.CrearNoTerminal(name,str(noTerminales[i]))

                #agregamos los terminales a la gramatica
                terminales = gramatica[2].split(',')
                for j in range(len(terminales)):
                    self.AgregarTerminales(name,str(terminales[j]))
                
                #asignamos el No terminal inicial
                self.AsignarNoTerminalInicial(name,str(gramatica[3]))

                #tratamos con las producciones
                for m in range(len(gramatica)):
                    if m >= 4:
                        #print(gramatica[m])
                        self.CrearProducciones(name,str(gramatica[m]))

                for q in range(len(self.gramaticas)):
                    if name == self.gramaticas[q].getName():
                        esTipo3 = self.gramaticas[q].getTipo3()
                        if esTipo3 == True:
                            print("Gramatica agregada con éxito.\n")
                            #time.sleep(2)
                        else:
                            self.gramaticas.pop(q)
                            print("Es gramatica regular. SE DESCARTA.\n")
                            #time.sleep(2)
            else: #se repite
                print("Aviso: Se encontró una gramatica con el mismo nombre en memoria, la accion no se puede completar.")
                time.sleep(2)

    def listarGramaticas(self):        
        for a in range(len(self.gramaticas)):
            print("-> "+self.gramaticas[a].getName())
        print(" ")

    def MostrarInformacion(self):
        self.clrscr()
        print("****** Mostrar información ******")
        self.listarGramaticas()
        eleccion = str(input("Ingrese el nombre de la gramatica: "))
        print(" ")
        for a in range(len(self.gramaticas)):
            if eleccion == self.gramaticas[a].getName():
                self.clrscr()
                print("Nombre: "+self.gramaticas[a].getName())
                listaNoTerminales=[]
                for p in range(len(self.gramaticas[a].getNoTerms())):
                    listaNoTerminales.append(self.gramaticas[a].getNoTerms()[p].getName())
                print("No terminales: "+str(listaNoTerminales))
                print("Terminales: "+str(self.gramaticas[a].getTerminales()))
                inicial = ""
                for q in range(len(self.gramaticas[a].getNoTerms())):
                    if self.gramaticas[a].getNoTerms()[q].getInicio()== True:
                        inicial = self.gramaticas[a].getNoTerms()[q].getName()
                print("No terminal inicial: "+inicial)
                print("Producciones:")
                anterior = ""
                for i in range(len(self.gramaticas[a].getProducciones())):
                    if i==0:
                        print(self.gramaticas[a].getProducciones()[i].gettInicial()+">"+self.gramaticas[a].getProducciones()[i].getDerivacion())
                        anterior=self.gramaticas[a].getProducciones()[i].gettInicial()
                    if i>=1:
                        if anterior==self.gramaticas[a].getProducciones()[i].gettInicial():
                            print(" |"+self.gramaticas[a].getProducciones()[i].getDerivacion())
                        else:
                            print(self.gramaticas[a].getProducciones()[i].gettInicial()+">"+self.gramaticas[a].getProducciones()[i].getDerivacion())
                            anterior=self.gramaticas[a].getProducciones()[i].gettInicial()
        input("\nPRESIONE ENTER PARA FINALIZAR EL REPORTE.")
    
    def generarArbol(self):
        contador = 0
        ancla = 0
        ancla2 = 0
        conexiones = []
        controles = []
        self.clrscr()
        print("****** Árbol de derivación ******")
        self.listarGramaticas()
        name = str(input("Ingrese el nombre de la gramatica: "))
        for i in range(len(self.gramaticas)):
            if name == self.gramaticas[i].getName():
                f = Digraph(filename = self.gramaticas[i].getName(), format='png', encoding='UTF-8')
                f.attr(rankdir = 'TB')
                f.attr('node', shape='none')
                
                f.edge_attr.update(arrowhead = "none")
                for a in range(len(self.gramaticas[i].getProducciones())):                    
                        if a == 0:                            
                            #creo el nodo de la terminal del inicio de la produccion
                            nodo = self.gramaticas[i].getProducciones()[a].gettInicial()
                            f.node(str(contador),nodo)
                            #guardo el id que corresponde al nodo
                            ancla=contador                        
                            contador+=1
                            #creo los otros nodos que corresponden a la derivacion del terminal inicial
                            derivacion = self.gramaticas[i].getProducciones()[a].getDerivacion().split(' ')
                            for k in range(len(derivacion)):
                                nodo = derivacion[k]
                                f.node(str(contador),nodo)
                                edge = Conexion(ancla,contador)
                                conexiones.append(edge)
                                for t in range(len(self.gramaticas[i].getNoTerms())):
                                    if nodo == self.gramaticas[i].getNoTerms()[t].getName():
                                        control = Control(contador,nodo)
                                        controles.append(control)
                                contador+=1
                            self.gramaticas[i].getProducciones()[a].setYapaso(True)
                        else:
                            for s in range(len(self.gramaticas[i].getProducciones())):
                                for c in range(len(controles)):
                                    if controles[c].getNodo() == self.gramaticas[i].getProducciones()[s].gettInicial() and self.gramaticas[i].getProducciones()[s].getYapaso()==False:
                                        derivaciones = self.gramaticas[i].getProducciones()[s].getDerivacion().split(' ')
                                        input(derivaciones)
                                        for x in range(len(derivaciones)):
                                            nodo = derivaciones[x]
                                            f.node(str(contador),nodo)
                                            edge = Conexion(controles[c].getAncla(),contador)
                                            conexiones.append(edge)
                                            for b in range(len(self.gramaticas[i].getNoTerms())):
                                                if nodo  == self.gramaticas[i].getNoTerms()[b].getName():
                                                    control = Control(contador,nodo)
                                                    controles.append(control)
                                            contador+=1
                                        self.gramaticas[i].getProducciones()[s].setYapaso(True)
                                                                                           
                for q in range(len(conexiones)):
                    f.edge(conexiones[q].getInicio(),conexiones[q].getSiguiente())
                            
                f.view()

        #f.node('nombre', label=)

    #*********************************************
    #de aqui en adelante viene lo de los automatas 
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