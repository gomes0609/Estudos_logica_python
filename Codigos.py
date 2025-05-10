# 1. Verificar se um número é par ou ímpar
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 2. Verificar se um número é positivo, negativo ou zero
num = float(input("Digite um número: "))
if num > 0:
    print("Número positivo.")
elif num < 0:
    print("Número negativo.")
else:
    print("Zero.")

# 3. Calcular a tabuada de um número
num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 4. Contar de 1 a 10
for i in range(1, 11):
    print(i)

# 5. Soma de números de 1 a 100
soma = 0
for i in range(1, 101):
    soma += i
print("A soma de 1 a 100 é:", soma)

# 6. Verificar se um número é primo
num = int(input("Digite um número: "))
if num < 2:
    print("Não é primo.")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Não é primo.")
            break
    else:
        print("É primo.")

# 7. Inverter uma string
texto = input("Digite uma palavra: ")
invertida = texto[::-1]
print("Palavra invertida:", invertida)

# 8. Calcular fatorial de um número
num = int(input("Digite um número: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print("Fatorial de", num, "é", fatorial)

# 9. Contar vogais em uma string
texto = input("Digite uma frase: ").lower()
vogais = "aeiou"
cont = 0
for letra in texto:
    if letra in vogais:
        cont += 1
print("Número de vogais:", cont)

# 10. Verificar se um número é palíndromo
num = input("Digite um número: ")
if num == num[::-1]:
    print("É palíndromo.")
else:
    print("Não é palíndromo.")
