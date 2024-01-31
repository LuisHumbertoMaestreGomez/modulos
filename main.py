import json
from os import system
import modulo.camper as camper
import modulo.trainer as trainer
from modulo.validar import menunovalido
def menu():
    print("sistema de almecenamiento de datos para campus")
    print("\t1.Informacion del camper") 
    print("\t2.Informacion del treiner")
    print("\t0. salir ")
bandera = True
while (bandera):
    menu()
    opc = int(input())
    match(opc):
        case 1:

          with open("modulo/storage/camper.json", "r") as f:
                camper.camper = json.loads(f.read())
                f.close()
                system("clear")
                camper.menu()
        case 2:
            system("clear")
            trainer.menu()
        case 0:
             system("clear")
             bandera = False
        case _:
            menunovalido(opc)
