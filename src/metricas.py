
def calcular_hits_totales(datos_participante):
    """
    Qué hace la función: Cuenta la cantidad total de eventos 'hit' exitosos.
    Parámetros: datos_participante (dict)
    Retorna: int
    """
    total = 0
    for h in datos_participante['hit']:
        if h:
            total += 1
    return total

def calcular_tiempo_primer_hit(datos_participante):
    """
    Qué hace la función: Encuentra el primer tiempo donde hit es True.
    Parámetros: datos_participante (dict)
    Retorna: float o None si no hubo hits.
    """
    for i in range(len(datos_participante['hit'])):
        if datos_participante['hit'][i]:
            return datos_participante['tiempo'][i]
    return None

def calcular_hits_por_bloques(datos_participante, ventana):
    """
    Qué hace la función: (Opcional) Cuenta hits en bloques de registros.
    Parámetros: datos_participante (dict), ventana (int)
    Retorna: list[int]
    """
    hits_bloque = []
    for i in range(0, len(datos_participante['hit']), ventana):
        segmento = datos_participante['hit'][i : i + ventana]
        hits_bloque.append(sum(segmento))
    return hits_bloque
