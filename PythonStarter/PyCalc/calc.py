import os 

print("============")

operation = {
    "+" : "Soma",
    "-" : "Sub",
    "*" : "Multi",
    "/" : "Div",
    "^" : "Expo",
}


while True:
    os.system("clear")
    i = 0
    for op, name in operation.items():
        print(i, ":", name)
        i += 1
    print("")
    print("Escolha a operação que deseja realzar:")
    op = int(input())
    op_string = list(operation.keys())[op]

    print("")
    print(f"{op_string} Escolhida")
    print("")
    print(f"Qual o primeiro valor?")
    v1 = float(input())
    print(f"Qual o segundo valor?")
    v2 = float(input())

    if op == 0:
        result = v1 + v2
    elif op == 1:
        result = v1 - v2
    elif op == 2:
        result = v1 * v2
    elif op == 3:
        result = v1 / v2
    elif op == 4:
        result = v1 ** v2

    print("")
    print(f"{v1} {op_string} {v2} = {result}")
    print("")

    print("============")
    print("Deseja fazer mais alguma operação (Responda com S ou N)")
    comando = input()
    os.system("clear")
    if comando == "N":
        print("Obrigado por usar a calculadora do python :)")
        break


