def filtrar_proyectos_webhook(proyectos, cadena_objetivo):
        proyectos_webhook: [
        {
            "nombre": "Proyecto A",
            "estado": "activo",
            "cadena": "Ethereum"
        },
        {
            "nombre": "Proyecto B",
            "estado": "inactivo",
            "cadena": "Polygon"
        },
        {
            "nombre": "Proyecto C",
            "estado": "activo",
            "cadena": "Polygon"
        }
] 
  
     
    proyectos_filtrados = [
        proyecto for proyecto in proyectos
        if proyecto["estado"] == "activo" and proyecto["cadena"] == cadena_objetivo
    ]
return proyectos_filtrados;

                                                                                                                                                                                                                                                                                                         esto es un programa hackeado.

