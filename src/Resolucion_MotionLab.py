

#=============================================================================
#=============================================================================
# PROYECTO: MOTIONLAB
#=============================================================================
#=============================================================================


#=============================================================================
# ARCHIVO: src/carga_datos.py
# =============================================================================

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


# =============================================================================
# ARCHIVO: src/validacion_datos.py
# =============================================================================

def validar_registro(registro):
    """
    Qué hace la función: Valida que los datos críticos sean convertibles a números
    y que el hit sea un valor lógico reconocible.
    Parámetros: registro (dict)
    Retorna: bool
    """
    try:
        float(registro['tiempo'])
        float(registro['x'])
        float(registro['y'])
        
        valor_hit = registro['hit'].strip().lower()
        if valor_hit not in ['true', 'false', '1', '0']:
            return False
            
        return True
    except (ValueError, KeyError):
        return False


# =============================================================================
# ARCHIVO: src/procesamiento_datos.py
# =============================================================================

def filtrar_por_participante(datos, id_participante):
    """
    Qué hace la función: Filtra los registros de un ID y los organiza en 
    listas para análisis de series temporales.
    Parámetros: datos (list), id_participante (str)
    Retorna: dict con las listas de datos del participante.
    """
    perfil = {
        "id": id_participante,
        "tiempo": [],
        "hit": [],
        "condicion": ""
    }
    for reg in datos:
        if str(reg['id']) == str(id_participante):
            perfil["tiempo"].append(float(reg['tiempo']))
            perfil["hit"].append(reg['hit'].lower() in ['true', '1'])
            if not perfil["condicion"]:
                perfil["condicion"] = reg['condicion']
    return perfil


# =============================================================================
# ARCHIVO: src/metricas.py
# =============================================================================

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


# =============================================================================
# ARCHIVO: main.py
# =============================================================================

# Importación de funciones a partir de otros scripts
from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit

# 1. Cargar datos desde el archivo
datos = cargar_datos("MotionLab_mock_data.csv")

# 2. Filtrar datos válidos
datos_validos = []
for registro in datos:
    if validar_registro(registro):
        datos_validos.append(registro)

#Procesamiento: Identificar IDs únicos para el análisis 
ids_unicos = []
for r in datos_validos:
    if r['id'] not in ids_unicos:
        ids_unicos.append(r['id'])

# 3. Calcular métrica (y mostrar resultados)
print(f"{'ID':<8} | {'HITS':<6} | {'1er HIT':<10} | {'CONDICIÓN'}")
print("-" * 45)

for p_id in ids_unicos:
    # Usamos procesamiento para obtener el perfil del sujeto
    perfil_sujeto = filtrar_por_participante(datos_validos, p_id)
    
    # 4. Mostrar resultado (Usando las funciones de metricas.py)
    hits = calcular_hits_totales(perfil_sujeto)
    t_primero = calcular_tiempo_primer_hit(perfil_sujeto)
    
    # OPCIONAL: Calcular hits por bloques 
    # ventana_bloque = 5
    # bloques = calcular_hits_por_bloques(perfil_sujeto, ventana_bloque)
    
    t_fmt = f"{t_primero:.2f}s" if t_primero is not None else "N/A"
    print(f"{p_id:<8} | {hits:<6} | {t_fmt:<10} | {perfil_sujeto['condicion']}")
    # Mostrar bloques si se calculan
    # print(f"Hits por bloques (ventana {ventana_bloque}): {bloques}")