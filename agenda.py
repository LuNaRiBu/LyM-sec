import os

class Contacto: 
    def __init__(self, pNombre, apellido,telefono,correo, nPoliza):
        self.nombre = pNombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.nPoliza = nPoliza
    def __str__(self):
        return f"Nombre = {self.nombre}, {self.apellido} Tel: {self.telefono}, Correo electronico: {self.correo} Poliza N° {self.nPoliza})"
            


def agregar():
     nombre = input("Ingrese nombre: ")
     apellido = input("Ingrese apellido: ")
     telefono = input("ingrese teléfono: ")
     correo = input("Ingrese correo: ")
     poliza = input("Ingrese el número de poliza: ")
     contacto_Nuevo = Contacto(nombre,apellido,telefono,correo,poliza)
     listaContactos.append(contacto_Nuevo)


def ver_Contacto():

    for contacto in listaContactos:
        print(contacto)


#Programa
listaContactos = []
opcion = " "
while(opcion != "x"):
    print("------ AGENDA------")
    print("1 - Agregar Contactos")
    print("2 - Modificar Contactos")
    print("3 - Buscar Contacto")
    print("4 - Ver contactos")
    print("5 - Borrar Contactos")
    print("x - Salir ")
    opcion = input("ingrese la opción deseada, para salir presione X ... ")
    if(opcion == "x"):
        print("Gracias y vuelva prontos")
    
    elif(opcion == "1"):
        agregar()
    
    
    elif (opcion == "4"):
        ver_Contacto()
    else:
        print("Elija una opción que corresponda!!")


