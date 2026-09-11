from blog.modelos import Autor, Post


def mostrar_resultados(posts, titulo_seccion):
    print()
    print(titulo_seccion)

    if len(posts) == 0:
        print("No se encontraron resultados.")
        return

    for post in posts:
        print()
        print("Titulo:", post.titulo)
        print("Autor:", post.autor.nombre)
        print("Estado:", post.estado)


def pedir_texto(mensaje):
    texto = input(mensaje).strip()

    while texto == "":
        print("Este campo no puede quedar vacio.")
        texto = input(mensaje).strip()

    return texto


def crear_post_desde_consola(blog):
    print()
    print("--- CREAR NUEVO POST ---")

    titulo = pedir_texto("Titulo: ")
    contenido = pedir_texto("Contenido: ")
    nombre_autor = pedir_texto("Nombre del autor: ")
    bio_autor = pedir_texto("Bio corta del autor: ")

    tags_texto = pedir_texto("Tags separados por coma: ")
    tags = []

    for tag in tags_texto.split(","):
        tag_limpio = tag.strip()

        if tag_limpio != "":
            tags.append(tag_limpio)

    estado = pedir_texto("Estado (borrador/publicado/archivado): ").lower()

    while estado not in ("borrador", "publicado", "archivado"):
        print("El estado ingresado no es valido.")
        estado = pedir_texto("Estado (borrador/publicado/archivado): ").lower()

    autor = Autor(nombre_autor, bio_autor)

    nuevo_post = Post(
        blog.siguiente_id(),
        titulo,
        contenido,
        autor,
        tags,
        estado
    )

    blog.agregar_post(nuevo_post)
    print("El post fue creado correctamente.")
