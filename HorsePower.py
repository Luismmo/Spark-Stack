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
            time.sleep(1)
            self.clrscr()
        self.Menu()         

    def Menu(self):
        try:
            salida = True
            while salida:
                self.clrscr()
                print("************** Módulo principal **************\n")
                print("1- Modulo gramática libre de contexto")
                print("2- Módulo autómatas de pila")
                print("3- Salir")
                opcion = int(input("\nIngrese una opcion: "))
                if opcion==1:
                    try:
                        self.ModuloGramaticas()
                    except:
                        self.ModuloGramaticas()
                elif opcion == 2:
                    try:
                        self.ModuloAutomatas()
                    except:
                        self.ModuloAutomatas()
                elif opcion == 3:                
                    salida = False
                    self.clrscr()
        except:
            self.Menu()
    
    #**************************************************************
    #Aqui en adelante viene lo de las gramaticas libres de contexto
    def ModuloGramaticas(self):
        try:
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
                    #time.sleep(1)
                elif opcion == 3:
                    self.generarArbol()
                    #time.sleep(1)
                elif opcion == 4:
                    self.automataEquivalente()
                    time.sleep(1)
                elif opcion == 5:
                    salida2 = False
        except:
            self.ModuloGramaticas()
        
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
        try:
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
                                time.sleep(1.3)
                            else:
                                self.gramaticas.pop(q)
                                print("Es gramatica regular. SE DESCARTA.\n")
                                time.sleep(1.3)
                else: #se repite
                    print("Aviso: Se encontró una gramatica con el mismo nombre en memoria, la accion no se puede completar.")
                    time.sleep(1.3)
        except:
            input("El archivo que se quiere cargar no cuenta con la estructura que demanda el programa")

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
        mismoNodo = ""
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
                                #uno el nodo raiz con su produccion.
                                edge = Conexion(ancla,contador)
                                conexiones.append(edge)
                                #valido si lo que viene en su derivación es un No terminal que tiene mas derivaciones
                                for t in range(len(self.gramaticas[i].getNoTerms())):
                                    if nodo == self.gramaticas[i].getNoTerms()[t].getName():
                                        #si encuentro un no terminal creo un objeto que lleva el control de su id para las conexiones
                                        control = Control(contador,nodo)
                                        controles.append(control)
                                contador+=1
                            self.gramaticas[i].getProducciones()[a].setYapaso(True)
                        else:
                            for s in range(len(self.gramaticas[i].getProducciones())):
                                for c in range(len(controles)):
                                    if controles[c].getNodo() == self.gramaticas[i].getProducciones()[s].gettInicial() and self.gramaticas[i].getProducciones()[s].getYapaso()==False:
                                        #codigo nuevo 
                                        if mismoNodo!=self.gramaticas[i].getProducciones()[s].gettInicial():
                                        #fin codigo nuevo                                            
                                            derivaciones = self.gramaticas[i].getProducciones()[s].getDerivacion().split(' ')                                        
                                            #input(derivaciones)
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
                                            mismoNodo=controles[c].getNodo()

                                        else:
                                        #nuevo codigo    
                                            nodo = self.gramaticas[i].getProducciones()[s].gettInicial()                                            
                                            for h in range(len(controles)):
                                                if nodo == controles[h].getNodo():
                                                    ancla2 = controles[h].getAncla()                                                    
                                                    
                                            #nodo = self.gramaticas[i].getProducciones()[s].gettInicial()                                            
                                            #f.node(str(contador),nodo)
                                            #guardo el id que corresponde al nodo
                                            #ancla=contador                        
                                            #edge = Conexion(ancla2,ancla)
                                            #conexiones.append(edge)
                                            #contador+=1
                                            #creo los otros nodos que corresponden a la derivacion del terminal inicial
                                            derivacion = self.gramaticas[i].getProducciones()[s].getDerivacion().split(' ')
                                            for k in range(len(derivacion)):
                                                nodo = derivacion[k]
                                                f.node(str(contador),nodo)
                                                #uno el nodo raiz con su produccion.
                                                edge = Conexion(ancla2,contador)
                                                conexiones.append(edge)
                                                #valido si lo que viene en su derivación es un No terminal que tiene mas derivaciones
                                                for t in range(len(self.gramaticas[i].getNoTerms())):
                                                    if nodo == self.gramaticas[i].getNoTerms()[t].getName():
                                                        #si encuentro un no terminal creo un objeto que lleva el control de su id para las conexiones
                                                        control = Control(contador,nodo)
                                                        controles.append(control)
                                                contador+=1
                                            self.gramaticas[i].getProducciones()[s].setYapaso(True)                                            
                                            #mismoNodo=controles[c].getNodo()
                                                                                           
                for q in range(len(conexiones)):
                    f.edge(conexiones[q].getInicio(),conexiones[q].getSiguiente())
                            
                f.view()

    def automataEquivalente(self):
        self.clrscr()
        print("****** Automata de pila equivalente ******")
        self.listarGramaticas()
        name = str(input("Ingrese el nombre de la gramatica: "))
        for i in range(len(self.gramaticas)):
            if name == self.gramaticas[i].getName():
                f = Digraph(filename = self.gramaticas[i].getName(), format='pdf', encoding='UTF-8')
                f.attr(rankdir = 'LR')                
                f.attr(fontsize='12')
                texto = ""
                texto += "Nombre: "+str(self.gramaticas[i].getName())+"\n"
                texto += "Alfabeto: "+str(self.gramaticas[i].getTerminales())+"\n"                
                lista = []
                lista +=self.gramaticas[i].getTerminales()
                for k in range(len(self.gramaticas[i].getNoTerms())):
                    lista.append(self.gramaticas[i].getNoTerms()[k].getName())
                lista.append('#')
                texto += "Alfabeto de pila: "+str(lista)+"\n"                
                texto+="Estados: [ i, p, q, f ]\n"
                texto+="Estado inicial: [ i ]\n"
                texto+="Estado de aceptación: [ f ]"
                f.attr(label=texto)
                f.attr('node', shape='none')
                f.node("0","")
                f.attr('node', shape='circle')
                f.node("1","i")
                f.node("2","p")
                f.node("3","q")
                f.attr('node', shape='doublecircle')
                f.node("4","f")
                f.edge('0','1')
                f.edge('1','2', label='λ,λ;#')
                f.edge('2','3', label='λ,λ;S')
                transiciones = ""
                for a in range(len(self.gramaticas[i].getTerminales())):
                    transiciones+=self.gramaticas[i].getTerminales()[a]+","+self.gramaticas[i].getTerminales()[a]+";λ\n"
                for k in range(len(self.gramaticas[i].getProducciones())):
                    transiciones+="λ,"+self.gramaticas[i].getProducciones()[k].gettInicial()+";"+self.gramaticas[i].getProducciones()[k].getDerivacion()+"\n"
                f.edge('3','3',label=transiciones)
                f.edge('3','4',label='λ,#;λ')
                f.view()
    
    #*********************************************
    #*********************************************
    #de aqui en adelante viene lo de los automatas 
    def ModuloAutomatas(self):
        try:
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
                    self.cargaAFD()
                elif opcion == 2:
                    self.informacionAutomata()
                elif opcion == 3:
                    self.clrscr()
                    print('********* Validar una cadena *********\n')
                    resultados = []
                    resultados = self.validarCadenaAFD()
                    if resultados[0] == True:
                        input('¡CADENA VALIDA!\nPrsione ENTER para volver al menú principal.')
                    else:
                        input('¡CADENA INVALIDA!\nPrsione ENTER para volver al menú principal.')
                elif opcion == 4:
                    self.clrscr()
                    print('********* Ruta de validación *********\n')
                    resultados = []
                    resultados = self.validarCadenaAFD()
                    if resultados[0] == True:
                        print('¡CADENA VALIDA!')
                        for u in range(len(resultados[1])):
                            print(resultados[1][u])
                        input('Prsione ENTER para volver al menú principal.')
                    else:                    
                        input('¡CADENA INVALIDA!\nPrsione ENTER para volver al menú principal.')
                elif opcion == 5:
                    self.recorridoApaso()
                elif opcion == 6:
                    self.validarPasada()
                elif opcion == 7:
                    salida3 = False
        except:
            self.ModuloAutomatas()
    
    def cargaAFD(self):
        try:
            self.clrscr()
            nombre = input("Ingrese el nombre del archivo para generar el/los AP/s: ")
            archivoAFDS = open(nombre,'r') 
            Datos = archivoAFDS.read()
            archivoAFDS.close()
            divisonAFDS = Datos.split('%')
            try:
                divisonAFDS.remove('')
            except:
                pass
            listaAutomatas = []
            #ciclo for para extraer los datos de cada automata, 
            # ponerlos en una lista de listas y eliminar elementos en blanco
            for a in range(len(divisonAFDS)):
                automata = divisonAFDS[a].split('\n')
                try:
                    automata.remove('')
                    automata.remove('')
                except:
                    pass
                listaAutomatas.append(automata)
            #Ciclo for para empezar a crear objetos Aefede
            for i in range(len(listaAutomatas)):
                try:
                    #verificando si el automata que se quiere agregar ya existe
                    flag = 0
                    for z in range(len(self.automatas)):
                        if listaAutomatas[i][0] == self.automatas[z].getName():
                            flag +=1
                    if flag == 0: #el automata no existe y lo agregamos
                        #tratamos con el nombre
                        name = str(listaAutomatas[i][0])
                        aefede = Aefede(name)
                        self.automatas.append(aefede)
                        #tratamos con el alfabeto
                        alpha = listaAutomatas[i][1].split(',')
                        for k in range(len(alpha)):
                            self.CrearAlfabeto(name,str(alpha[k]))
                        #tratamos con los simbolos de pila
                        simPila = listaAutomatas[i][2].split(',')
                        for k in range(len(simPila)):
                            self.CrearSimPila(name,str(simPila[k]))
                        #tratamos con los estados
                        estrato = listaAutomatas[i][3].split(',')
                        for j in range(len(estrato)):
                            self.CrearEstados(name,str(estrato[j]))                    
                        #tratamos con el estado inicial
                        self.AsignarEstadoInicial(name,str(listaAutomatas[i][4]))
                        #tratamos con los estados de aceptacion
                        try:
                            aceptaciones = listaAutomatas[i][5].split(',')
                            aceptaciones.remove('')
                        except:
                            pass
                        for l in range(len(aceptaciones)):
                            self.Acetona(name,str(aceptaciones[l]))
                        #Tratamos con las transiciones
                        for m in range(len(listaAutomatas[i])):
                            if m >=6:
                                self.Transiciones(name,str(listaAutomatas[i][m]))
                        print("AP cargado correctamente.")
                        time.sleep(1.3)

                    else:
                        print("El AP que se quiere agregar ya existe en memoria")
                        time.sleep(0.5)
                except:
                    pass
        except:
            input("El archivo que se quiere cargar no cuenta con la estructura que demanda el programa")
    
    def CrearEstados(self, nome, estado):
        state = Estado(estado)
                #print("acabamos de crear el estado")
        for a in range(len(self.automatas)):
                    #print("estamos verificando afds")
            if nome == self.automatas[a].getName():
                        #print("encontramos el afd")
                if self.automatas[a].getEstados():
                    flag = 0
                    for i in range(len(self.automatas[a].getEstados())):
                                #print("verificando estados  del afd")
                        if estado == self.automatas[a].getEstados()[i].getNameE():
                            flag+=1

                    if flag == 0:
                        self.automatas[a].getEstados().append(state)
                    else:
                        print("El estado ya existe, no puede haber dos estados con el mismo nombre.")
                                #estesi[a].getEstados().append(state)
                else:                    
                    self.automatas[a].getEstados().append(state)
    
    def CrearAlfabeto(self, nome, alfa):
        for a in range(len(self.automatas)):
            if nome == self.automatas[a].getName():
                #viendo si no ingresamos un alfabeto que ya está como estado
                bandera = 0
                for k in range(len(self.automatas[a].getEstados())):
                    if alfa == self.automatas[a].getEstados()[k].getNameE():
                        bandera+=1
                if bandera==0:
                    #print("podemos ingresar el alfabeto")
                    if self.automatas[a].getAlfabeto():    
                        flag = 0                                                                                
                        for i in range(len(self.automatas[a].getAlfabeto())):
                            if alfa == self.automatas[a].getAlfabeto()[i]:                                    
                                flag+=1

                        if flag == 0:
                            self.automatas[a].getAlfabeto().append(alfa)
                        else:
                            print("El caracter ya existe en el alfabeto.")
                    else:
                        self.automatas[a].getAlfabeto().append(alfa)
                else:
                    print("El caracter que se quiere agregar como alfabeto ya está como un estado.\nNo se puede realizar la operacion.")

    def CrearSimPila(self, nome, alfa):
        for a in range(len(self.automatas)):
            if nome == self.automatas[a].getName():
                #viendo si no ingresamos un alfabeto que ya está como estado
                bandera = 0
                for k in range(len(self.automatas[a].getEstados())):
                    if alfa == self.automatas[a].getEstados()[k].getNameE():
                        bandera+=1
                if bandera==0:
                    #print("podemos ingresar el alfabeto")
                    if self.automatas[a].getSimbolosPila():    
                        flag = 0                                                                                
                        for i in range(len(self.automatas[a].getSimbolosPila())):
                            if alfa == self.automatas[a].getSimbolosPila()[i]:                                    
                                flag+=1

                        if flag == 0:
                            self.automatas[a].getSimbolosPila().append(alfa)
                        else:
                            print("El caracter ya existe en el alfabeto.")
                    else:
                        self.automatas[a].getSimbolosPila().append(alfa)
                else:
                    print("El caracter que se quiere agregar como alfabeto ya está como un estado.\nNo se puede realizar la operacion.")

    def AsignarEstadoInicial(self, nome, dato):
        flag = 0
        for i in range(len(self.automatas)):
            if nome == self.automatas[i].getName():
                if self.automatas[i].getEstados():                    
                    #busco el nuevo estado
                    for b in range(len(self.automatas[i].getEstados())):
                        if self.automatas[i].getEstados()[b].getNameE()==dato:
                            flag+=1
                            self.automatas[i].getEstados()[b].setInicio(True)                    
                else:
                    print("El AP al que intenta asignar un estado inicial no cuenta con ningun estado todavia.")                    

    def Acetona(self,nome,dato):
        for i in range(len(self.automatas)):
            if nome == self.automatas[i].getName():
                if self.automatas[i].getEstados():                                                
                    for b in range(len(self.automatas[i].getEstados())):
                        if self.automatas[i].getEstados()[b].getNameE()==dato:                                                                
                            self.automatas[i].getEstados()[b].setAcepta(True)                         
                else:
                    print("El AP al que intenta asignar estados de aceptacion no cuenta con ningun estado todavia.")
    
    def Transiciones(self, nome, trans):
        #try:
            #A,$,$;B,#
            frag = trans.split(';')
                    #  0  , 1
            #Frag = ["A,$,$","B,#"]
            #estados = ["A","$","$"]
            parte1 = frag[0].split(',')
            parte2 = frag[1].split(',')
            for i in range(len(self.automatas)):
                if nome == self.automatas[i].getName():
                    flag1=0
                    flag2=0
                    flag3=0
                    banderita=0
                    inicial = None
                    final = None
                    #Validando terminal involucrado en la transición.
                    for c in range(len(self.automatas[i].getAlfabeto())):
                        if parte1[1] == self.automatas[i].getAlfabeto()[c] or parte1[1]=='$':
                            flag3+=1
                                    #input("terminal")

                    #validando estado inicial                     
                    for b in range(len(self.automatas[i].getEstados())):
                        if parte1[0]== self.automatas[i].getEstados()[b].getNameE():
                            flag1+=1
                            inicial = self.automatas[i].getEstados()[b]                    
                                    
                    #validando estado final
                    for b in range(len(self.automatas[i].getEstados())):
                        if parte2[0]== self.automatas[i].getEstados()[b].getNameE():
                            flag2+=1
                            final = self.automatas[i].getEstados()[b]
                                    #input("final")

                    if flag1!=0 and flag2!=0 and flag3!=0:                        
                        trancy = Transicion(inicial, parte1[1], parte1[2], final, parte2[1])
                        self.automatas[i].getTransiciones().append(trancy)                        
                    else:
                        print("Almenos un estado que está involucrado en ésta transición no existe en la lista de estados de este AFD.\nO bien el terminal involucrado no existe en el alfabeto del AFD")
        #except:
            #pass
    
    def listarAP(self):
        for i in range(len(self.automatas)):
            print("->"+self.automatas[i].getName())
        print('')
        opcion = str(input('Ingrese el nombre del automata de pila: '))
        return opcion
    
    def informacionAutomata(self):
        self.clrscr()
        print('********* Mostrar información del automata de pila *********\n')
        name = self.listarAP()
        nombre = name+".pdf"
        c = canvas.Canvas(nombre)
        #parte donde agrego los detalles        
        titulo = "Nombre: "+name
        c.setFontSize(20)
        c.drawString(225,750,titulo)                       
        c.setFont('Helvetica', 12)
        for a in range(len(self.automatas)):
            if name == self.automatas[a].getName():
                    ##parte del automata               
                    #alfabeto
                alfa=""
                for i in range(len(self.automatas[a].getAlfabeto())):
                    if i >=1:                        
                        alfa+=", "+self.automatas[a].getAlfabeto()[i]
                    else:
                        alfa+=self.automatas[a].getAlfabeto()[i]
                c.drawString(75,700,"Alfabeto: "+alfa)
                #simbolos de pila
                alfa=""
                for i in range(len(self.automatas[a].getSimbolosPila())):
                    if i >=1:                        
                        alfa+=", "+self.automatas[a].getSimbolosPila()[i]
                    else:
                        alfa+=self.automatas[a].getSimbolosPila()[i]
                c.drawString(75,685,"Alfabeto de pila: "+alfa)
                    #estados
                estadio=""
                for j in range(len(self.automatas[a].getEstados())):
                    if j >=1:
                        estadio+=", "+self.automatas[a].getEstados()[j].getNameE()
                    else:
                        estadio+=self.automatas[a].getEstados()[j].getNameE()
                c.drawString(75,670,"Estados: "+estadio)
                    #inicial
                estarto=""
                for k in range(len(self.automatas[a].getEstados())):
                    if self.automatas[a].getEstados()[k].getInicio()==True:
                        estarto=self.automatas[a].getEstados()[k].getNameE()
                c.drawString(75,655,"Estado inicial: "+estarto)
                    #estados de aceptación
                estufa=""
                bandy = 0
                for l in range(len(self.automatas[a].getEstados())):
                    if self.automatas[a].getEstados()[l].getAcepta()==True:
                        if bandy>=1:                            
                            estufa+=", "+self.automatas[a].getEstados()[l].getNameE()
                        else:
                            estufa+=self.automatas[a].getEstados()[l].getNameE()
                            bandy+=1
                c.drawString(75,640,"Estados de aceptación: "+estufa)
                                
                    #grafica
                self.generarDot(name)
                    #"C:\\Users\\almxo\\Desktop\\"+nome+".dot"
                    #os.system('dot -Tpng archivo.dot -o salida.png')
                os.system('dot -Tpng '+ name+'.dot -o '+name+'.png')
                    #subprocess.call(nome+".dot -Tpng -o "+nome+".png")
                pato=name+".png"                
                c.drawImage(pato,75,450, 450,100)                                
        c.save()
        os.system(nombre)

    def generarDot(self, nome):
        try:
            archivo = open(nome+".dot", 'w')
            archivo.write("digraph A {\n")
            archivo.write("rankdir = LR;\n")
            archivo.write("EMPTY [style=invis]\n")
            archivo.write("EMPTY [shape=point]\n")
            for a in range(len(self.automatas)):
                if nome == self.automatas[a].getName():
                    #agregando estados al dot
                    for i in range(len(self.automatas[a].getEstados())):
                        if self.automatas[a].getEstados()[i].getAcepta()==True:
                            archivo.write("node [shape=doublecircle,style=filled] "+self.automatas[a].getEstados()[i].getNameE()+"\n")
                        else:
                            archivo.write("node [shape=circle,style=filled] "+self.automatas[a].getEstados()[i].getNameE()+"\n")
                    #agregando transiciones
                    eInicial=""
                    for h in range(len(self.automatas[a].getEstados())):
                        if self.automatas[a].getEstados()[h].getInicio()==True:
                            eInicial=self.automatas[a].getEstados()[h].getNameE()
                    #EMPTY -> INCIO [label =""];
                    archivo.write("EMPTY"+" -> "+eInicial+" [label=\" "+" \"];\n")
                    for j in range(len(self.automatas[a].getTransiciones())):
                        
                        archivo.write(self.automatas[a].getTransiciones()[j].geteInicial().getNameE()+" -> "+self.automatas[a].getTransiciones()[j].geteFinal().getNameE()+" [label=\""+self.automatas[a].getTransiciones()[j].getLeer()+","+self.automatas[a].getTransiciones()[j].getSacar()+";"+self.automatas[a].getTransiciones()[j].getGuardar()+" \"];\n")
                    archivo.write("}")
            archivo.close()     
        except:
            pass
        
    def validarCadenaAFD(self):        
        nome = self.listarAP()
        aceptamos = False
        ruta = []
        bandera = 0        
        final = ""
        banderazo = 0
        #print(cadena.__len__())
        for i in range(len(self.automatas)):
            if nome == self.automatas[i].getName():
                cadena ="#"
                cadena += input("Ingrese la cadena a evaluar: ")                
                cadena+='#'
                #print(cadena)
                #for para la cadena ingresada
                for a in range(cadena.__len__()):
                    #print("empezamos con el for de la cadena")
                    #for para recorrer las transiciones del automata
                    for b in range(len(self.automatas[i].getTransiciones())):
                        #print("empezamos con el for de las transiciones")
                        if bandera == 0:
                            if self.automatas[i].getTransiciones()[b].geteInicial().getInicio()==True:
                                #print("reconozco el inicio")
                                bandera+=1                                                                
                                final = self.automatas[i].getTransiciones()[b].geteFinal().getNameE()
                                transicion = self.automatas[i].getTransiciones()[b].geteInicial().getNameE()+","+self.automatas[i].getTransiciones()[b].getLeer()+","+self.automatas[i].getTransiciones()[b].getSacar()+";"+self.automatas[i].getTransiciones()[b].geteFinal().getNameE()+","+self.automatas[i].getTransiciones()[b].getGuardar()
                                if self.automatas[i].getTransiciones()[b].getGuardar() != '$':
                                    self.automatas[i].getPila().append(self.automatas[i].getTransiciones()[b].getGuardar())
                                ruta.append(transicion)                                
                                break
                                #print("aceptacion transicion 1" + str(self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()))
                                #input("pasa en el inicial")                            
                        else:
                            if final == self.automatas[i].getTransiciones()[b].geteInicial().getNameE():
                                if cadena[a]==self.automatas[i].getTransiciones()[b].getLeer():
                                    #print("reconozco las demas transiciones")
                                    #aceptamos = self.automatas[i].getTransiciones()[b].geteFinal().getAcepta()
                                    final = self.automatas[i].getTransiciones()[b].geteFinal().getNameE()
                                    transicion = self.automatas[i].getTransiciones()[b].geteInicial().getNameE()+","+self.automatas[i].getTransiciones()[b].getLeer()+","+self.automatas[i].getTransiciones()[b].getSacar()+";"+self.automatas[i].getTransiciones()[b].geteFinal().getNameE()+","+self.automatas[i].getTransiciones()[b].getGuardar()
                                    ruta.append(transicion)
                                    #print(self.automatas[i].getPila())
                                    if self.automatas[i].getTransiciones()[b].getGuardar() != '$':
                                        self.automatas[i].getPila().append(self.automatas[i].getTransiciones()[b].getGuardar())
                                    if self.automatas[i].getTransiciones()[b].getSacar() != '$':
                                        try:
                                            self.automatas[i].getPila().remove(self.automatas[i].getTransiciones()[b].getSacar())
                                        except:
                                            pass
                                            #input("algo salió mal")
                                            banderazo+=1
                                    break
                                #print("aceptacion transicion " + str(b+1) + str(self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()))
                                #input("pasa en los demas transiciones")  
                                if cadena[a]=='#' and self.automatas[i].getTransiciones()[b].getLeer() =='$':
                                    #print("reconozco el final")
                                    #aceptamos = self.automatas[i].getTransiciones()[b].geteFinal().getAcepta()                                    
                                    transicion = self.automatas[i].getTransiciones()[b].geteInicial().getNameE()+","+self.automatas[i].getTransiciones()[b].getLeer()+","+self.automatas[i].getTransiciones()[b].getSacar()+";"+self.automatas[i].getTransiciones()[b].geteFinal().getNameE()+","+self.automatas[i].getTransiciones()[b].getGuardar()
                                    ruta.append(transicion)
                                    if self.automatas[i].getTransiciones()[b].getGuardar() != '$':
                                        self.automatas[i].getPila().append(self.automatas[i].getTransiciones()[b].getGuardar())
                                    if self.automatas[i].getTransiciones()[b].getSacar() != '$':
                                        #print('tengo que eliminar')
                                        try:    
                                            self.automatas[i].getPila().remove(self.automatas[i].getTransiciones()[b].getSacar())
                                        except:
                                            pass
                                    break
                #print(self.automatas[i].getPila())
                if len(self.automatas[i].getPila())==0 and banderazo == 0: 
                    aceptamos = True
                nuevaPila = []
                self.automatas[i].setPila(nuevaPila)
        return aceptamos, ruta
    
    def recorridoApaso(self):
        self.clrscr()
        entrada =""
        aceptamos = False
        ruta = []
        bandera = 0        
        final = ""
        banderazo = 0
        name = self.listarAP()
        for i in range(len(self.automatas)):
            if name == self.automatas[i].getName():
                cadena ="#"
                cadena += input("Ingrese la cadena a evaluar: ")                
                cadena+='#'                
                #for para la cadena ingresada
                for a in range(cadena.__len__()):
                    #print("empezamos con el for de la cadena")
                    #for para recorrer las transiciones del automata
                    for b in range(len(self.automatas[i].getTransiciones())):
                        #print("empezamos con el for de las transiciones")
                        if bandera == 0:
                            if self.automatas[i].getTransiciones()[b].geteInicial().getInicio()==True:
                                #print("reconozco el inicio")
                                bandera+=1                                                                
                                final = self.automatas[i].getTransiciones()[b].geteFinal().getNameE()
                                transicion = self.automatas[i].getTransiciones()[b].geteInicial().getNameE()+","+self.automatas[i].getTransiciones()[b].getLeer()+","+self.automatas[i].getTransiciones()[b].getSacar()+";"+self.automatas[i].getTransiciones()[b].geteFinal().getNameE()+","+self.automatas[i].getTransiciones()[b].getGuardar()
                                if self.automatas[i].getTransiciones()[b].getGuardar() != '$':
                                    self.automatas[i].getPila().append(self.automatas[i].getTransiciones()[b].getGuardar())
                                ruta.append(transicion)
                                self.generarGrafo(name,self.automatas[i].getTransiciones()[b].geteInicial().getNameE(),self.automatas[i].getTransiciones()[b].geteFinal().getNameE(),a,str(self.automatas[i].getPila()),entrada)
                                input('Presione enter para postrar la siguiente imagen.')
                                break
                                #print("aceptacion transicion 1" + str(self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()))
                                #input("pasa en el inicial")                            
                        else:
                            if final == self.automatas[i].getTransiciones()[b].geteInicial().getNameE():
                                if cadena[a]==self.automatas[i].getTransiciones()[b].getLeer():
                                    entrada+=cadena[a]
                                    #print("reconozco las demas transiciones")
                                    #aceptamos = self.automatas[i].getTransiciones()[b].geteFinal().getAcepta()
                                    final = self.automatas[i].getTransiciones()[b].geteFinal().getNameE()
                                    transicion = self.automatas[i].getTransiciones()[b].geteInicial().getNameE()+","+self.automatas[i].getTransiciones()[b].getLeer()+","+self.automatas[i].getTransiciones()[b].getSacar()+";"+self.automatas[i].getTransiciones()[b].geteFinal().getNameE()+","+self.automatas[i].getTransiciones()[b].getGuardar()
                                    ruta.append(transicion)
                                    #print(self.automatas[i].getPila())
                                    if self.automatas[i].getTransiciones()[b].getGuardar() != '$':
                                        self.automatas[i].getPila().append(self.automatas[i].getTransiciones()[b].getGuardar())
                                    if self.automatas[i].getTransiciones()[b].getSacar() != '$':
                                        try:
                                            self.automatas[i].getPila().remove(self.automatas[i].getTransiciones()[b].getSacar())
                                        except:
                                            pass
                                            #input("algo salió mal")
                                            banderazo+=1
                                    self.generarGrafo(name,self.automatas[i].getTransiciones()[b].geteInicial().getNameE(),self.automatas[i].getTransiciones()[b].geteFinal().getNameE(),a,str(self.automatas[i].getPila()),entrada)
                                    input('Presione enter para postrar la siguiente imagen.')
                                    break
                                #print("aceptacion transicion " + str(b+1) + str(self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()))
                                #input("pasa en los demas transiciones")  
                                if cadena[a]=='#' and self.automatas[i].getTransiciones()[b].getLeer() =='$':
                                    #print("reconozco el final")
                                    #aceptamos = self.automatas[i].getTransiciones()[b].geteFinal().getAcepta()                                    
                                    transicion = self.automatas[i].getTransiciones()[b].geteInicial().getNameE()+","+self.automatas[i].getTransiciones()[b].getLeer()+","+self.automatas[i].getTransiciones()[b].getSacar()+";"+self.automatas[i].getTransiciones()[b].geteFinal().getNameE()+","+self.automatas[i].getTransiciones()[b].getGuardar()
                                    ruta.append(transicion)
                                    if self.automatas[i].getTransiciones()[b].getGuardar() != '$':
                                        self.automatas[i].getPila().append(self.automatas[i].getTransiciones()[b].getGuardar())
                                    if self.automatas[i].getTransiciones()[b].getSacar() != '$':
                                        #print('tengo que eliminar')
                                        try:    
                                            self.automatas[i].getPila().remove(self.automatas[i].getTransiciones()[b].getSacar())
                                        except:
                                            pass
                                        self.generarGrafo(name,self.automatas[i].getTransiciones()[b].geteInicial().getNameE(),self.automatas[i].getTransiciones()[b].geteFinal().getNameE(),a,str(self.automatas[i].getPila()),entrada)
                                        input('Presione enter para postrar la siguiente imagen.')
                                    break
                #print(self.automatas[i].getPila())
                if len(self.automatas[i].getPila())==0 and banderazo == 0: 
                    aceptamos = True
                nuevaPila = []
                pilaa = ""
                pilaa = str(self.automatas[i].getPila())+"\n"
                self.automatas[i].setPila(nuevaPila)
                for i in range(len(self.automatas)):
                    if name == self.automatas[i].getName():
                        f = Digraph(filename = 'Fin', format='png', encoding='UTF-8')
                        f.attr(rankdir = 'LR')                
                        for a in range(len(self.automatas[i].getEstados())):
                            if self.automatas[i].getEstados()[a].getAcepta()==False:                                                        
                                f.attr('node',shape = 'circle',style='filled', color='grey')
                                f.node(self.automatas[i].getEstados()[a].getNameE())
                            else:                                
                                f.attr('node', shape = 'doublecircle', style='filled', color='gold')
                                f.node(self.automatas[i].getEstados()[a].getNameE())

                        for k in range(len(self.automatas[i].getTransiciones())):                            
                            transicion = self.automatas[i].getTransiciones()[k].getLeer()+","+self.automatas[i].getTransiciones()[k].getSacar()+";"+self.automatas[i].getTransiciones()[k].getGuardar()
                            f.edge(self.automatas[i].getTransiciones()[k].geteInicial().getNameE(),self.automatas[i].getTransiciones()[k].geteFinal().getNameE(), label=transicion)
                        if aceptamos==True:
                            pilaa +="Cadena valida"
                            f.attr(label = pilaa)
                        else:
                            pilaa+="Cadena invalida"
                            f.attr(label =pilaa)
                        f.view()

    def generarGrafo(self, name, inicio, final,indice, pila, entrada):
        for i in range(len(self.automatas)):
            if name == self.automatas[i].getName():
                f = Digraph(filename = str(indice), format='png', encoding='UTF-8')
                f.attr(rankdir = 'LR')                
                texto=""
                texto+="Pila: "+pila+"\n"
                texto+="Entrada: "+entrada+"\n"
                f.attr(label=texto)
                for a in range(len(self.automatas[i].getEstados())):
                    if self.automatas[i].getEstados()[a].getAcepta()==False:                        
                        if inicio == self.automatas[i].getEstados()[a].getNameE():
                            f.attr('node',shape = 'circle', style='filled', color='gold')
                            f.node(self.automatas[i].getEstados()[a].getNameE())
                        else:
                            f.attr('node',shape = 'circle',style='filled', color='grey')
                            f.node(self.automatas[i].getEstados()[a].getNameE())
                    else:
                        if inicio == self.automatas[i].getEstados()[a].getNameE():
                            f.attr('node', shape = 'doublecircle',style='filled', color='gold')
                            f.node(self.automatas[i].getEstados()[a].getNameE())
                        else:
                            f.attr('node', shape = 'doublecircle', style='filled', color='grey')
                            f.node(self.automatas[i].getEstados()[a].getNameE())

                for k in range(len(self.automatas[i].getTransiciones())):
                    if inicio == self.automatas[i].getTransiciones()[k].geteInicial().getNameE() and final == self.automatas[i].getTransiciones()[k].geteFinal().getNameE():                        
                        transicion = self.automatas[i].getTransiciones()[k].getLeer()+","+self.automatas[i].getTransiciones()[k].getSacar()+";"+self.automatas[i].getTransiciones()[k].getGuardar()
                        f.edge(self.automatas[i].getTransiciones()[k].geteInicial().getNameE(),self.automatas[i].getTransiciones()[k].geteFinal().getNameE(), label=transicion, color = 'red')
                    else:
                        transicion = self.automatas[i].getTransiciones()[k].getLeer()+","+self.automatas[i].getTransiciones()[k].getSacar()+";"+self.automatas[i].getTransiciones()[k].getGuardar()
                        f.edge(self.automatas[i].getTransiciones()[k].geteInicial().getNameE(),self.automatas[i].getTransiciones()[k].geteFinal().getNameE(), label=transicion)
                f.view()

    def validarPasada(self):        
        self.clrscr()
        print("****** Validar cadena de una pasada ******")
        name = self.listarAP()        
        for i in range(len(self.automatas)):
            if name == self.automatas[i].getName():
                nombre = name+".pdf"
                c = canvas.Canvas(nombre)
                #parte donde agrego los detalles        
                titulo = "Nombre: "+name
                c.setFontSize(20)
                c.drawString(225,750,titulo)
                c.setFontSize(12)
                archivo = open(name+".dot", 'w')
                archivo.write("digraph A {\n")
                archivo.write("shape = plaintext\n")
                archivo.write("label=<\n")
                archivo.write("<table border='0' cellborder='1' cellspacing='0'>\n")
                archivo.write("<tr><td>Iteracion</td><td>Pila</td><td>Entrada</td><td>Transicion</td></tr>\n")
                #start
                aceptamos = False
                ruta = []
                bandera = 0        
                final = ""
                banderazo = 0
                #alv
                entrada = ""
                cadena ="#"
                cadena += input("Ingrese la cadena a evaluar: ")                
                cadena+='#'                
                #for para la cadena ingresada
                for a in range(cadena.__len__()):
                    #print("empezamos con el for de la cadena")
                    #for para recorrer las transiciones del automata
                    for b in range(len(self.automatas[i].getTransiciones())):
                        #print("empezamos con el for de las transiciones")
                        if bandera == 0:
                            if self.automatas[i].getTransiciones()[b].geteInicial().getInicio()==True:
                                #print("reconozco el inicio")
                                bandera+=1                                                                
                                final = self.automatas[i].getTransiciones()[b].geteFinal().getNameE()
                                transicion = self.automatas[i].getTransiciones()[b].geteInicial().getNameE()+","+self.automatas[i].getTransiciones()[b].getLeer()+","+self.automatas[i].getTransiciones()[b].getSacar()+";"+self.automatas[i].getTransiciones()[b].geteFinal().getNameE()+","+self.automatas[i].getTransiciones()[b].getGuardar()
                                if self.automatas[i].getTransiciones()[b].getGuardar() != '$':
                                    self.automatas[i].getPila().append(self.automatas[i].getTransiciones()[b].getGuardar())
                                ruta.append(transicion)
                                archivo.write("<tr><td>"+str(a)+"</td><td>"+str(self.automatas[i].getPila())+"</td><td></td><td>"+transicion+"</td></tr>\n")
                                break
                                #print("aceptacion transicion 1" + str(self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()))
                                #input("pasa en el inicial")                            
                        else:
                            if final == self.automatas[i].getTransiciones()[b].geteInicial().getNameE():
                                if cadena[a]==self.automatas[i].getTransiciones()[b].getLeer():
                                    entrada+=cadena[a] 
                                    #print("reconozco las demas transiciones")
                                    #aceptamos = self.automatas[i].getTransiciones()[b].geteFinal().getAcepta()
                                    final = self.automatas[i].getTransiciones()[b].geteFinal().getNameE()
                                    transicion = self.automatas[i].getTransiciones()[b].geteInicial().getNameE()+","+self.automatas[i].getTransiciones()[b].getLeer()+","+self.automatas[i].getTransiciones()[b].getSacar()+";"+self.automatas[i].getTransiciones()[b].geteFinal().getNameE()+","+self.automatas[i].getTransiciones()[b].getGuardar()
                                    ruta.append(transicion)
                                    #print(self.automatas[i].getPila())
                                    if self.automatas[i].getTransiciones()[b].getGuardar() != '$':
                                        self.automatas[i].getPila().append(self.automatas[i].getTransiciones()[b].getGuardar())
                                    if self.automatas[i].getTransiciones()[b].getSacar() != '$':
                                        try:
                                            self.automatas[i].getPila().pop()
                                        except:
                                            pass
                                            #input("algo salió mal")
                                            banderazo+=1
                                    archivo.write("<tr><td>"+str(a)+"</td><td>"+str(self.automatas[i].getPila())+"</td><td>"+entrada+"</td><td>"+transicion+"</td></tr>\n")
                                    break
                                #print("aceptacion transicion " + str(b+1) + str(self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()))
                                #input("pasa en los demas transiciones")  
                                if cadena[a]=='#' and self.automatas[i].getTransiciones()[b].getLeer() =='$':
                                    #print("reconozco el final")
                                    #aceptamos = self.automatas[i].getTransiciones()[b].geteFinal().getAcepta()                                    
                                    transicion = self.automatas[i].getTransiciones()[b].geteInicial().getNameE()+","+self.automatas[i].getTransiciones()[b].getLeer()+","+self.automatas[i].getTransiciones()[b].getSacar()+";"+self.automatas[i].getTransiciones()[b].geteFinal().getNameE()+","+self.automatas[i].getTransiciones()[b].getGuardar()
                                    ruta.append(transicion)
                                    if self.automatas[i].getTransiciones()[b].getGuardar() != '$':
                                        self.automatas[i].getPila().append(self.automatas[i].getTransiciones()[b].getGuardar())
                                    if self.automatas[i].getTransiciones()[b].getSacar() != '$':
                                        #print('tengo que eliminar')
                                        try:    
                                            self.automatas[i].getPila().pop()
                                        except:
                                            pass
                                    archivo.write("<tr><td>"+str(a)+"</td><td>"+str(self.automatas[i].getPila())+"</td><td>"+entrada+"</td><td>"+transicion+"</td></tr>\n")
                                    break
                #print(self.automatas[i].getPila())
                if len(self.automatas[i].getPila())==0 and banderazo == 0: 
                    aceptamos = True
                nuevaPila = []
                self.automatas[i].setPila(nuevaPila)
                
                #end
                if aceptamos==True:                    
                    archivo.write("<tr><td colspan='4'>Cadena valida</td></tr>\n")
                else:
                    archivo.write("<tr><td colspan='4'>Cadena invalida</td></tr>\n")
                archivo.write("</table>\n")
                archivo.write(">\n")
                archivo.write("}")
                archivo.close()
                os.system('dot -Tpng '+ name+'.dot -o '+name+'.png')
                pato=name+".png"                
                c.drawImage(pato,110,440)
                c.save()
                os.system(nombre)
                #input("perate")
                