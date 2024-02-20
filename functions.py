def my_function():
  print("Hi, I'm a function")

# Chamando uma função
def soma():
  print(1+1)

soma()

# Argumentos
def soma(num1, num2):
  print(num1 + num2)

# Argumentos - type hints
def soma(num1: int, num2: int):
  print(num1 + num2)


# Quando não sabemos quantos argumentos iremos receber, usamos o *
def print_nums(*nums):
  print(f"Nums: {nums[0]}")

nums = print_nums(1,2,3)

# Quando não sabemos quantos argumentos iremos receber, usamos o **, dessa forma podemos ter acesso a chaves e valores
def nomes(**names):
  print(f"Hello, {names['name1']}")
nomes = nomes(name1="Maria")


# Default Parameters
def print_countries(country = "Norway"):
  print("I am from " + country)

print_countries("Portugal")
print_countries("India")
print_countries()
print_countries("Brazil")

# Retornar valores
def soma(num1: int, num2: int):
  return num1 + num2

print(soma(5,5))


# Recursion
"""
Recursão é um conceito na programação em que uma função chama 
a si mesma repetidamente até atingir uma condição de parada. 
É como se a função se "dividisse" em várias instâncias 
menores de si mesma para resolver um problema.
"""

def fatorial(n):
    # Condição de parada
    if n == 1:
        print("fatorial(1) retorna 1")
        return 1
    # Chamar a função recursivamente
    else:
        resultado = n * fatorial(n - 1)
        print("fatorial({}) retorna {}".format(n, resultado))
        return resultado

# Calculando o fatorial de 5
resultado = fatorial(5)
print("O fatorial de 5 é:", resultado)
