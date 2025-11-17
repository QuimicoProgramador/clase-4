def filtrar_proyectos_activos(proyectos: list, cadena_a_filtrar: str) -> list:
    """Filtra una lista de proyectos y devuelve solo los activos que coinciden
    con la cadena proporcionada en la clave 'cadena'.

    - `proyectos` debe ser una lista de diccionarios que al menos contengan
      las claves `'cadena'` y `'estado'`.
    - `cadena_a_filtrar` es la cadena que se comparará con `p['cadena']`.

    Devuelve una lista (posiblemente vacía) con los proyectos que cumplen
    ambas condiciones: coinciden en la cadena y su estado es 'activo'.
    """
    return [
        p for p in proyectos
        if p.get('cadena') == cadena_a_filtrar and p.get('estado') == 'activo'
    ]
