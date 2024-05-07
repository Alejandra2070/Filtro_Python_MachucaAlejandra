import json

def abrirArchivo():
    with open("Filtro.json",encoding="utf-8") as openfile:
        return json.load(openfile)
def guardarArchivo():
    with open("Filtro.json", "w") as outfile:
        return json.dump(outfile)

print("--------BIENVENIDOSSSSS--------")
print("----------MENÚ PRINCIPAL---------")
print("1. Usuarios ")
print("2. Gestión de servicios")
print("3. Reportes")
print("4. Bonificaciones")
print("5. Salir del programa")
opc = int(input("Seleccione una de las opciones de nuestro menú: "))
if opc ==1:
    print("")
    print("--------MENÚ USUARIOS--------")
    print("1. Crear un nuevo usuario")
    print("2. Ver la información de los usuarios")
    print("3. Actualizar datos del usuario")
    print("4. Historial de usuarios")
    print("5. Eliminar usuarios")
    print("6. Asignar categorias al usuario")
    print("7. Salir")
    x = int(input("Seleccione una de nuestras opciones: "))
    if  x ==1:
        print("ID:", ["id"])
        print("Nombre:", ["nombre"])
        print("Apellido:", ["apellido"])
        print("Dirección:", ["direccion"])
        print("Número de celular:", ["numero_celular"])
        nuevo_usuario= print("Por favor ingrese la información del nuevo usuario")
        NUid= int(input("Ingrese el id del nuevo usuario: "))
        NUnombre= input("Ingrese el nombre del nuevo usuario: ")
        NUapellido= input("Ingrese el apellido del nuevo usuario: ")
        NUdireccion= input("Ingrese la dirección del nuevo usuario: ")
        NUnumero_celular= int(input("Ingrese el número de celular del nuevo usuario: "))
        nuevo_usuario:{
            "id", NUid,
            "nombre", NUnombre,
            "apellido", NUapellido,
            "direccion", NUdireccion,
            "numero_celular", NUnumero_celular
        }
        miInfo=abrirArchivo()
        miInfo[0]["usuarios"]=nuevo_usuario
        miInfo=guardarArchivo[miInfo]
        print("Se creo el usuario exitosamente")
    elif x ==2:
        print("ID:",["id"])
        print("Nombre:",["nombre"])
        print("Apellido:",["apellido"])
        print("Dirección:",["direccion"])
        print("Número de celular:",["numero_celular"])
    elif x ==3:
        print("ID:",["id"])
        print("Nombre:",["nombre"])
        print("Apellido:",["apellido"])
        print("Dirección:",["direccion"])
        print("Número de celular:",["numero_celular"])
        idU= int(input("Ingrese el id del usuario al que quiere actualizar los datos: "))
        if idU==["usuarios"]:
            print("Qué desea actualizar del usuario?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Dirección")
            print("4. Número de celular")
            a=int(input("Elige una opción: "))
            if a ==1:
                ADnombre=print("Ingrese el nuevo nombre del usuario: ")
            elif a ==2:
                ADapellido=print("Ingrese el nuevo apellido del usuario: ")
            elif a==3:
                ADdireccion=print("Ingrese la nueva dirección del usuario: ")
            elif a==4:
                ADnumero=print("Ingrese el nuevo número de celular del usuario: ")
        miInfo=abrirArchivo()
        miInfo[0]["usuarios"].append
        miInfo=guardarArchivo(miInfo)
        print("Se actualizaron los datos del usuario correctamente")
    elif x ==4:
        print("----Menú historial----")
        print("1. Servicio al cliente")
        print("2. Reclamaciones")
        print("3. Sugerencias")
        x==int(input("Elige una opción: "))
    elif x==5:
        Eid= int(input("Ingrese el id del usuario que desea eliminar: "))
        if Eid==["usuarios"]:
            miInfo=abrirArchivo()
            miInfo[0]["usuarios"].remove
            miInfo=guardarArchivo()
            miInfo[0]["usuarios"]
            print("El usuario fue eliminado exitosamente")
    elif x==6:
        int(input("Ingrese el id del usuario al que desea asignarle una categoria: "))
        print("Qué categoria le gustaria asignarle?\n1. Nuevos clientes\n2. Clientes regulares\n3. Clientes leales")
        int(input("Elige una opción: "))
    elif x==7:
        print("Saliendo del programa...")
