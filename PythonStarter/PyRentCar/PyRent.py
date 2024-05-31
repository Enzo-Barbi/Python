import os 
import sys
from collections import OrderedDict


dict_carros = {
    "0" : ["Chevrolet Tracker", 120],
    "1" : ["Chevrolet Onix", 90],
    "2" : ["Chevrolet Spin", 150],
    "3" : ["Hyundai HB20", 85],
    "4" : ["Hyundai Tucson", 120],
    "5" : ["Fiat Uno", 60],
    "6" : ["Fiat Mobi", 70],
    "7" : ["Fiat Pulse", 130],
}

dict_carros_alugados = {

}

def saudacao():
    print("========")
    print("Bem vindo à locadora de carros!")
    print("========")

def opcoes():
    print("o que deseja fazer?")
    print("0 - Mostrar Portifolio | 1 - Alugar um carro | 2 - Devolver um carro")
    escolha = input()

    if escolha == "0":
        portfolio()
    elif escolha == "1":
        alugar()
    elif escolha == "2":
        devolver()
    else:
        print("Escolha uma de nossas opções!")

def portfolio():
    os.system("clear")
    for key, value in dict_carros.items():
        print(f"[{key}] {value[0]} - R${value[1]} /dia ")

    print("")
    print("===========")
    print(" 0 - Continuar | 1 - Sair")
    escolha = input()
    if escolha == "1":
        sys.exit()

def alugar():
    os.system("clear")
    print("[ ALUGAR ] Dê uma olhada em nosso portfólio")
    print("")
    for key, value in dict_carros.items():
        print(f"[{key}] {value[0]} - R${value[1]} /dia ")

    print("")
    print("===========")
    print("Escolha o código do carro desejado: ")
    escolha_carro = input()
    print("Escolha quantos dias deseja alugar:")
    escolha_dias = int(input())
    os.system("clear")
    valor = dict_carros[escolha_carro][1] * escolha_dias

    print(f"Você escolheu {dict_carros[escolha_carro][0]} por {escolha_dias} dias")
    print(f"O aluguel totaliza em R$ {valor}. Deseja alugar?")
    print("")

    print("0 - SIM | 1 - NÃO")
    escolha = input()
    if escolha == "0":
        print(f"Parabéns você alugou o {dict_carros[escolha_carro][0]} por {escolha_dias} dias")
        dict_carros_alugados[escolha_carro] = dict_carros.pop(escolha_carro)


    print("")
    print("===========")
    print(" 0 - Continuar | 1 - Sair")
    escolha = input()
    if escolha == "1":
        sys.exit()
    


def devolver():
    os.system("clear")
    print("Segue a lista do carros alugados. Qual deseja devolver?")

    for key, value in dict_carros_alugados.items():
        print(f"[{key}] {value[0]} - R${value[1]} /dia ")

    print("Escolha o código do carro desejado: ")
    escolha_carro = input()
    print(f"Obrigado por devikver o carro {dict_carros_alugados[escolha_carro][0]}")
    dict_carros[escolha_carro] = dict_carros_alugados.pop(escolha_carro)
    dict_carros = OrderedDict()


    print("")
    print("===========")
    print(" 0 - Continuar | 1 - Sair")
    escolha = input()
    if escolha == "1":
        sys.exit()

while True:
    os.system("clear")
    saudacao()
    opcoes()
