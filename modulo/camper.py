import json
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
    with open("modulo/storage/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
    return f"sucessfully camper "
def edit():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***************************
        * Acualizacion del camper *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del camper que deseas actualizar"))
        print (f"""
_____________________________________
codigo: {codigo}
nombre: {camper[codigo].get('nombre')}
apellido: {camper[codigo].get('apellido')}
edad: {camper[codigo].get('edad')}
genero: {camper[codigo].get(generos)}
______________________________________
               """)
        print("¿este es el camper que deseas actualizar?")
        print("1. si")
        print("2. no")
        print("3. salir")
        opc = int(input())
        if(opc == 0):
            info = {
                "nombre": input("ingrese el nombre del camper\n"),
                "Apellido": input("Ingrese el apellido del camper\n"),
                "Edad": int(input("Ingrese la edad del camper\n")),
                "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
            }
            camper[codigo] = info
            with open("modulo/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
    return"camper editado"

def search():
    
    for i,val in enumerate(camper):
        print("__________________")
        print(f"codigo: {i}\nnombre: {val.get('nombre')}\n apellido: {val.get('apellido')}\n edad: {val.get('edad')}\n genero: {val.get('genero')}")
    print("___________________")
    return "the camper is avalible"
def delete():
    bandera = True
    while(bandera):
        system("clear")
        print("""
**************************
* Eliminacion del camper *
**************************
              """)
        codigo = int(input("ingrese el codigo del camper que deseas eliminar:"))
        print(f"""
__________________________________
codigo: {codigo}
nombre: {camper[codigo].get('nombre')}
apellido: {camper[codigo].get('apellido')}
edad: {camper[codigo].get('edad')}
genero: {camper[codigo].get(generos)}
_________________________________
            """)
        
        print("¿este es el camper que deseas eliminar?")
        print("1. si")
        print("2. no")
        print("3. salir")
        opc = int(input())
        if(opc == 1):
            camper.pop(codigo)
            with open("modulo/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
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
            case 1: save()
            case 2: search()
            case 3: edit()
            case 4: delete()
            case 0:
                system("clear")
                bandera = False
            case _: menunovalido(opc)         
        

