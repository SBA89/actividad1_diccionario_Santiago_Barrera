mi_diccionario = {}
import os 
sw = True
def fnt_agregar(diccionario, id_persona, codigo, nombre, apellido, contacto, correo, edad, estrato, sexo, telefono, direccion):
    if id_persona == '' or nombre == '' or  apellido == ''  or contacto == ''  or correo == ''  or edad == '' or estrato == ''  or sexo == '' or telefono == '' or direccion == '':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[id_persona] = {'Codigo': codigo, 'Nombre': nombre, 'Apellido': apellido, 'Contacto': contacto, 'Correo': correo, 'Edad': edad, 'Estrato': estrato, 'Sexo': sexo, 'Telefono': telefono, 'Dirección': direccion}
        enter = input(f'\nLa persona {nombre} ha sido resgistrada con éxito <ENTER>')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        codigo = int(input('Codigo: '))
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        contacto = int(input('Contacto: '))
        correo = input('Correo: ')
        edad = int(input('Edad: '))
        estrato = int(input('Estrato: '))
        sexo = input('Sexo: ')
        telefono = int(input('Telefono: '))
        direccion = input('Dirección: ')
        fnt_agregar(mi_diccionario, codigo, nombre, apellido, contacto, correo, edad, estrato, sexo,  telefono, direccion)

while sw == True:
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n--> ')
    if opcion == '1':
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        print('\nCantidad de registros: ',len(mi_diccionario),'\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\n\nPresione ENTER para continuar...')
    elif opcion ==  '3':
        sw = False