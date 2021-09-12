from helpers import borrarPantalla,gotoxy
from componentes import Menu,Valida
from entidadesUnemi import *
from crudArchivos import Archivo
from datetime import date


def carreras():
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion carrera: ")
    gotoxy(35,5)
    desCarrera = input()
    archiCarrera = Archivo("./Proyecto/nota.txt",";")
    carreras = archiCarrera.leer()
    if carreras : idSig = int(carreras[-1][0])+1
    else: idSig = 1
    carrera = Carrera(idSig,desCarrera)
    datos = carrera.getCarrera()
    datos = ";".join(datos)
    archiCarrera.escribir([datos],"a")
    
    
       





#Menu Proceso Principal
opc = ""
while opc != "5":
    borrarPantalla()
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Matriculación","3) Notas","4) Consultas","5) Salir"])
    opc = menu.menu()
    if opc == "1":
        opc1 = ""
        while opc1 != "7":
            borrarPantalla()
            menu1 = Menu("Menu Mantenimiento",["1) Materias","2) Profesores", "3) Estudiantes","4) Cargo","5) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                carreras()
            elif opc1 == "2":
                pass
            elif opc1 == "3":
                pass
            elif opc1 == "4":
                pass
    
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Matriculación",["1) Matricula","2) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                pass
            elif opc2 == "2":
                pass
            
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                pass
            elif opc3 == "2":
                pass
            
    elif opc == "4":
            borrarPantalla()
            menu4 = Menu("Menu Consultas",["1) Materias","2) Profesores", "3) Estudiantes","4) Cargo","5) Salir"],20,10)
            opc4 = menu4.menu()
            if opc4 == "1":
                pass
            elif opc4 == "2":
                pass
            
    elif opc == "5":
        borrarPantalla()
        print("Gracias por su visita....")
        
    else:
        print("Opcion no valida")
        
input("Presione una tecla para salir")
borrarPantalla()
        
            
            
            
    
        