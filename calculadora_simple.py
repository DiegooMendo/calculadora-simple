
print("BIENVENIDO A MI CALCULADORA")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operador = input(
    "Que operación deseas realizar? (Suma, Resta, Multiplicación o División)")

resultado = 0

if operador == 'suma':
    resultado = num1 + num2
elif operador == 'resta':
    resultado = num1 - num2
elif operador == 'multiplicación':
    resultado = num1 * num2
elif operador == 'división':
    resultado = num1 / num2
print("El resultado es", resultado)
