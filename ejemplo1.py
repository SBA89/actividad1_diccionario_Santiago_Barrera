import os
#clasificación de estudiantes de acuerdo a puntaje
ls_categoria1 = []#puntaje (30 - 50) y edad (15 - 20)
ls_categoria2 = []#puntaje (51 - 80) y edad (21 - 30)
ls_categoria3 = []#puntaje (81 - 100) y edad (31 - 50)
sw = True
def fnt_limpiar():
    os.system('cls')
    print('\nBienvenido al sistema de calificación de estudiantes')
    print('Autor: Dulfran Montaño')
    print('Institución: Universidad Católica Luis Amigó')
    print('Categoría   I: ',ls_categoria1)
    print('Categoría  II: ',ls_categoria2)
    print('Categoría III: ',ls_categoria3)
    
def fnt_registrar(id, nombre, edad, puntaje):
    if id == '' or puntaje == '' or edad == '' or nombre == '':
        enter = input('\nDebe ingresar todos los datos <ENTER>')
    else:
        if id in ls_categoria1: #or ls_categoria2 or ls_categoria3:#si ese id se encuentra ya registrado
               enter = input('\nEsta persona ya se encuentra categorizada <ENTER>')
        else:
            axuP = int(puntaje) #convierte el dato en entero.
            AuxE = int(edad) #convierte el dato a entero.
            if (axuP >= 30 and axuP <= 50) and (AuxE >= 15 and AuxE <= 20):
               ls_categoria1.append([id,nombre,edad,puntaje])
            elif (axuP >= 51 and axuP <= 80) and (AuxE >= 21 and AuxE <= 30):
                ls_categoria2.append([id,nombre,edad,puntaje])
            elif (axuP >= 81 and axuP <= 100) and (AuxE >= 31 and AuxE <= 50):
                ls_categoria3.append([id,nombre,edad,puntaje])
            enter = input(f'\nEstudiante {nombre} registrado con éxito')
def fnt_selector(op):
    fnt_limpiar()
    if op == '1':
        idStr = input('\n\nId:  ')
        nombreStr = input('Nombres completos:  ')
        edadStr = input('Edad:  ')
        puntajeStr = input('Puntaje:  ')
        fnt_registrar(idStr,nombreStr,edadStr,puntajeStr)
        
while sw == True:
    fnt_limpiar()
    opcionesStr = input('\n\n<<<<< MENU PRINCIPAL >>>>>\n\n1. REGISTRAR\n2. CONSULTAR\n\n-> ')
    fnt_selector(opcionesStr)