elif opc==2:
    print("--------Menú Servicios---------")
    print("1. Añadir un servicio")
    print("2. Revisar servicios disponibles")
    print("3. Actualizar datos de un servicio")
    print("4. Eliminar servicios")
    print("5. Salir")
    abc= int(input("Elige una opción: "))
    if abc==1:
        print("ID:", ["id"])
        print("Nombre del servicio: ",["nombre"])
        print("Características del servicio: ",["caracteristicas"])
        print("Precio del servicio: ",["precio"])
        print("Pago del servicio: "["pago"])
        nuevo_servicio=print("Por favor ingrese la siguiente información para añadir un nuevo servicio: ")
        NSid=int(input("Ingrese el id del nuevo servicio: "))
        NSnombre=input("Ingrese el nombre del nuevo servicio: ")
        NSprecio=input("Ingrese el precio del nuevo servicio: ")
        NSpago= input("Ingrese la forma de pago del nuevo servicio: ")("Diario, quincenal, mensual, anual")
        nuevo_servicio:{
            "id", NSid,
            "nombre", NSnombre,
            "precio", NSprecio,
            "pago", NSpago,
        }
        miInfo=abrirArchivo()
        miInfo[0]["servicios"]=nuevo_servicio
        miInfo=guardarArchivo(miInfo)
    elif abc==2:
        print("ID:",["id"])
        print("Nombre del servicio: ",["nombre"])
        print("Precio del servicio: ",["precio"])
        print("Pago del servicio: ",["pago"])
    elif abc==3:
        print("ID:",["id"])
        print("Nombre del servicio: ", ["nombre"])
        print("Precio del servicio: ", ["precio"])
        print("Pago del servicio: ", ["pago"])
        idS=int(input("Ingrese el id del servicio que desea actualizar: "))
        if idS==["servicios"]:
            print("Qué desea utilizar del servicio: ")
            print("1. Nombre del servicio")
            print("2. Precio del servicio")
            print("3. Forma de pago del servicio")
            ab=int(input("Elige una opción: "))
            if ab==1:
                print("Ingrese el nuevo nombre del servicio: ")
            if ab==2:
                print("Ingrese el nuevo precio del servicio: ")
            if ab==3:
                print("Ingrese la nueva forma de pago del servicio: ")
        miInfo=abrirArchivo()
        miInfo[0]["servicios"].append
        miInfo=guardarArchivo(miInfo)
        print("Se actualizaron los datos del servicio correctamente")
    elif abc==4:
        ESid= int(input("Ingrese el id del servicio que desea eliminar: "))
        if ESid==["servicios"]:
            miInfo=abrirArchivo()
            miInfo[0]["servicios"].remove
            miInfo=guardarArchivo()
            miInfo[0]["servicios"]
            print("El servicio fue eliminado exitosamente")
    elif abc==5:
        print("Saliendo del programa...")
elif opc==3:
    print("------Menú reportes------")
    print("1. Informe sobre la cantidad de servicios ofrecidos por la empresa")
    print("2. Servicios más populares de la empresa")
    print("3. Ver usuarios que han adquirido servicios y la cantidad de veces que lo han hecho")
    print("4. Salir del programa")
    db=int(input("Seleccione una de las opciones de este menú: "))
    if db==1:
        print("")
    elif db==2:
        print("")
    elif db==3:
        print("")
    elif db==4:
        print("Saliendo del programa...")

elif opc==4:
    print("----Menú bonificaciones----")
    print("1. Ver los clientes que han permanecido con la compañía por más de 10 años")
    print("2. Cálculo y asignación de bonificaciones")
    print("3. Salir del programa")
    bc=int(input("Elige una opción de este menú: "))
    if bc==1:
        print("")
    if bc==2:
        print("")
    if bc==3:
        print("Saliendo del programa...")
elif opc==5:
    print("Muchas gracias por utilizar nuestro programa!")
    print("Vuelve pronto :D")
#Desarrollado por Alejandra Machuca. Grupo T2