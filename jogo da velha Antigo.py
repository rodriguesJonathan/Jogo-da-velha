import colorama, os
def limparTerminal():
	os.system("cls||clear")

def mostrarTabuleiro():
	global espaco,tabela11,tabela12,tabela13,tabela21,tabela22,tabela23,tabela31,tabela32,tabela33
	print("\n"+espaco,tabela11,"|",tabela12,"|",tabela13)
	print(espaco+"---|---|---")
	print(espaco,tabela21,"|",tabela22,"|",tabela23)
	print(espaco+"---|---|---")
	print(espaco,tabela31,"|",tabela32,"|",tabela33,"\n")

colorama.init()

espaco = " "*14
print("\n"+espaco+"Jogo da velha!\n")
Jogador1 = str(input("Nome de um jogador: "))
Jogador2 = str(input("Nome do outro jogador: "))
buffer = input("Clique enter para iniciar o jogo.\n")


limparTerminal()
xAzul,oAzul = '\033[34m'+'X'+'\033[0;0m',    '\033[34m'+'O'+'\033[0;0m'
xVermelho, oVermelho = '\033[31m'+'X'+'\033[0;0m', '\033[31m'+'O'+'\033[0;0m'
mensagemFinal = '\033[31m%s ganhou!\nFim de jogo.\033[0;0m'

if buffer == "conf":
	num = int(input("Digite o numero de espaços desejados\n"))
	espaco = num*" "
	limparTerminal()
print("\n"+espaco+Jogador1+" será "+xAzul+"\n"+espaco+Jogador2+" será "+oAzul)
tabela11,tabela12,tabela13,tabela21,tabela22,tabela23,tabela31,tabela32,tabela33 = 1,2,3,4,5,6,7,8,9
mostrarTabuleiro()
campoTabelaUsado = []

