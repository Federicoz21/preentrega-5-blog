from blog.datos import estados_post


def validar_post(post):
    # Revisamos que el post sea un diccionario
    if type(post) != dict:
        return False, "El post no es un diccionario"

    # Revisamos que tenga ID
    if "id" not in post:
        return False, "Falta la clave id"

    # Revisamos que tenga titulo
    if "titulo" not in post:
        return False, "Falta la clave titulo"

    # Revisamos que el titulo no este vacio
    if post.get("titulo") == "":
        return False, "El titulo esta vacio"

    # Revisamos que tenga contenido
    if "contenido" not in post:
        return False, "Falta la clave contenido"

    # Revisamos que el contenido no este vacio
    if post.get("contenido") == "":
        return False, "El contenido esta vacio"

    # Revisamos que tenga autor
    if "autor" not in post:
        return False, "Falta la clave autor"

    # El autor debe seguir siendo un diccionario anidado
    if type(post.get("autor")) != dict:
        return False, "El autor debe ser un diccionario"

    # Revisamos que el autor tenga nombre
    if "nombre" not in post.get("autor"):
        return False, "Falta el nombre del autor"

    if post.get("autor").get("nombre", "") == "":
        return False, "El nombre del autor esta vacio"

    # Revisamos que tenga tags
    if "tags" not in post:
        return False, "Falta la clave tags"

    # Revisamos que tags sea una lista
    if type(post.get("tags")) != list:
        return False, "Los tags deben ser una lista"

    # Revisamos que tenga estado
    if "estado" not in post:
        return False, "Falta la clave estado"

    # Revisamos que el estado sea correcto
    if post.get("estado") not in estados_post:
        return False, "El estado no es valido"

    return True, "Post correcto"
