from os import system
from .data import camper, generos
from .validar import menunovalido
def save():
    info = {
        "nombre": input("ingrese el nombre del camper\n"),
        "Apellido": input("Ingrese el apellido del camper\n"),
        "Edad": int(input("Ingrese la edad del camper\n")),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))

    }
   
    camper.append(info)
    return f"sucessfully camper "
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

            

