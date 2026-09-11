class Autor:
    def __init__(self, nombre, bio, especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad

        if redes_sociales is None:
            self.redes_sociales = []
        else:
            self.redes_sociales = redes_sociales

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }


class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def a_diccionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),
            "tags": self.tags,
            "estado": self.estado
        }


class Blog:
    def __init__(self, posts=None):
        if posts is None:
            self.posts = []
        else:
            self.posts = posts

    def obtener_posts(self):
        return self.posts

    def listar_posts(self):
        print()
        print("--- TODOS LOS POSTS ---")

        if len(self.posts) == 0:
            print("No hay posts cargados.")
            return

        for post in self.posts:
            print()
            print("Titulo:", post.titulo)
            print("Autor:", post.autor.nombre)
            print("Estado:", post.estado)

    def buscar_por_titulo(self, termino):
        encontrados = []

        for post in self.posts:
            if termino.lower() in post.titulo.lower():
                encontrados.append(post)

        return encontrados

    def filtrar_por_tag(self, tag):
        encontrados = []

        for post in self.posts:
            for etiqueta in post.tags:
                if tag.lower() == etiqueta.lower():
                    encontrados.append(post)
                    break

        return encontrados

    def agregar_post(self, post):
        self.posts.append(post)

    def siguiente_id(self):
        if len(self.posts) == 0:
            return 1

        mayor_id = 0

        for post in self.posts:
            if post.id > mayor_id:
                mayor_id = post.id

        return mayor_id + 1


def autor_desde_diccionario(datos):
    if "nombre" not in datos or "bio" not in datos:
        raise ValueError("Los datos del autor estan incompletos.")

    return Autor(
        datos["nombre"],
        datos["bio"],
        datos.get("especialidad", ""),
        datos.get("redes_sociales", [])
    )


def post_desde_diccionario(datos):
    campos_necesarios = ["id", "titulo", "contenido", "autor", "tags", "estado"]

    for campo in campos_necesarios:
        if campo not in datos:
            raise ValueError("Falta el campo " + campo + " en un post.")

    autor = autor_desde_diccionario(datos["autor"])

    return Post(
        datos["id"],
        datos["titulo"],
        datos["contenido"],
        autor,
        datos["tags"],
        datos["estado"]
    )
