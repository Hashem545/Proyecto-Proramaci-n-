# -*- coding: utf-8 -*-
"""
Created on Sat May 22 16:37:09 2021

@author: santiago.fernandez
"""

## Arreglo de la base de datos 
Lista = open("LaminasRusia.txt" ,"r")
Datos = Lista.readlines()
Album = [i.strip("()").split("\t") for i in Datos]
##Creación de la clase
class Lamina:
    """Crea objetos que tienen equipo, nombre y numero"""
    def __init__(self, 
                 equipo="Team",  Numero = "Numero",Nombre= "Nombre",Cantidad=0):
        self. equipo= equipo
        self.Nombre=Nombre
        self.Numero= Numero
        self.Cantidad= Cantidad
    def Ingreso(self, valor):
        self.Cantidad += valor 
        
    def Retiro (self, valor):
        self.Cantidad -= valor 
Album1 = []
for i in Album:
    Album1.append(Lamina(i[0],i[1],i[2],0))
Llenas=[]
Repet=[]

##Funciones
#### Agregar
def Agregar(number):
    if Album1[number-1].Cantidad ==0:
      Llenas.append(Album1[number-1])
    else:
      Repet.append(Album1[number-1])        
    Album1[number-1].Ingreso(1)
### Agregar varias láminas
def AgregarV():
    nuevas = []
    while True:
        nueva = input("Ingrese el número de su lámina (si desea terminar ingrese YA)\n") 
        if nueva == "YA":
            break
        nuevas.append(int(nueva))
    for i in nuevas:
        if Album1[i-1].Cantidad ==0:
            Llenas.append(Album1[i-1])
        elif Album1[i-1] in Llenas:
            Repet.append(Album1[i-1])        
    Album1[i-1].Ingreso(1) 
#### Quitar
def Quitar(number):
    if Album1[number -1] in Repet:
         Repet.remove(Album1[number -1])
        #Llenas.pop(Album1[number-1])
    elif Album1[number -1] in Llenas:
        Llenas.remove(Album1[number -1])
    else :
        print("No tiene esta lámina")
    Album1[number -1].Retiro(1)
#### Ver faltantes 
def Faltan():
    print("Faltan ",len(Album)-len(Llenas), " láminas de ", len(Album))
    
#### Ver repetidas
def Repetidas():    
    for i in Repet:
        print (Album[i].Numero)
### Describir
def Describir(number):
    print("La lámina ", Album1[number-1].Numero,
              "es de",Album1[number-1].Nombre, " de "
              ,Album1[number-1].equipo," tienes ",Album1[number-1].Cantidad)
