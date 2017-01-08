
# coding: utf-8

# In[10]:

class Saludo (object):
    nombre = 'Manuel'
    apellidos = 'Hidalgo Manzano'
    def saludar (self):
        print "Hola. Soy ", self.nombre, ' ', self.apellidos
objeto = Saludo()
objeto.saludar()


# In[11]:

class Calculadora (object):
    op1 = None
    op2 = None
    def __init__ (self, operando1, operando2):
        self.op1 = operando1
        self.op2 = operando2
    def sumar (self):
        return self.op1 + self.op2
    def resta (self):
        return self.op1 - self.op2
    def multiplicar (self):
        return self.op1 * self.op2
    
o = Calculadora(10, 2)
o.sumar()


# In[12]:




# In[15]:

class Madre (object):
    par1 = None
    def __init__(self, parametro1):
        self.par1 = parametro1
    def metodo1 (self):
        print "metodo1 de la clase Madre"
    def metodo2 (self):
        print "metodo de la clase Madre"
        
class Hija (Madre):
    def metodo1 (self):
        print "metodo1 de la clase Hija"
        
objeto_hija = Hija(24)
objeto_hija.par1

objeto_hija.metodo1()

objeto_hija.metodo2()


# In[25]:

#ejercicio 20 de las diapos

class Cuenta(object):
    

    def __init__ (self, sal, ing, ret):
        self.saldo = sal
        self.ingresar = ing
        self.retirar= ret

    def ingresar (self):
        
        return self.saldo+self.ingresar
    def retirar (self):
       
        return self.saldo-self.retirar


sal = 0
print "Pulse 1 para Ingresar cantidad: "
print "Pulse 2 para Retirar cantidad: "
print "Pulse 3 para Salir"
opciones= raw_input("Elija una opcion")
while True:
    if opciones == 1:
        ing =input("Ingresar cantidad: ")
        o = Cuenta (sal, ing, ret)
        sal=o.ingresar()
        print sal
    elif opciones == 2:
        ret = input ("Retirar cantidad: ")
        o = Cuenta (sal, ing, ret)
        sal=o.retirar()
        print sal
    elif opciones == 3:
        break
    
    
    


# In[30]:

#ejercicio 20 diapos
class Cuenta (object):
    def __init__(self,cantidad):
        self.saldo = float(cantidad)
        
    def ingresar (self, cantidad):
        self.saldo = self.saldo+cantidad
        #return self.saldo
    def retirar (self, cantidad):
        self.saldo = self.saldo - cantidad
        #return self.saldo
saldo=0
objeto_cuenta = Cuenta(saldo)
while True:
    
   
    print "Pulse 1 para Ingresar cantidad: "
    print "Pulse 2 para Retirar cantidad: "
    print "Pulse 3 para Salir"
    opciones = input('selecione una opcion: ') 
    if opciones == 1:
        cantidad = input('cantidad a ingresar: ')
        objeto_cuenta.ingresar(cantidad)
        print objeto_cuenta.saldo
            
    elif opciones == 2:
        cantidad = input('cantidad a retirar: ')
        objeto_cuenta.retirar(cantidad)
        print objeto_cuenta.saldo
    
    elif opciones == 3:
        break
        
    
    


# In[29]:

# ejercicio 20 diapos (resuelto profesor)
class Cuenta (object):
    def __init__(self, cantidad):
        self.saldo = float(cantidad)
    def ingresar (self, cantidad):
        self.saldo = self.saldo+cantidad
        return self.saldo
    def retirar (self, cantidad):
        self.saldo = self.saldo - cantidad
        return self.saldo
    
objeto_cuenta = Cuenta(0.0)
print 'Cuenta recien creada : saldo: ', objeto_cuenta.saldo
objeto_cuenta.ingresar(125.23)
print 'saldo actual: ', objeto_cuenta.saldo

    


# In[ ]:

# ejercicio 23 diapos (resuelto profesor)

class Cuenta (object):
    def __init__(self,cantidad):
        self.saldo = float(cantidad)
        
    def ingresar (self, cantidad):
        self.saldo = self.saldo+cantidad
        #return self.saldo
    def retirar (self, cantidad):
        self.saldo = self.saldo - cantidad
        #return self.saldo
        
class Cuenta_ahorro (Cuenta):
    def retirar (self, cantidad):
        
        if self.saldo<0.0:
            print 'No tiene credito' 
        else:
            self.saldo = self.saldo - cantidad
            
    
    def avisar (self):
        if self.saldo<0.0:
            print 'Numeros rojos'
saldo=0
objeto_cuenta = Cuenta_ahorro(saldo)
while True:
    if saldo<0.0:
        objeto_cuenta.avisar()
   
    print "Pulse 1 para Ingresar cantidad: "
    print "Pulse 2 para Retirar cantidad: "
    print "Pulse 3 para Salir"
    opciones = input('selecione una opcion: ') 
    if opciones == 1:
        cantidad = input('cantidad a ingresar: ')
        objeto_cuenta.ingresar(cantidad)
        print objeto_cuenta.saldo
            
    elif opciones == 2:
        cantidad = input('cantidad a retirar: ')
        objeto_cuenta.retirar(cantidad)
        print objeto_cuenta.saldo
    
    elif opciones == 3:
        break


# In[ ]:

#ejercicio 21 diapos
class Fichero(object):
    


# In[ ]:



