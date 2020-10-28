class Aefede(object):
    def __init__(self, name):        
        self.nombre = name
        self.estados= []
        self.alfabeto = []        
        self.eAceptacion = []
        self.transiciones = []
        self.pila = []
        self.simbolosPila = []
    
    #getters
    def getName(self):
        return str(self.nombre)
    def getEstados(self):
        return self.estados
    def getAlfabeto(self):
        return self.alfabeto
    def getTransiciones(self):
        return self.transiciones
    def getPila(self):
        return self.pila
    def getSimbolosPila(self):
        return self.simbolosPila

    #setters
    def setName(self, valor):
        self.nombre = valor
    def seteInicial(self, valor):
        self.eInicial = valor
    def setPila(self,valor):
        self.pila=valor


class Transicion(object):
    def __init__(self, inicial, leer, sacar, final, guardar):
        self.eInicial = inicial
        self.eFinal = final
        self.leer = leer
        self.sacar = sacar
        self.guardar = guardar
    #getters
    def geteInicial(self):
        return self.eInicial
    def geteFinal(self):
        return self.eFinal
    def getLeer(self):
        return str(self.leer)  
    def getSacar(self):
        return str(self.sacar)
    def getGuardar(self):
        return str(self.guardar)

class Estado(object):
    def __init__(self, nombre):
        self.name = nombre
        self.aceptacion = False
        self.inicio = False
        
    #Getters
    def getNameE(self):
        return str(self.name)
    def getAcepta(self):
        return self.aceptacion
    def getInicio(self):
        return self.inicio    

    def setSalidas(self,valor):
        self.salidas=valor
    def setAcepta(self, valor):
        self.aceptacion = valor
    def setInicio(self, valor):
        self.inicio = valor
    def setAlto(self, valor):
        self.alto = valor
#frontera
#frontera
#fabrica de gramaticas
class Gramatica(object):
    def __init__(self, name):
        self.nombre = name
        self.noTerms = []
        self.terminales = []        
        self.producciones = []
        self.tipo3 = False
    
    #getters
    def getName(self):
        return str(self.nombre)
    def getNoTerms(self):
        return self.noTerms
    def getTerminales(self):
        return self.terminales    
    def getProducciones(self):
        return self.producciones
    def getTipo3(self):
        return self.tipo3
    
    #setters    
    def setTerminales(self,valor):
        self.terminales=valor
    def setTipo3(self,valor):
        self.tipo3 = valor

class noTerminal(object):
    def __init__(self, nombre):
        self.name = nombre        
        self.inicio = False        
        
    #getters
    def getName(self):
        return str(self.name)    
    def getInicio(self):
        return self.inicio
    
    def setInicio(self, valor):
        self.inicio=valor      

class Produccion (object):
    def __init__(self, inicial,derivar):
        self.tInicial = inicial        
        self.derivacion = derivar
        self.yapaso = False
    #getters
    def gettInicial(self):
        return self.tInicial
    def getDerivacion(self):
        return self.derivacion
    def getYapaso(self):
        return self.yapaso
    #setters
    def setYapaso(self, valor):
        self.yapaso = valor

class Conexion(object):
    def __init__(self,inicio, siguiente):
        self.inicio = inicio
        self.siguiente = siguiente

    #getters
    def getInicio(self):
        return str(self.inicio)
    def getSiguiente(self):
        return str(self.siguiente)

class Control(object):
    def __init__(self,ancla, nodo):
        self.ancla = ancla
        self.nodo = nodo

    #getters
    def getAncla(self):
        return str(self.ancla)
    def getNodo(self):
        return str(self.nodo)
        