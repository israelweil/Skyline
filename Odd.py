# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
num = 42
result = check_even_odd(num)
print(f"The number {num} is {result}.")

# agregue el print
print("2 + 2 = 4")

# agregue el print
print("2 + 2 = 5")

# Solicitar un número al usuario
numero = int(input("Introduce un número entero: "))

# Mensaje inicial
print("Comenzando a imprimir las iteraciones:")

# Bucle for para imprimir las iteraciones
for i in range(numero):
    # Imprimir el número de la iteración
    print(f"Esta es la iteración número {i + 1}")

# Mensaje final
print("Se completaron todas las iteraciones.")
