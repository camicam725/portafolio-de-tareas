# -------- Cami Cam -------

def todos_distintos(secuencia):
    vistos = []                     # Lista para ir guardando los números ya vistos
    for numero in secuencia:        # Recorremos cada número de la secuencia
        if numero in vistos:        # Si el número ya apareció antes
            return False            # Entonces NO son todos distintos
        vistos.append(numero)       # Si no, lo agregamos a la lista de vistos
    return True                     # Si terminamos el ciclo sin repetidos, son distintos

# Ejemplos de prueba
print(todos_distintos([10, 20, 30]))  # True -> todos diferentes
print(todos_distintos([5, 7, 5]))     # False -> el 5 se repite