def mostrar_menu():
    print()
    print("--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

    try:
        opcion = int(input("Elegi una opcion: "))
        return opcion

    except ValueError:
        print("Tenes que ingresar un numero.")
        return 0
