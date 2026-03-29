def validar_registro(registro):
    """
    Qué hace la función: Valida que los datos críticos sean convertibles a números
    y que el hit sea un valor lógico reconocible.
    Parámetros: registro (dict)
    Retorna: bool
    """
    try:
        
        float(registro['x'])
        float(registro['y'])
        
        valor_hit = registro['hit'].strip().lower()
        if valor_hit not in ['true', 'false', '1', '0']:
            return False
        
        tiempo = float(registro['tiempo'])
        if tiempo<0:
            return False
        
        return True
    except (ValueError, KeyError):
        return False