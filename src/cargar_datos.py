def parsear_linea(linea):
    """
    Qué hace la función: Separa una línea de texto CSV en una lista de strings.
    Parámetros: linea (str)
    Retorna: list[str]
    """
    return linea.strip().split(',')

def cargar_datos(ruta):
    """
    Qué hace la función: Lee el archivo y genera una lista de registros (diccionarios).
    Parámetros: ruta (str)
    Retorna: list[dict]
    """
    registros = []
    try:
        with open(ruta, "r") as archivo:
            for linea in archivo:
                campos = parsear_linea(linea)
                if len(campos) >= 6 and campos[0] != "":
                    reg = {
                        "id": campos[0], "tiempo": campos[1],
                        "x": campos[2], "y": campos[3],
                        "hit": campos[4], "condicion": campos[5]
                    }
                    registros.append(reg)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta}")
    return registros