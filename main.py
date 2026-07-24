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

resultado = None  # Inicializa a variável do resultado

# 5. Processamento dos Cálculos
if opcao == "1":
    resultado = num1 + num2
elif opcao == "2":
    resultado = num1 - num2
elif opcao == "3":
    resultado = num1 * num2
elif opcao == "4":
    if num2 == 0:
        print("Malandro, não dá pra dividir por zero né!")
        sys.exit()
    else:
        resultado = num1 / num2
else:
    print("Tá cego mlk? Escolhe de 1 a 4. Faz favor ne.")
    sys.exit()

# 6. Verificação do Resultado Maior que 100
print("\n" + "="*30)
print(f"Ó quantos que deu aq ó, lerdão: {resultado}")

if resultado > 100:
    print("\nSe liga: Como o bagulho é maior que 100, preciso de uns negócio ai.")
    cpf = input("Digita seu CPF ae fznd favor: \n")
    cartao = input("Agora passa o número do cartão ae: \n")
    print("\nGratidão malandragem, só regresso pro cê")

print("="*30)