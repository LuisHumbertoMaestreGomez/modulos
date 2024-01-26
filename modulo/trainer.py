from os import system
from .data import trainer
from .validar import menunovalido
def save():
    return "sucessfully treiner"
def edit():
    return "edit to treiner"
def search():
    return "the treiner is avalible"
def delete():
    return "treiner deleted"
def menu():
    bandera = True
    while (bandera):
        print("CRUD del camper")
        print("\t1. guardar trainer")
        print("\t2. buscar  trainer")
        print("\t3. actualizar trainer")
        print("\t4. eliminar trainer")
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

            

