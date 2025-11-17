def crear_id_proyecto(nombre_proyecto: str, version: int) -> str:
#     """Función que genera un ID de proyecto basado en el nombre y la versión."""
#     # Convertimos la entrada a mayúsculas para estandarizar
    nombre_formateado = nombreproyecto.upper().replace(" ", "")
id_polygon = crear_id_proyecto("Polygon Tracker", 2)
id_algorand = crear_id_proyecto("Algorand Wallet", 1)

print(f"ID generado 1: {id_polygon}")
print(f"ID generado 2: {id_algorand}")


id_final = f"{nombre_formateado}-V{version}"
return id_final;
