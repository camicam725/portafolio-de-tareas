# P-2.33 Write a Python program that inputs a polynomial in standard algebraic
# notation and outputs the first derivative of that polynomial.

# ------Camila Cameras R

import re

def derivar_polinomio(polinomio):
    # Eliminar espacios
    polinomio = polinomio.replace(" ", "")

    # Separar términos usando + y -
    terminos = re.findall(r'[+-]?[^+-]+', polinomio)

    derivada = []

    for termino in terminos:
        # Caso 1: término con x y exponente (ej: 3x^2)
        if 'x^' in termino:
            coef, exp = termino.split('x^')
            coef = 1 if coef in ['', '+'] else -1 if coef == '-' else int(coef)
            exp = int(exp)

            nuevo_coef = coef * exp
            nuevo_exp = exp - 1

            if nuevo_exp == 1:
                derivada.append(f"{nuevo_coef}x")
            elif nuevo_exp == 0:
                derivada.append(str(nuevo_coef))
            else:
                derivada.append(f"{nuevo_coef}x^{nuevo_exp}")

        # Caso 2: término lineal (ej: -2x)
        elif 'x' in termino:
            coef = termino.replace('x', '')
            coef = 1 if coef in ['', '+'] else -1 if coef == '-' else int(coef)
            derivada.append(str(coef))

        # Caso 3: término constante (su derivada es 0)
        else:
            continue

    # Unir términos y corregir signos
    resultado = " + ".join(derivada)
    resultado = resultado.replace("+ -", "- ")

    return resultado if resultado else "0"


# Entrada del usuario
polinomio = input("Ingresa el polinomio: ")

# Salida
print("La primera derivada es:")
print(derivar_polinomio(polinomio))