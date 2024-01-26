from os import system
from .data import camper
from .validar import menunovalido
def save(nombre):
    camper.append(nombre)
    return f"sucessfully camper {nombre} "
def edit():
    return "edit to treiner"
def search():
    return "the camper is avalible"
def delete():
    return "camper deleted"
def menu():
    bandera = True
    while (bandera):
        print("CRUD del camper")
        print("\t1. guardar camper")
        print("\t2. buscar  camper")
        print("\t3. actualizar camper")
        print("\t4. eliminar camper")
        print("\t0. atras")
        opc = int(input())
        match(opc):
            case 1:
                save()
            case 0:
                system("clear")
                bandera = False
            case _:
                menunovalido(opc)

            

