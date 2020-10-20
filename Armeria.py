class Aefede(object):
    def __init__(self, name):        
        self.nombre = name
        self.estados= []
        self.alfabeto = []        
        self.eAceptacion = []
        self.transiciones = []
    
    #getters
    def getName(self):
        return str(self.nombre)
    def getEstados(self):
        return self.estados
    def getAlfabeto(self):
        return self.alfabeto
    def geteInicial(self):
        return self.eInicial
    def geteAceptacion(self):
        return self.eAceptacion
    def getTransiciones(self):
        return self.transiciones

    #setters
    def setName(self, valor):
        self.nombre = valor
    def seteInicial(self, valor):
        self.eInicial = valor
    def setAlfabeto(self,valor):
        self.alfabeto=valor


class Transicion(object):
    def __init__(self, inicial, final, entra):
        self.eInicial = inicial
        self.eFinal = final
        self.entrada = entra 
    #getters
    def geteInicial(self):
        return self.eInicial
    def geteFinal(self):
        return self.eFinal
    def getEntrada(self):
        return str(self.entrada)  

class Estado(object):
    def __init__(self, nombre):
        self.name = nombre
        self.aceptacion = False
        self.inicio = False
        self.salidas= []
        self.alto = False
    #Getters
    def getNameE(self):
        return str(self.name)
    def getAcepta(self):
        return self.aceptacion
    def getInicio(self):
        return self.inicio
    def getSalidas(self):        
        return self.salidas
    def getAlto(self):
        return self.alto

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
    #getters
    def gettInicial(self):
        return self.tInicial
    def getDerivacion(self):
        return self.derivacion