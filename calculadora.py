#calculadora.py

def sumar(a, b):
	return a + b
	
def restar (a, b):
	return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b

if __name__ == "__main__":
	num1 = 10
	num2 = 4
	
	print(f"El resultado de la suma es: {sumar(num1, num2)}")
	print(f"El resultado de la resta es: {restar(num1, num2)}")
	print(f"El resultado de la multiplicación es: {multiplicación(num1, num2)}")
	print(f"El resultado de la division es: {division(num1, num2)}")