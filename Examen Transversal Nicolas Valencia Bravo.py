peliculas = {
    "P101": ["Luz de Otoño", "drama", 110, "B", "Español", False],
    "P102": ["Noche Neón", "acción", 125, "C", "Ingles", True],
    "P103": ["Planeta Agua", "documental", 90, "A", "Español", False],
    "P104": ["Risa Total", "comedia", 105, "A", "Español", True],
    "P105": ["Código Zero", "thriller", 118, "C", "Ingles", True],
    "P106": ["Viaje Lunar", "ciencia ficción", 132, "B", "Ingles", False],
    }

cartelera = {
    "P101": [5990, 40],
    "P102": [7990, 0],
    "P103": [4990, 25],
    "P104": [6990, 12],
    "P105": [8990, 8],
    "P106": [7490, 3],
    }

def Mostrar_Menu ():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género.")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("="*45)

def Leer_Opcion ():
    while True:
        try:
            Opcion = int (input ("Ingrese opcion: "))
            if 1 <= Opcion <= 6:
                return Opcion
            else:
                print ("ERROR: Debe seleccionar una opción válida")
        except:
            print ("ERROR: Debe seleccionar una opción válida")

def Cupos_Genero (Genero):
    Total = 0
    for Codigo, Datos in peliculas.items ():
        if Datos[1].lower() == Genero.lower():
            Total += cartelera[Codigo][1]
    print (f"El total de cupos disponible de ese genero es: {Total}")

def Busqueda_Precio (Precio_Min, Precio_Max):
    Resultados = []
    for Codigo, Datos_Cartelera in cartelera.items():
        Precio = Datos_Cartelera[0]
        Cupos = Datos_Cartelera[1]
        if Precio_Min <= Precio <= Precio_Max and Cupos != 0:
            Nombre = peliculas[Codigo][0]
            Genero = peliculas[Codigo][1]
            Resultados.append(f"{Nombre}-{Genero}--{Codigo}")
    Resultados.sort()
    if len(Resultados) == 0:
        print ("No hay peliculas con ese rango de precios.")
    else:
        print(f"Las peliculas encontradas son: {Resultados}")

def Actualizar_Precio (Codigo, Nuevo_Precio):
    Codigo = Codigo.upper()
    if Codigo not in cartelera:
        return False
    cartelera[Codigo][0] = Nuevo_Precio
    return True

def Validar_Texto (Texto):
    return Texto.strip () != " "

def Validar_Codigo_Nuevo (Codigo):
    return Codigo.strip () != " " and Codigo.upper() not in peliculas

def Validar_Entero_Positivo (Valor):
    try:
        return int(Valor) >0
    except:
        return False

def Validar_Entero_No_Negativo (Valor):
    try:
        return int (Valor) >= 0
    except:
        return False

def Validar_Clasificacion (Clasificacion):
    return Clasificacion in ("A","B","C")

def Validar_Idioma (Idioma):
    return Idioma in ("Español","Ingles")

def Agregar_Pelicula (Codigo, Nombre, Genero, Duracion, Clasificacion, Idioma, Es_3d, Precio, Cupos):
    Codigo = Codigo.upper()
    if Codigo in peliculas:
        return False
    peliculas [Codigo] = [Nombre, Genero, Duracion, Clasificacion, Idioma, Es_3d]
    cartelera [Codigo] = [Precio, Cupos]
    return True

def Eliminar_Pelicula (Codigo):
    Codigo = Codigo.upper()
    if Codigo not in peliculas:
        return False
    del peliculas[Codigo]
    del cartelera[Codigo]
    return True

while True:
    Mostrar_Menu()
    Opcion = Leer_Opcion()

    if Opcion == 1:
        Genero = input ("Ingrese genero de pelicula a consultar: ")
        Cupos_Genero(Genero)
    elif Opcion == 2:
        while True:
            Precio_Min_Texto = input ("Ingrese precio minimo a consultar: ")
            Precio_Max_Texto = input ("Ingrese precio maximo a consultar: ")
            try:
                Precio_Min = int (Precio_Min_Texto)
                Precio_Max = int (Precio_Max_Texto)
                if Precio_Min < 0 or Precio_Max <0 or Precio_Min > Precio_Max:
                    print("Debe ingresar valores enteros: ")
                    continue
                break
            except:
                print("Debe ingresar valore enteros")
        Busqueda_Precio(Precio_Min,Precio_Max)
    elif Opcion == 3:
        while True:
            Codigo = input("Ingrese codigo de la pelicula a actualizar: ")
            while True:
                Precio_Texto = input("Ingrese nuevo precio: ")
                if Validar_Entero_Positivo(Precio_Texto):
                    Nuevo_Precio = int (Precio_Texto)
                    break
                print("El prcio debe ser un numero entero positivo")
            if Actualizar_Precio(Codigo, Nuevo_Precio):
                print("Precio actualizado correctamente")
            else:
                print("Codigo no existe")
            Repetir = input ("¿Desea actualizar otro precio (s/n) ?")
            if Repetir.lower() != "s":
                break
    elif Opcion == 4:
        Codigo = input ("Ingrese codigo de pleicula a agregar: ")
        if not Validar_Codigo_Nuevo(Codigo):
            print ("ERROR: El codigo no puede esta vacio ni debe existir previamente")
            continue
        Nombre = input ("Ingrese el nombre de la pelicula a agregar: ")
        if not Validar_Texto(Nombre):
            print ("ERROR: El nombre no puede estar vacio")
            continue
        Genero = input ("Ingrese el genero de la pelicula: ")
        if not Validar_Texto(Genero):
            print ("ERROR: El genero no puede estar vacio")
            continue
        Duracion_Texto = input ("Ingrese la duracion en minutos: ")
        if not Validar_Entero_Positivo (Duracion_Texto):
            print("ERROR: La duracion debe ser un numero entero mayor que cero")
            continue
        Duracion = int(Duracion_Texto)
        Clasificacion = input ("Ingrese la clasificacion de la pelicula: ")
        if not Validar_Clasificacion (Clasificacion):
            print("ERROR: La clasificacion de la pelicula debe ser A, B o C")
            continue
        Idioma = input ("ingrese el idioma de la pelicula: ")
        if not Validar_Idioma (Idioma):
            print ("ERROR: el idioma tiene que ser ingles o español")
            continue
        Es_3d_texto = input ("ingrese si la pelicula es 3d (s/n): ")
        Es_3d = Es_3d_texto.lower() == "s"
        Precio_Texto = input ("Ingrese el precio de la entrada: ")
        if not Validar_Entero_Positivo(Precio_Texto):
            print("ERROR: El precio debe ser un numero entero mayor que cero")
            continue
        Precio = int (Precio_Texto)
        Cupos_Texto = input ("Ingrese cantidad de cupos de la pelicula: ")
        if not Validar_Entero_No_Negativo(Cupos_Texto):
            print("Error: los cupos deben ser un numero entero mayor o igual a cero")
            continue
        Cupos = int (Cupos_Texto)
        if Agregar_Pelicula (Codigo, Nombre, Genero, Duracion, Clasificacion, Idioma, Es_3d, Precio, Cupos):
            print("Pelicula agregada correctamente")
        else:
            print("el Codigo ya existe")
    elif Opcion == 5:
        Codigo = input ("Ingrese codigo de la pelicula a eliminar: ")
        if Eliminar_Pelicula(Codigo):
            print("pelicula Eliminada correctamente")
        else:
            print("El codigo no existe")
    elif Opcion == 6:
        print ("Programa finalizado.")
        break