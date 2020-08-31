# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!


print("\n******************* Python Calculator *******************")

print("V1 - Números interios by Dolly")

print("Escolha uma das operações: \n1- Soma \n2- Subtração \n3-Multiplicação \n4-Divisão")

operacao = int(input("Qual operação você quer realizar?"))

numero1 = int(input("Digite o primeiro número:"))

numero2 = int(input("Digite o segundo número:"))

if operacao == 1:
    print("O resultado é:", numero1 + numero2)

if operacao == 2:
    print("O resultado é:", numero1 - numero2)

if operacao == 3:
    print("O resultado é:", numero1 * numero2)

if operacao == 4:
    print("O resultado é:", numero1 / numero2)

if operacao > 4:
    print("Escolha uma operação entre 1 e 4")
