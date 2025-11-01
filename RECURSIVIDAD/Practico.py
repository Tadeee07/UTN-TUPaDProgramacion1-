def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
        
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
        
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
        
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
        
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        # Asume que un "bloque" se refiere a la suma de 1 + 2 + ... + n
        return n + contar_bloques(n - 1)
        
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        cuenta = 1 if (numero % 10) == digito else 0
        return cuenta + contar_digito(numero // 10, digito)
        
# aca podes agregar codigo para probarlo

if __name__ == "__main__":
    # ejemplo de uso de las funciones

    num = 5
    print(f"Factorial de {num}: {factorial(num)}")
    
    pos = 7
    print(f"Fibonacci en posicion {pos}: {fibonacci(pos)}")
    
    base = 2
    exponente = 3
    print(f"{base} elevado a {exponente}: {potencia(base, exponente)}")
    
    decimal = 10
    print(f"Decimal {decimal} en binario: {decimal_a_binario(decimal)}")
    
    palabra = "radar"
    print(f"La palabra '{palabra}' es palindromo: {es_palindromo(palabra)}")
    
    numero = 1234
    print(f"Suma de digitos de {numero}: {suma_digitos(numero)}")
    
    niveles = 4
    print(f"Total de bloques para una piramide con {niveles} niveles: {contar_bloques(niveles)}")
    
    numero = 12233421
    digito = 2
    print(f"El digito {digito} aparece {contar_digito(numero, digito)} veces en el numero {numero}")