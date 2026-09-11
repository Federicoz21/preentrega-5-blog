import json

from blog.modelos import post_desde_diccionario


ARCHIVO_POSTS = "posts.json"

estados_post = (
    "borrador",
    "publicado",
    "archivado"
)


def cargar_posts():
    try:
        with open(ARCHIVO_POSTS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()

            if contenido == "":
                print("El archivo posts.json esta vacio. Se inicia sin posts.")
                return []

            datos = json.loads(contenido)

            if type(datos) != list:
                print("El archivo posts.json no tiene el formato esperado.")
                return []

            posts = []

            for dato in datos:
                post = post_desde_diccionario(dato)
                posts.append(post)

            return posts

    except FileNotFoundError:
        print("No existe posts.json. Se inicia sin posts.")
        return []

    except json.JSONDecodeError:
        print("El archivo posts.json tiene contenido JSON invalido.")
        return []

    except (ValueError, TypeError) as error:
        print("No se pudieron cargar los posts:", error)
        return []


def guardar_posts(posts):
    try:
        lista_diccionarios = []

        for post in posts:
            lista_diccionarios.append(post.a_diccionario())

        with open(ARCHIVO_POSTS, "w", encoding="utf-8") as archivo:
            json.dump(lista_diccionarios, archivo, ensure_ascii=False, indent=4)

        print("Los posts se guardaron correctamente en posts.json.")
        return True

    except (AttributeError, TypeError) as error:
        print("No se pudieron convertir los posts a diccionarios:", error)
        return False

    except OSError as error:
        print("No se pudo guardar el archivo:", error)
        return False
