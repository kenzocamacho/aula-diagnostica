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

opcao = input("Digite o número da operação: ")