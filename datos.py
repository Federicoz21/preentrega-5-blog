# Datos del autor
perfil_autor = {
    "nombre": "Federico Zangaro",
    "bio": "Estoy aprendiendo Python y ciberseguridad.",
    "especialidad": "Python y Ciberseguridad",
    "redes_sociales": []
}


# Estados posibles de los posts
estados_post = (
    "borrador",
    "publicado",
    "archivado"
)


# Etiquetas usadas en el blog
etiquetas_blog = {
    "genex",
    "python",
    "programacion",
    "ciberseguridad",
    "automatizacion"
}


# Lista de posts
posts = [
    {
        "id": 1,
        "titulo": "Creando mi proyecto GENEX",
        "contenido": "GENEX es un proyecto personal que estoy desarrollando para aprender programacion, automatizacion y ciberseguridad.",
        "autor": perfil_autor,
        "tags": ["genex", "programacion"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Aprendiendo Python para mejorar GENEX",
        "contenido": "Estoy aprendiendo Python para poder agregar nuevas funciones y mejorar distintas partes de GENEX.",
        "autor": perfil_autor,
        "tags": ["python", "genex"],
        "estado": "publicado"
    },
    {
        "id": 3,
        "titulo": "Ciberseguridad y automatizacion con GENEX",
        "contenido": "En este post cuento algunas ideas que estoy aprendiendo sobre ciberseguridad y automatizacion para aplicarlas en GENEX.",
        "autor": perfil_autor,
        "tags": ["ciberseguridad", "automatizacion", "genex"],
        "estado": "borrador"
    }
]
