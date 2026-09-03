def mostrar_menu():
    print()
    print("--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = int(input("Elegi una opcion: "))
        return opcion

    except ValueError:
        print("Tenes que ingresar un numero.")
        return 0
