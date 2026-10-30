#calculadora.py

def sumar(a, b):
	return a + b
	
def restar (a, b):
	return a - b

if __name__ == "__main__":
	num1 = 10
	num2 = 4
	
	print(f"El resultado de la suma es: {sumar(num1, num2)}")
	print(f"El resultado de la resta es: {restar(num1, num2)}")
