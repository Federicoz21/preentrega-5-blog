# Sistema de Blog con POO y JSON

## Autor

Federico Zangaro

## Descripcion

Este proyecto es la continuacion del blog por consola que fui desarrollando en las entregas anteriores de Python.

En esta preentrega agregue Programacion Orientada a Objetos. Los autores, los posts y el blog ahora se representan con clases y objetos.

Tambien agregue persistencia con JSON. Los posts se cargan desde `posts.json` cuando inicia el programa y se pueden volver a guardar para que la informacion no se pierda al cerrar el programa.

## Estructura del proyecto

```text
preentrega-6-blog/
|
|-- main.py
|-- README.md
|-- posts.json
|
`-- blog/
    |-- __init__.py
    |-- datos.py
    |-- menu.py
    |-- modelos.py
    |-- operaciones.py
    `-- validaciones.py
```

## Clases principales

### Autor

Representa a la persona que escribe un post.

Tiene datos como:

- nombre
- bio
- especialidad
- redes sociales

Tambien tiene el metodo `a_diccionario()` para poder convertir el objeto a un formato que JSON pueda guardar.

### Post

Representa una publicacion del blog.

Tiene:

- id
- titulo
- contenido
- autor
- tags
- estado

El atributo `autor` guarda un objeto de la clase `Autor`.

Tambien tiene el metodo `a_diccionario()` para convertir el post a un diccionario antes de guardarlo en JSON.

### Blog

La clase `Blog` guarda la lista de objetos `Post` y centraliza las operaciones principales.

Permite:

- listar posts
- buscar por titulo
- filtrar por tag
- agregar posts
- obtener los posts cargados
- generar el siguiente id

Las busquedas por titulo y tag usan `lower()` para ignorar mayusculas y minusculas.

## Persistencia con JSON

El archivo `blog/datos.py` se encarga de cargar y guardar la informacion.

Al iniciar el programa, la funcion `cargar_posts()` lee `posts.json`. Los diccionarios leidos se convierten nuevamente en objetos `Autor` y `Post`.

Cuando se guardan los datos, cada objeto `Post` se convierte primero a diccionario. Luego se usa el modulo `json` de Python para escribir la lista en `posts.json`.

El programa tambien maneja casos donde el archivo no existe, esta vacio o contiene JSON invalido.

## Menu del programa

El programa permite usar estas opciones:

```text
--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Crear nuevo post
5. Validar posts
6. Guardar posts en JSON
7. Salir
```

Al crear un post se piden los datos por consola, se crea un objeto `Autor`, luego un objeto `Post` y finalmente se agrega a la instancia de `Blog`.

## Como ejecutar el programa

Abrir una terminal en la carpeta donde esta `main.py` y ejecutar:

```bash
python main.py
```

## Manejo de errores

El proyecto controla algunos errores basicos para evitar que el programa se cierre inesperadamente:

- opcion del menu que no es un numero
- campos vacios al crear posts
- estado de post incorrecto
- archivo `posts.json` inexistente
- archivo JSON vacio
- contenido JSON invalido
- datos incompletos al reconstruir objetos

## Cambios respecto a la entrega anterior

En la entrega anterior los posts y autores se manejaban principalmente con diccionarios y las operaciones estaban realizadas con funciones.

En esta entrega:

- se agrego `blog/modelos.py`
- se crearon las clases `Autor`, `Post` y `Blog`
- el autor de cada post ahora es un objeto `Autor`
- el blog trabaja con una lista de objetos `Post`
- se agrego el archivo `posts.json`
- se agrego carga y guardado de datos con JSON
- el menu ahora permite crear nuevos posts y guardarlos
- `main.py` crea una instancia de `Blog` y usa sus metodos

La idea fue mantener el proyecto simple, pero aplicar los conceptos nuevos de clases, objetos, metodos y persistencia.
