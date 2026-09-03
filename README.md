# Sistema de Blog Modular en Python

## Autor

Federico Zangaro

## Descripcion

Este proyecto es la continuacion del sistema de blog que fui haciendo en los modulos anteriores.

En esta entrega el objetivo fue dejar de tener todo el codigo dentro de un solo archivo y separarlo en distintos modulos. La idea es que cada archivo tenga una responsabilidad clara y que `main.py` se encargue solamente de coordinar el programa.

El sistema sigue funcionando por consola y permite ver todos los posts, buscar por titulo, filtrar por tag, validar la estructura de los posts y salir del programa.

## Estructura del proyecto

```text
blog_consola/
|
|-- main.py
|-- README.md
|
`-- blog/
    |-- __init__.py
    |-- datos.py
    |-- menu.py
    |-- operaciones.py
    `-- validaciones.py
```

## Que hace cada archivo

### main.py

Es el archivo principal. Importa los datos y funciones de los otros modulos, muestra el flujo del programa y controla las opciones elegidas por el usuario.

### blog/__init__.py

Permite que Python reconozca la carpeta `blog` como un paquete.

### blog/datos.py

Contiene los datos principales del blog:

- perfil del autor
- estados posibles
- etiquetas
- lista de posts

El autor se mantiene como un diccionario anidado dentro de cada post.

### blog/menu.py

Contiene la funcion que muestra el menu y pide una opcion al usuario.

Tambien usa `try-except` para evitar que el programa se cierre si se ingresa una letra en lugar de un numero.

### blog/operaciones.py

Contiene las funciones que permiten:

- listar posts
- buscar por titulo
- filtrar por tag

Las busquedas usan `lower()` para ignorar mayusculas y minusculas.

### blog/validaciones.py

Contiene la funcion que revisa que cada post tenga los datos necesarios y que esos datos tengan el formato esperado.

## Como ejecutar el programa

Primero hay que abrir una terminal en la carpeta donde se encuentra `main.py`.

Despues ejecutar:

```bash
python main.py
```

Al iniciar aparece este menu:

```text
--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Validar posts
5. Salir
```

## Explicacion corta del trabajo

En esta entrega tome el sistema de blog que ya habia hecho y lo separe en varios archivos.

Antes tenia los datos, el menu, las busquedas y las validaciones en el mismo archivo. Ahora cada parte esta ubicada en un modulo diferente dentro de la carpeta `blog`.

Use imports en `main.py` para conectar todos los archivos sin copiar las funciones. Tambien mantuve el autor como diccionario dentro de cada post y conserve las busquedas con `lower()` para que no importe si se escribe con mayusculas o minusculas.

Con esta organizacion el programa hace practicamente lo mismo que antes, pero el codigo queda mucho mas ordenado y resulta mas facil encontrar cada parte.
