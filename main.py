import sqlite3

#inserta datos a la base de datos
def insertar(datos,opcion):
    #conexion a la base de datos
    con_bd = sqlite3.connect('data.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()

    if opcion == '1':
        #consultas
        cursor_agenda.execute("INSERT INTO usuarios(username, password, correo) VALUES(?, ?, ?)", (datos))
    elif opcion == '2':
        #consultas
        cursor_agenda.execute("INSERT INTO cliente(nombre, apellido, correo, id, direccion) VALUES(?, ?, ?, ?, ?)", (datos))
    elif opcion == '3':
        #consultas
        cursor_agenda.execute("INSERT INTO producto(nombre, descripcion, imagen, precio) VALUES(?, ?, ?, ?)", (datos))
    #se ejecutan los cambios
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()


    print("EXITO EN LA OPERACION")


def eliminar(datos,opcion):

    #conexion a la base de datos
    con_bd = sqlite3.connect('data.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()

    if opcion == '1':
        #consultas
        cursor_agenda.execute("DELETE FROM usuarios WHERE username=?", (datos,))
    elif opcion == '2':
        #consultas
        cursor_agenda.execute("DELETE FROM cliente WHERE id=?", (datos,))
    elif opcion == '3':
        #consultas
        cursor_agenda.execute("DELETE FROM producto WHERE codigo=?", (datos,))
    #se ejecutan los cambios
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()
    print("LA ELIMINICACION FUE EXITOSA")

    
def consulta_especifica(llavePrimaria,opcion):
    #conexion a la base de datos
    con_bd = sqlite3.connect('data.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()

    if opcion == '1':
        #consultas
        consulta = cursor_agenda.execute("SELECT username,correo FROM usuarios WHERE username=?", (llavePrimaria,))
    elif opcion == '2':
        #consultas
        consulta = cursor_agenda.execute("SELECT nombre,apellido,correo FROM cliente WHERE id=? ", (llavePrimaria,))
    elif opcion == '3':
        #consultas
        consulta = cursor_agenda.execute("SELECT nombre,descripcion FROM producto WHERE precio<=?", (llavePrimaria,))

    #impresion de todos los campos
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()

def consultar_todo():
    #conexion a la base de datos
    con_bd = sqlite3.connect('data.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()
    #consultas
    consulta = cursor_agenda.execute("SELECT * FROM usuarios")
    #impresion de todos los campos
    for fila in consulta:
        print("fila: {0}".format(fila))
        for campo in fila:
            print("Campo de la fila: {0}".format(campo))
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()


def actualizar(datos,opcion,actualizacion1,actualizacion2=None):

    #conexion a la base de datos
    con_bd = sqlite3.connect('data.db')
    #cursor a la db
    cursor_agenda = con_bd.cursor()

    if opcion == '1':
        #consultas
        cursor_agenda.execute("UPDATE usuarios SET correo=? WHERE username=?", (actualizacion1,datos,))
    elif opcion == '2':
        #consultas
        cursor_agenda.execute("UPDATE cliente SET correo=?,direccion=? WHERE id=?", (actualizacion1,actualizacion2,datos,))
    elif opcion == '3':
        #consultas
        cursor_agenda.execute("UPDATE producto SET descripcion=?,precio=? WHERE codigo=?", (actualizacion1,actualizacion2,datos,))
    #se ejecutan los cambios
    con_bd.commit()
    #cierre del cursor
    cursor_agenda.close()
    #cierre de la conexion
    con_bd.close()
    print("LA ACTUALIZACION FUE EXITOSA")




def registrarUsuarios():
    usuario=()
    username=input("Digite nombre usuario: ")
    password=input("Digite password: ")
    correo=input("Digite correo: ")
    usuario=(username,password,correo)
    return usuario

def registrarClientes():
    cliente=()
    nombre=input("Digite nombre del cliente").upper()
    apellido=input("Digite apellido del cliente").upper()
    correo=input("Digite correo electronico")
    identificador=int(input("Digite su numero de identificacion"))
    direccion=input("Digite la direccion").upper()
    cliente=(nombre,apellido,correo,identificador,direccion)
    return cliente

def registrarProducto():
    producto=()
    nombre=input("Digite nombre del producto").upper()
    descripcion=input("Ingrese la descripcion/precio del producto").upper()
    imagen=input("Digite ruta de la imagen")
    precio=float(input("Digite el precio del producto"))
    producto=(nombre,descripcion,imagen,precio)
    return producto

def insercion_datos():
    opcion=0
    while opcion!='4':
        print("1 Crear usuario nuevo")
        print("2 Crear cliente nuevo")
        print("3 Crear un nuevo producto")
        print("4 Regresar menu principal")
        opcion=input()
        if opcion=="1":
            usuario = registrarUsuarios()
            insertar(usuario,opcion)
        elif opcion =="2":
            usuario = registrarClientes()
            insertar(usuario,opcion)
        elif opcion == "3":
            producto = registrarProducto()
            insertar(producto,opcion)

def consultar_datos():
    opcion=0
    while opcion!='4':
        print("1 Consultar usuario registrado")
        print("2 Consultar clientes registrados")
        print("3 Consultar producto por precios")
        print("4 Regresar menu principal")
        opcion=input()
        if opcion == "1":
            username=input("Digite el username a buscar")
            consulta_especifica(username,'1')
        elif opcion == "2":
            username=input("Digite la cedula del cliente a buscar")
            consulta_especifica(username,'2')
        elif opcion == '3':
            precio=input("Digite su presupuesto")
            consulta_especifica(precio,'3')

def eliminar_datos():
        opcion=0
        while opcion!='4':
            print("1 Eliminar usuario registrado")
            print("2 Eliminar clientes registrados")
            print("3 Eliminar producto por precios")
            print("4 Regresar menu principal")
            opcion=input()
            if opcion == "1":
                username=input("Digite el username a eliminar")
                eliminar(username,opcion)
            elif opcion == "2":
                identificador=input("Digite la cedula del cliente a eliminar")
                eliminar(identificador,opcion)
            elif opcion == '3':
                codigo=input("Digite el codigo del producto a eliminar")
                eliminar(codigo,opcion)

def actualizar_datos():
    opcion=0
    while opcion!='4':
        print("1 Actualizar usuario registrado")
        print("2 Actualizar clientes registrados")
        print("3 Actualizar producto por precios")
        print("4 Regresar menu principal")
        opcion=input()
        if opcion == "1":
            username=input("Digite el username a Actualizar")
            correo=input("Digite nuevo correo")
            actualizar(username,opcion,correo)
        elif opcion == "2":
            identificador=input("Digite la cedula del cliente a Actualizar")
            correo=input("Digite nuevo correo")
            direccion=input("Diite nueva dierccion")
            actualizar(identificador,opcion,correo,direccion)
        elif opcion == '3':
            codigo=input("Digite el codigo del producto a Actualizar")
            descripcion=input("Digite nueva descripción")
            precio=float(input("Digite nuevo precio"))
            actualizar(codigo,opcion,descripcion,precio)


def menu_principal():
    continuar="si"
    while continuar=="si":

        print("Digite una opcion")
        print("1 Insertar datos")
        print("2 Consultar datos")
        print("3 Eliminar datos")
        print("4 Actualizar datos")

        opcion=input()
        if opcion == '1':
            insercion_datos()
        elif opcion == '2':
            consultar_datos()
        elif opcion == '3':
            eliminar_datos()
        elif opcion == '4':
            actualizar_datos()
        continuar=input("si/no  mostrar menu").lower()

print("Menu Principal")
menu_principal()
print("Ha terminado de ejecutar el programa")