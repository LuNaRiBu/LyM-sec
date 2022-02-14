import os

class Contacto: 
    def __init__(self, pNombre, apellido,telefono,correo, nPoliza):
        self.nombre = pNombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.nPoliza = nPoliza
    def __str__(self):
        return f"Nombre = {self.nombre}, {self.apellido} Tel: {self.telefono}, Correo electronico: {self.correo} Poliza N° {self.nPoliza}"
    
    def getNombre (self):
        return self.nombre
    
    def getApellido (self):
        return self.apellido      

    def setNombre (self, nNombre):
        self.nombre = nNombre

    def setApellido (self, nApellido):
        self.apellido = nApellido   

    def setTel (self, nTel):
        self.telefono = nTel

    def setMail (self, nMail):
        self.correo = nMail
    
    def setPoli (self, nPoli):
        self.nPoliza = nPoli


def agregar():
     nombre = input("Ingrese nombre: ")
     apellido = input("Ingrese apellido: ")
     telefono = input("ingrese teléfono: ")
     correo = input("Ingrese correo: ")
     poliza = input("Ingrese el número de poliza: ")
     contacto_Nuevo = Contacto(nombre,apellido,telefono,correo,poliza)
     listaContactos.append(contacto_Nuevo)


def ver_Contacto():
    print (" ")
    print("Contactos")
    for i in range (0, len(listaContactos)):
        print(f"{i + 1} -- {listaContactos[i]}")



def borrar():
    ver_Contacto()
    indice = int(input("Ingrese el número de contacto que desea borrar:  "))   
    print(f"Esta seguro que desea eliminar a {listaContactos[indice - 1].getNombre()} {listaContactos[indice - 1].getApellido()}")
    rta = input("""y = Borrar...
n = No borrar...  """) 
    if (rta == "y"):
        listaContactos.remove(listaContactos[indice - 1])


def modificar():
    ver_Contacto()
    indice = int(input("Ingrese el número de contacto que desea modificar:  "))   
    nombre = input("Ingrese el nuevo nombre: ")
    listaContactos[indice - 1].setNombre(nombre)
    


#Programa
listaContactos = [ ]

opcion = " "
while(opcion != "x"):
    print("------ AGENDA------")
    print("1 - Agregar Contactos")
    print("2 - Modificar Contactos")
    print("3 - Ver contactos")
    print("4 - Borrar Contactos")
    print("x - Salir ")
    opcion = input("ingrese la opción deseada, para salir presione X ... ")
    if(opcion == "x"):
        print("Gracias y vuelva prontos")
    
    elif(opcion == "1"):
        agregar()
    
    elif (opcion == "2"):
        modificar()

    elif (opcion == "3"):
        ver_Contacto()

    elif (opcion =="4"):
        borrar()  
    else:
        print("Elija una opción que corresponda!!")


