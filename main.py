from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


def ejecutar_programa():
    salir = False

    while salir == False:
        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Escribi una palabra para buscar: ").strip()

            if termino == "":
                print("No podes dejar la busqueda vacia.")
            else:
                buscar_por_titulo(posts, termino)

        elif opcion == 3:
            tag = input("Escribi el tag que queres buscar: ").strip()

            if tag == "":
                print("No podes dejar el tag vacio.")
            else:
                filtrar_por_tag(posts, tag)

        elif opcion == 4:
            print()
            print("--- VALIDACION DE POSTS ---")

            numero = 1

            for post in posts:
                valido, mensaje = validar_post(post)

                if valido == True:
                    print("Post", numero, ": valido")
                else:
                    print("Post", numero, ": error -", mensaje)

                numero = numero + 1

        elif opcion == 5:
            print()
            print("Gracias por usar el blog.")
            salir = True

        elif opcion != 0:
            print("La opcion ingresada no existe.")


if __name__ == "__main__":
    ejecutar_programa()
