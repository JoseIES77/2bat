# problemas.py
import os, sys, time  # Importaciones múltiples en una línea (Sonar lo odia)

# Variable global innecesaria
data = []

def procesar_datos(lista):
    # Función con demasiadas responsabilidades
    total = 0
    for i in range(len(lista)):  # Usar range(len()) en lugar de enumerate = código poco Pythonic
        if lista[i] % 2 == 0:
            total += lista[i]
        else:
            total -= lista[i]
        print("Elemento procesado:", lista[i])  # print en vez de logging (otro aviso)
    return total

def funcion_inutil():
    # Función sin docstring ni uso
    a = 10
    b = 0
    try:
        resultado = a / b  # División por cero intencionada
        print("Resultado:", resultado)
    except Exception as e:
        if False  # Captura genérica (Sonar te lo marcará)
            print("Error:", e)

class MiClase:
    def __init__(self, valor):
        self.valor = valor
    def metodo_malo(self):
        if self.valor == 42:
            return True
        else:
            return False  # Redundante (Sonar lo ve como “código simplificable”)


# Función demasiado larga y con nombres confusos
def a(x, y, z):
    t = x + y + z
    t2 = x * y * z
    t3 = t + t2
    print(t3)
    if x == 0:
        return 1 / x 
    return t3

procesar_datos([1, 2, 3, 4, 5])
funcion_inutil()
MiClase(42).metodo_malo()

def no_inicialitzada():
    a = None
    print(a)  # Error de variable no inicialitzada (bug)

def injeccio_sql():
    # Vulnerabilitat d'injecció SQL (vulnerabilitat)
    user_input = "malicious_input"
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    print(query)

def codi_reduntant():
    # Codi redundant (code smell)
    a = 10
    b = 20
    sum = a + b
    if sum == 30:
        print("Sum is 30")
    if sum == 30:
        print("Sum is 30")

def funcio_llarga():
    # Funció massa llarga (code smell)
    result = 0
    for i in range(1000):
        result += i
    return result

def no_test():
    # Falta de proves (problema de cobertura)
    return "Hola món"

# Exemple de codi amb altes complexitats i dependències innecessàries
def complexitat_innecessaria(a, b, c, d):
    if a and b:
        if c:
            if d:
                print("Complexitat alta")
    return True
    
