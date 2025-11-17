def crear_id_proyecto(nombre_proyecto: str, version: int) -> str:
    """Genera un ID de proyecto a partir del nombre y la versión.

    Ejemplo: "Polygon Tracker", 2 -> "POLYGONTRACKER-V2"
    """
    nombre_formateado = nombre_proyecto.upper().replace(" ", "")
    id_final = f"{nombre_formateado}-V{version}"
    return id_final


def filtrar_proyectos_activos(proyectos: list, cadena_a_filtrar: str) -> list:
    """Filtra una lista de proyectos y devuelve solo los activos que coinciden
    con la cadena proporcionada en la clave 'cadena'.

    - `proyectos` debe ser una lista de diccionarios que al menos contengan
      las claves `'cadena'` y `'estado'`.
    - `cadena_a_filtrar` es la cadena que se comparará con `p['cadena']`.

    Devuelve una lista (posiblemente vacía) con los proyectos que cumplen
    ambas condiciones: coinciden en la cadena y su estado es 'activo'.
    """
    proyectos_filtrados = []
    for p in proyectos:
        if p.get('cadena') == cadena_a_filtrar and p.get('estado') == 'activo':
            proyectos_filtrados.append(p)

    return proyectos_filtrados


if __name__ == '__main__':
    # Ejemplos de uso rápido / prueba
    id_polygon = crear_id_proyecto("Polygon Tracker", 2)
    id_algorand = crear_id_proyecto("Algorand Wallet", 1)

    print(f"ID generado 1: {id_polygon}")
    print(f"ID generado 2: {id_algorand}")

    proyectos_ejemplo = [
        {'nombre': 'A', 'cadena': 'ethereum', 'estado': 'activo'},
        {'nombre': 'B', 'cadena': 'polygon', 'estado': 'inactivo'},
        {'nombre': 'C', 'cadena': 'ethereum', 'estado': 'activo'},
        {'nombre': 'D', 'cadena': 'polygon', 'estado': 'activo'},
    ]

    filtrados = filtrar_proyectos_activos(proyectos_ejemplo, 'ethereum')
    print('Proyectos activos filtrados:', filtrados)
