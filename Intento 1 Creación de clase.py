
class Album :
    Grupos = ["GrupoA", "GrupoB", "GrupoC","GrupoD", "GrupoE", "GrupoF","GrupoG", "GrupoH"]
    Otros = ["Especiales", "Leyenda", "Estadios", "Sedes"]
    Selecciones = []
    
    def __init__(self, Grupos, Seleccion):
        if Seleccion in self.Seleccion:
            self.Seleccion = Seleccion 
        else:
            print("Esta selección no hizo parte del mundial")
            
 #Creación de los Grupos

class Grupo:
    
    def __init__(self, Grupo):
        self.Grupo = []
        self.Seleccion = Seleccion
        
    def agregar (self, Seleccion):
        self.Seleccion.append(Seleccion)
    
    def __str__(self):
        msn =""
        for Seleccion in self.Seleccion:
            msn += str(Seleccion)+ "\n"
        return msn 

    
    


