import os

class Contacto: 
    def __init__(self, pNombre, apellido,telefono,correo, nPoliza):
        self.nombre = pNombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.nPoliza = nPoliza
    def __str__(self):
        return f"Nombre = {self.nombre}, {self.apellido} Tel: {self.telefono})"
            


def agregar():
     nombre = input("Ingrese nombre: ")
     apellido = input("Ingrese apellido: ")
     telefono = input("ingrese teléfono: ")
     correo = input("Ingrese correo: ")
     poliza = input("Ingrese el número de poliza: ")
     contacto_Nuevo = Contacto(nombre,apellido,telefono,correo,poliza)
     listaContactos.append(contacto_Nuevo)


listaContactos = []
opcion = " "
while(opcion != "x"):
    print("------ AGENDA------")
    print("1 - Agregar Contactos")
    print("2 - Modificar Contactos")
    print("3 - Ver contactos")
    print("4 - Borrar Contactos")
    print("5 - Salir ")
    opcion = input("ingrese la opción deseada, para salir presione X  ")
    if(opcion == "x"):
        print("Gracias y vuelva prontos")
    
    if(opcion == "1"):
        agregar()
    else:
        print("Elija una opción que corresponda!!")


