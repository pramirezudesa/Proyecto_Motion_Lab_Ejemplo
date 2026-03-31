def filtrar_datos(datos, id_participante):
    """
    Filtra los registros de un ID y los organiza en
    listas para análisis de series temporales.
    Parámetros: datos (list), id_participante (str)
    Retorna: dict con las listas de datos del participante.
    """
    perfil = {"id": id_participante, "tiempo": [], "hit": [], "condicion": ""}
    for reg in datos:
        if str(reg["id_participante"]) == str(id_participante):
            perfil["tiempo"].append(float(reg["tiempo"]))
            perfil["hit"].append(reg["hit"].lower() in ["true", "1"])
            if not perfil["condicion"]:
                perfil["condicion"] = reg["condicion"]
    return perfil
