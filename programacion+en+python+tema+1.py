
# coding: utf-8

# In[9]:

#ejercicio de repaso 5
def multiplicacion():
    num1 = input ("Introducir primer operando: ")
    num2 = input ("Introducir segundo oprando: ")
    print "El resultdo es: ", num1*num2

opcion = 0
while opcion <> 4:
    print "\n"
    print "Pulse 1 si quiere multiplicar dos numeros"
    print "Pulse 2 si quiere elevar un numero"
    print "Pulse 3 si quiere conocer el factorial de un numero"
    print "Pulse 4 si desea salir del programa"
    print " ".center(50,"-")
    opcion = input("Opcion: ")
    print opcion

    if opcion == 1:
        multiplicacion ()
    elif opcion == 2:
        print "opcion 2"
    elif opcion == 3:
        print "opcion 3"
    elif opcion == 4:
        print "opcion 4"
    else:
        print "opcion no valida"


# In[14]:

#ejercicio diapos 1
bases =["A", "C", "T", "G"]
print bases
bases.append("U")
print bases
bases.remove("U")
print bases
bases.sort()
print bases


# In[22]:

#ejercicio diapos 2
letras = ["A", "B", "C", "Z", "I", "H"]
print letras
letras2 = []
print letras2
for i in letras:
    letras2.append(i)
letras2.sort()
print "lista ordenada:", letras2
print letras


# In[35]:

#ejercicio diapos 3
size_lista = input("Introducir el tamaño de la lista: ")
lista =[None] * size_lista
num = 999
i = 0
while i< size_lista:
    num = input ("Introducir numero: ")

    lista.append(num)
    i = i +1
    print "EL numero mayor es: ", max(lista)


# In[8]:

#funcion para calcular el factorial de un numero
def factorial(n):
    if  n == 0 or n == 1 :
        return 1
    else:
        return n * factorial (n-1)

n = 8    
print factorial(n)


# In[55]:

#ejercicio diapos 7
#tiene que introducir toda la ruta (ruta absoluta), '/home/bioinfo/Escritorio/cuento.txt' sin comillas

f = open(raw_input("Introduzca nombre del fichero: "))
palabras = f.read()

lista=palabras.split()
diccionario={}
for i in lista:
    if i in diccionario:
        n= diccionario[i]
        n = n + 1
        diccionario[i]=n
        
    else:
        n=1
        diccionario[i]=n
for i, n in diccionario.items():
    print i, "esta repetido", n, "veces"


# In[73]:

#ejercicio diapos 8
f = open("/home/bioinfo/Escritorio/dna1.txt")

lineas = f.readline()
lineas = f.readline()
lineas = f.readline()
lineas = f.readline()
lineas = f.readline()

ADN = f.read()

ade=0
cit=0
tim=0
gua=0
for i in ADN:
    if i == 'a':
        ade = ade +1
    elif i == 'c':
        cit = cit +1
    elif i == 't':
        tim = tim + 1
    elif i == 'g':
        gua = gua +1
print "Adeninas: ", ade
print "Citosinas: ", cit
print "Timinas: ", tim
print "Guaninas: ", gua
Dic_amino = {"ttt": Phe, "ttc": Phe, "tta":leu, "ttg":Leu, "atg": Met, "tta": Stop, "tga": Stop, "tag": Stop}


# In[74]:

#ejemplos del modulo re
import re 
er = re.compile("Esto")
print er


# In[75]:

import re 
er = re.compile("Esto")
print er
print er.search('Esto es una prueba')


# In[76]:

import re 
er = re.compile("Esto")
print er
print er.search('Esto es una prueba')
print er.match('Esto es una prueba')


# In[77]:

import re 
er = re.compile("es")
print er
print er.search('Esto es una prueba')
print er.match('Esto es una prueba')


# In[80]:

import re 
er = re.compile("es")
print er
print er.search('Esto es una prueba')
print er.match('Esto es una prueba')
print re.search('es', 'Esto es una prueba')
print re.match('es', 'Esto es una prueba')
print re.split('es', 'Esto es una prueba')
print re.findall('es', 'Esto es una es prueba')
print re.sub('es', 'no es', 'Esto es una prueba')
print re.escape('Como te llamas?')


# In[82]:

import re 
er = re.compile("es")
print er
print re.findall('.s', 'Esto es una as prueba')


# In[98]:

#ejercicio de diapos 14
def traducir(ADN):
    import re
    ADN = raw_input("Introducir una cadena de ADN:")
    ARN=re.sub('T', 'U', ADN)
    return ARN              
           
traducir(ADN)


# In[97]:

import re
ADN = "ACCCTGGTGACCG"
ARN= re.sub('T', 'U', ADN)
print ADN 
print ARN


# In[106]:

import re
prog = re.compile("h[0-9].org")
result = prog.search('esto es un dato h4.org valido')
print result.group()

result = re.search('h[0-9].org', "esto es un dato h4.org valido")
print result.group()


# In[111]:

import re
m = re.match('www\.(.*)\..{3}', 'www.python.org')
print m.group(1)
print m.start(1)
print m.end(1)
print m.span(1)

print m.group()
print m.start()
print m.end()
print m.span()


# In[1]:

import re
m = re.match('www\.(.*)\.(.{3})', 'www.python.org')

print m.group(2)
print m.start(2)
print m.end(2)
print m.span(2)


# In[127]:

#ejercicio 16 de diapos
import re
palabra = raw_input("Intoduzca una palabra: ")
print palabra
perl = re.match('(\$)([a-z]*)', palabra)
if re.match('(\$)([a-z]*)', palabra):
    print "perl"
else:
    print "python"



# In[2]:

#ejercicio 17 de diapos
import re
numero = raw_input("Introduzca un numero: ")

validar2 = re.match('([0-9]*)(e|E|\.)(\+|\-|[0-9]*)([0-9])', numero)
if validar2 :
    print "numero valido"
    print validar2.group()
    validar2.group(1)
    validar2.group(2)
    validar2.group(3)
    validar2.group(4)
else:
    print "numero no valido"


    


# In[241]:

#ejercicio 18 de diapos
f =open('/home/bioinfo/Escritorio/genbank.gb')
lineas = f.readline()
primeras_lineas = open('/home/bioinfo/Escritorio/primeras_lineas.txt', 'w')
ADN = open('/home/bioinfo/Escritorio/ADN.txt', 'w')
contador = 0
for linea in f:
    if 'ORIGIN' not in linea and contador == 0:
        primeras_lineas = open('/home/bioinfo/Escritorio/primeras_lineas.txt', 'a')
        primeras_lineas.write(linea)
    if 'ORIGIN' in linea:
        contador = 1
        primeras_lineas = open('/home/bioinfo/Escritorio/primeras_lineas.txt', 'a')
        primeras_lineas.write(linea)
        primeras_lineas.close()
    if 'ORIGIN' not in linea and contador == 1:
        ADN = open('/home/bioinfo/Escritorio/ADN.txt', 'a')
        ADN.write(linea)
        ADN.close()
f.close()
import re

dna = open('/home/bioinfo/Escritorio/ADN.txt', 'r')


num_linea = 1
er = re.compile('tca')
for linea in dna:
    if er.search(linea):
        print 'tca aparece en la linea ', num_linea
    num_linea = num_linea + 1

    


   
  
    



# In[ ]:




# In[ ]:



