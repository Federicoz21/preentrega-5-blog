from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu
from blog.modelos import Blog
from blog.operaciones import crear_post_desde_consola, mostrar_resultados
from blog.validaciones import validar_post


def ejecutar_programa():
    posts_cargados = cargar_posts()
    blog = Blog(posts_cargados)

    salir = False

    while salir == False:
        opcion = mostrar_menu()

        if opcion == 1:
            blog.listar_posts()

        elif opcion == 2:
            termino = input("Escribi una palabra para buscar: ").strip()

            if termino == "":
                print("No podes dejar la busqueda vacia.")
            else:
                resultados = blog.buscar_por_titulo(termino)
                mostrar_resultados(resultados, "--- RESULTADOS ---")

        elif opcion == 3:
            tag = input("Escribi el tag que queres buscar: ").strip()

            if tag == "":
                print("No podes dejar el tag vacio.")
            else:
                resultados = blog.filtrar_por_tag(tag)
                mostrar_resultados(resultados, "--- RESULTADOS POR TAG ---")

        elif opcion == 4:
            crear_post_desde_consola(blog)

        elif opcion == 5:
            print()
            print("--- VALIDACION DE POSTS ---")

            numero = 1

            for post in blog.obtener_posts():
                valido, mensaje = validar_post(post)

                if valido == True:
                    print("Post", numero, ": valido")
                else:
                    print("Post", numero, ": error -", mensaje)

                numero = numero + 1

        elif opcion == 6:
            guardar_posts(blog.obtener_posts())

        elif opcion == 7:
            print()
            guardar_posts(blog.obtener_posts())
            print("Gracias por usar el blog.")
            salir = True

        elif opcion != 0:
            print("La opcion ingresada no existe.")


if __name__ == "__main__":
    ejecutar_programa()