while True:
	escolhaCampoJogador1 = int(input(Jogador1+", em que numero vai pôr X? "))
	while escolhaCampoJogador1 in campoTabelaUsado or escolhaCampoJogador1 < 1 or escolhaCampoJogador1 > 9:
		print("Opção inválida.\nOu esse espaço já foi preenchido,\nOu o numero não é de 1 à 9.")
		escolhaCampoJogador1 = int(input("Por favor "+Jogador1+", diga outro numero. "))
	if escolhaCampoJogador1 == 1 and escolhaCampoJogador1 not in campoTabelaUsado:
		tabela11 = xAzul
		campoTabelaUsado.append(escolhaCampoJogador1)
	elif escolhaCampoJogador1 == 2 and escolhaCampoJogador1 not in campoTabelaUsado:
		tabela12 = xAzul
		campoTabelaUsado.append(escolhaCampoJogador1)
	elif escolhaCampoJogador1 == 3 and escolhaCampoJogador1 not in campoTabelaUsado:
		tabela13 = xAzul
		campoTabelaUsado.append(escolhaCampoJogador1)
	elif escolhaCampoJogador1== 4 and escolhaCampoJogador1 not in campoTabelaUsado:
		tabela21 = xAzul
		campoTabelaUsado.append(escolhaCampoJogador1)
	elif escolhaCampoJogador1 == 5 and escolhaCampoJogador1 not in campoTabelaUsado:
		tabela22 = xAzul
		campoTabelaUsado.append(escolhaCampoJogador1)
	elif escolhaCampoJogador1 == 6 and escolhaCampoJogador1 not in campoTabelaUsado:
		tabela23 = xAzul
		campoTabelaUsado.append(escolhaCampoJogador1)
	elif escolhaCampoJogador1 == 7 and escolhaCampoJogador1 not in campoTabelaUsado:
		tabela31 = xAzul
		campoTabelaUsado.append(escolhaCampoJogador1)
	elif escolhaCampoJogador1 == 8 and escolhaCampoJogador1 not in campoTabelaUsado:
		tabela32 = xAzul
		campoTabelaUsado.append(escolhaCampoJogador1)
	elif escolhaCampoJogador1 == 9 and escolhaCampoJogador1 not in campoTabelaUsado:
		tabela33 = xAzul
		campoTabelaUsado.append(escolhaCampoJogador1)
	if tabela11 == tabela21 == tabela31 == xAzul:
		print(mensagemFinal%Jogador1)
		tabela11 = tabela21 = tabela31 = xVermelho
		break
	elif tabela12 == tabela22 == tabela32 == xAzul:
		print(mensagemFinal%Jogador1)
		tabela12 = tabela22 = tabela32 = xVermelho
		break
	elif tabela13 == tabela23 == tabela33 == xAzul:
		print(mensagemFinal%Jogador1)
		tabela13 = tabela23 = tabela33 = xVermelho
		break
	elif tabela11 == tabela12 == tabela13 == xAzul:
		print(mensagemFinal%Jogador1)
		tabela11 = tabela12 = tabela13 = xVermelho
		break
	elif tabela21 == tabela22 == tabela23 == xAzul:
		print(mensagemFinal%Jogador1)
		tabela21 = tabela22 = tabela23 = xVermelho
		break
	elif tabela31 == tabela32 == tabela33 == xAzul:
		print(mensagemFinal%Jogador1)
		tabela31 = tabela32 = tabela33 = xVermelho
		break
	elif tabela11 == tabela22 == tabela33 == xAzul:
		print(mensagemFinal%Jogador1)
		tabela11 = tabela22 = tabela33 = xVermelho
		break
	elif tabela13 == tabela22 == tabela31 == xAzul:
		print(mensagemFinal%Jogador1)
		tabela13 = tabela22 = tabela31 = xVermelho
		break
	elif len(campoTabelaUsado) == 9:
		print(espaco+"Deu velha:")
		break

	limparTerminal()
	mostrarTabuleiro()


	escolhaCampoJogador2 = int(input(Jogador2+", em que numero vai pôr O? "))
	if escolhaCampoJogador2 in campoTabelaUsado or escolhaCampoJogador2 < 1 or escolhaCampoJogador2 > 9:
		while escolhaCampoJogador2 in campoTabelaUsado or escolhaCampoJogador2 < 1 or escolhaCampoJogador2 > 9:
			print("Opção inválida.\nOu esse espaço já foi preenchido,\nOu o numero não é de 1 à 9.")
			escolhaCampoJogador2 = int(input("Por favor"+Jogador2+", diga outro numero. "))
	if escolhaCampoJogador2 == 1 and escolhaCampoJogador2 not in campoTabelaUsado:
		tabela11 = oAzul
		campoTabelaUsado.append(escolhaCampoJogador2)
	elif escolhaCampoJogador2 == 2 and escolhaCampoJogador2 not in campoTabelaUsado:
		tabela12 = oAzul
		campoTabelaUsado.append(escolhaCampoJogador2)
	elif escolhaCampoJogador2 == 3 and escolhaCampoJogador2 not in campoTabelaUsado:
		tabela13 = oAzul
		campoTabelaUsado.append(escolhaCampoJogador2)
	elif escolhaCampoJogador2 == 4 and escolhaCampoJogador2 not in campoTabelaUsado:
		tabela21 = oAzul
		campoTabelaUsado.append(escolhaCampoJogador2)
	elif escolhaCampoJogador2 == 5 and escolhaCampoJogador2 not in campoTabelaUsado:
		tabela22 = oAzul
		campoTabelaUsado.append(escolhaCampoJogador2)
	elif escolhaCampoJogador2 == 6 and escolhaCampoJogador2 not in campoTabelaUsado:
		tabela23 = oAzul
		campoTabelaUsado.append(escolhaCampoJogador2)
	elif escolhaCampoJogador2 == 7 and escolhaCampoJogador2 not in campoTabelaUsado:
		tabela31 = oAzul
		campoTabelaUsado.append(escolhaCampoJogador2)
	elif escolhaCampoJogador2 == 8 and escolhaCampoJogador2 not in campoTabelaUsado:
		tabela32 = oAzul
		campoTabelaUsado.append(escolhaCampoJogador2)
	elif escolhaCampoJogador2 == 9 and escolhaCampoJogador2 not in campoTabelaUsado:
		tabela33 = oAzul
		campoTabelaUsado.append(escolhaCampoJogador2)

	if tabela11 == tabela21 == tabela31 == oAzul:
		print(mensagemFinal%Jogador2)
		tabela11 = tabela21 = tabela31 = oVermelho
		break
	elif tabela12 == tabela22 == tabela32 == oAzul:
		print(mensagemFinal%Jogador2)
		tabela12 = tabela22 = tabela32 = oVermelho
		break
	elif tabela13 == tabela23 == tabela33 == oAzul:
		print(mensagemFinal%Jogador2)
		tabela13 = tabela23 = tabela33 = oVermelho
		break
	elif tabela11 == tabela12 == tabela13 == oAzul:
		print(mensagemFinal%Jogador2)
		tabela11 = tabela12 = tabela13 = oVermelho
		break
	elif tabela21 == tabela22 == tabela23 == oAzul:
		print(mensagemFinal%Jogador2)
		tabela21 = tabela22 = tabela23 = oVermelho
		break
	elif tabela31 == tabela32 == tabela33 == oAzul:
		print(mensagemFinal%Jogador2)
		tabela31 = tabela32 = tabela33 = oVermelho
		break
	elif tabela11 == tabela22 == tabela33 == oAzul:
		print(mensagemFinal%Jogador2)
		tabela11 = tabela22 = tabela33 = oVermelho
		break
	elif tabela13 == tabela22 == tabela31 == oAzul:
		print(mensagemFinal%Jogador2)
		tabela13 = tabela22 = tabela31 = oVermelho
		break
	limparTerminal()
	mostrarTabuleiro()
limparTerminal()
mostrarTabuleiro()