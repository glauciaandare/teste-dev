def fibonacci(number):

    a, b = 0, 1
    while a <= number:
        if a == number:
            return True
        a, b = b, a+b
    return False

number = int(input("Digite um número, para verificar se pertence a sequência: "))
print (f"A sequência fibonacci é: {number}")

if fibonacci(number):
    print(f"O número {number} pertence a sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence a sequência de Fibonacci.")  