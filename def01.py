# Crie um programa que leia dois números e mostre a soma, a
# subtração, a multiplicação e a divisão entre eles



n1 = int(input("Insira o primeiro número: "))
n2 =int(input("Insira o segundo número: "))


def soma(a,b):
    soma = a + b
    print(F"RESULTADO DA SOMA: {soma}")


def divisao(a,b):
    div = a / b
    print(F"RESULTADO DA DIVISÃO: {div}")


def multiplicacao(a,b):
    mult = a * b
    print(F"RESULTADO DA MULTIPLICAÇÃO: {mult}")


def subtracao(a,b):
    sub = a - b
    print(F"RESULTADO DA SUBTRAÇÃO: {sub}")

soma( n1,n2)
divisao(n1,n2)
multiplicacao(n1,n2)
subtracao(n1,n2)



