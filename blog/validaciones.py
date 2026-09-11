from blog.datos import estados_post
from blog.modelos import Autor, Post


def validar_post(post):
    if type(post) != Post:
        return False, "El dato no es un objeto Post"

    if type(post.id) != int:
        return False, "El id debe ser un numero entero"

    if post.titulo.strip() == "":
        return False, "El titulo esta vacio"

    if post.contenido.strip() == "":
        return False, "El contenido esta vacio"

    if type(post.autor) != Autor:
        return False, "El autor debe ser un objeto Autor"

    if post.autor.nombre.strip() == "":
        return False, "El nombre del autor esta vacio"

    if type(post.tags) != list:
        return False, "Los tags deben ser una lista"

    if post.estado not in estados_post:
        return False, "El estado no es valido"

    return True, "Post correcto"
