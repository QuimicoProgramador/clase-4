from automatizador_utils import filtrar_proyectos_activos


if __name__ == '__main__':
    # Datos de prueba (podrían venir de un webhook)
    proyectos_webhook = [
        {"nombre": "A", "cadena": "Polygon", "estado": "activo"},
        {"nombre": "B", "cadena": "Algorand", "estado": "inactivo"},
        {"nombre": "C", "cadena": "Polygon", "estado": "activo"},
    ]

    # Llamamos a la función importada desde el módulo
    resultados = filtrar_proyectos_activos(proyectos_webhook, "Polygon")

    # Usamos el resultado
    print(f"Proyectos Activos en Polygon: {len(resultados)}")
    for proyecto in resultados:
        print(f"-> {proyecto['nombre']}")

