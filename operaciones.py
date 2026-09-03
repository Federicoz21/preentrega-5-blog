def listar_posts(lista):
    print()
    print("--- TODOS LOS POSTS ---")

    for post in lista:
        titulo = post.get("titulo", "Sin titulo")
        autor = post.get("autor", {})
        nombre_autor = autor.get("nombre", "Autor desconocido")
        estado = post.get("estado", "Sin estado")

        print()
        print("Titulo:", titulo)
        print("Autor:", nombre_autor)
        print("Estado:", estado)


def buscar_por_titulo(lista, termino):
    encontrado = False

    print()
    print("--- RESULTADOS ---")

    for post in lista:
        titulo = post.get("titulo", "")

        if termino.lower() in titulo.lower():
            print()
            print("Titulo:", titulo)
            print("Autor:", post.get("autor", {}).get("nombre", "Autor desconocido"))
            print("Estado:", post.get("estado", "Sin estado"))
            encontrado = True

    if encontrado == False:
        print("No se encontraron posts con ese titulo.")


def filtrar_por_tag(lista, tag):
    encontrado = False

    print()
    print("--- RESULTADOS POR TAG ---")

    for post in lista:
        tags = post.get("tags", [])

        for etiqueta in tags:
            if tag.lower() == etiqueta.lower():
                print()
                print("Titulo:", post.get("titulo", "Sin titulo"))
                print("Autor:", post.get("autor", {}).get("nombre", "Autor desconocido"))
                print("Estado:", post.get("estado", "Sin estado"))
                encontrado = True
                break

    if encontrado == False:
        print("No se encontraron posts con ese tag.")
