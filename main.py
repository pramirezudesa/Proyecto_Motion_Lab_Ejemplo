from src.cargar_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_datos
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit

direccion_datos = "datos/MotionLab_mock_data.csv"

# 1. Cargar datos desde el archivo
datos = cargar_datos(direccion_datos)

# 2. Filtrar datos válidos
datos_validos = []
for registro in datos:
    # if validar_registro(registro):
    datos_validos.append(registro)

# Procesamiento: Identificar IDs únicos para el análisis
ids_unicos = []
for r in datos_validos:
    if r["id_participante"] not in ids_unicos:
        ids_unicos.append(r["id_participante"])

# 3. Calcular métrica (y mostrar resultados)
print(f"{'ID':<8} | {'HITS':<6} | {'1er HIT':<10} | {'CONDICIÓN'}")
print("-" * 45)

for p_id in ids_unicos:
    # Usamos procesamiento para obtener el perfil del sujeto
    perfil_sujeto = filtrar_datos(datos_validos, p_id)

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
