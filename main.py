import sys

nome = input("Qual seu nome malandro? \n")

if nome.lower() in ["luis", "felipe", "luis felipe", "luis felipe saff"]:
    print("Vaza irmão ngm chamou o cê aq n")
    sys.exit()

idade = int(input("Pdp, e qnts anos ce tem lek? \n"))

if idade <= 13:
    print("Slk mt novo pra usar isso aqui vaza")
    sys.exit()

num1 = float(input("Digita um número ae prç:\n"))
num2 = float(input("Digita outro número ae prç:\n"))

print("\nEscolha a operação prç:")
print("[1] Somar (+)")
print("[2] Subtrair (-)")
print("[3] Multiplicar (*)")
print("[4] Dividir (/)")

opcao = input("Digite ai q numero ce qr: ")

print("\n" + "="*30)
if opcao == "1":
    resultado = num1 + num2
    print(f"Resultado da Soma: {resultado}")
elif opcao == "2":
    resultado = num1 - num2
    print(f"Resultado da Subtração: {resultado}")
elif opcao == "3":
    resultado = num1 * num2
    print(f"Resultado da Multiplicação: {resultado}")
elif opcao == "4":
    # Evita que o programa quebre se o usuário tentar dividir por zero
    if num2 == 0:
        print("Malandro, não dá pra dividir por zero né")
    else:
        resultado = num1 / num2
        print(f"Resultado da Divisão: {resultado}")
else:
    print("Ce é cego, mlk? Escolhe de 1 a 4, cara. Faz favor fia")
print("="*30)