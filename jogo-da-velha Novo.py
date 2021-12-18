import colorama, os
colorama.init()

def limparTerminal():
	os.system("cls||clear")

def mostrarTabuleiro():
	global espaco,tabela
	print("\n"+espaco,tabela[0],"|",tabela[1],"|",tabela[2])
	print(espaco+"---|---|---")
	print(espaco,tabela[3],"|",tabela[4],"|",tabela[5])
	print(espaco+"---|---|---")
	print(espaco,tabela[6],"|",tabela[7],"|",tabela[8],"\n")

limparTerminal()
print("\n"+" "*13+"Jogo da velha!\n")

Jogador1,Jogador2 = input("Nome do primeiro jogador: "),input("Nome do segundo jogador: ")
jogadores = [Jogador1,Jogador2]

espaco = " "*13
tabela = [1,2,3,4,5,6,7,8,9]
camposJaEscolhidos = []
campoAserAnalisado = 0

xAzul,oAzul = '\033[34m'+'X'+'\033[0;0m','\033[34m'+'O'+'\033[0;0m'
xVermelho,oVermelho = '\033[31m'+'X'+'\033[0;0m','\033[31m'+'O'+'\033[0;0m'

listaXO, listaAzulXO,listaVermelhaXO = ['X','O'], [xAzul,oAzul],[xVermelho,oVermelho]
mensagemFinal = espaco+"\033[31m%s ganhou!\n"+espaco+"Fim de jogo."'\033[0;0m'
ganhou,muda = 0,2

buffer = input("Clique enter para iniciar o jogo.\n")
if buffer == "configurar":
	num = int(input("Digite o numero de espaços desejados\n"))
	espaco = num*" "

print("\n"+espaco+Jogador1+" será "+xAzul+"\n"+espaco+Jogador2+" será "+oAzul)

limparTerminal()
mostrarTabuleiro()
while ganhou < 1:
	muda -= 2
	while muda < 2:
		campoEscolhido = int(input(jogadores[muda]+", em que numero vai pôr "+listaXO[muda]+"? "))
		while campoEscolhido in camposJaEscolhidos or campoEscolhido < 1 or campoEscolhido > 9:
			print("Opção inválida.\nOu esse espaço já foi preenchido,\nOu o numero não é de 1 à 9.")
			campoEscolhido = int(input("Por favor "+jogadores[muda]+", diga outro numero. "))
		while campoEscolhido != tabela[campoAserAnalisado]:
			campoAserAnalisado += 1
		tabela.pop(campoAserAnalisado),tabela.insert(campoAserAnalisado,listaAzulXO[muda]),camposJaEscolhidos.append(campoEscolhido)
		campoAserAnalisado = 0
		limparTerminal()
		mostrarTabuleiro()
		#Verificação de vitórias na vertical
		tabelaX1,tabelaX2,tabelaX3 = 0,1,2
		for i in range(3):    
			if tabela[tabelaX1] == tabela[tabelaX2] == tabela[tabelaX3] == listaAzulXO[muda]:
				tabela.pop(tabelaX1),tabela.insert(tabelaX1,listaVermelhaXO[muda]),tabela.pop(tabelaX2),tabela.insert(tabelaX2,listaVermelhaXO[muda]),tabela.pop(tabelaX3),tabela.insert(tabelaX3,listaVermelhaXO[muda])
				ganhou,muda,nomeDoVencedor = ganhou+1,muda+1, jogadores[muda]
			tabelaX1,tabelaX2,tabelaX3 = tabelaX1+3,tabelaX2+3,tabelaX3+3
		#Verificação de vitórias na horinzontal
		tabela1X,tabela2X,tabela3X = 0,3,6
		for i in range(3):
			if tabela[tabela1X] == tabela[tabela2X] == tabela[tabela3X] == listaAzulXO[muda]:
				tabela.pop(tabela1X),tabela.insert(tabela1X,listaVermelhaXO[muda]),tabela.pop(tabela2X),tabela.insert(tabela2X,listaVermelhaXO[muda]),tabela.pop(tabela3X),tabela.insert(tabela3X,listaVermelhaXO[muda])
				ganhou,muda,nomeDoVencedor = ganhou+1,muda+1, jogadores[muda]
			tabela1X,tabela2X,tabela3X = tabela1X+1,tabela2X+1,tabela3X+1
		#Verificação de vitórias na diagonal
		if tabela[0] == tabela[4] == tabela[8] == listaAzulXO[muda]:
			tabela.pop(0),tabela.insert(0,listaVermelhaXO[muda]),tabela.pop(4),tabela.insert(4,listaVermelhaXO[muda]),tabela.pop(8),tabela.insert(8,listaVermelhaXO[muda])
			ganhou,muda,nomeDoVencedor = ganhou+1,muda+1, jogadores[muda]
		elif tabela[2] == tabela[4] == tabela[6] == listaAzulXO[muda]:
			tabela.pop(2),tabela.insert(2,listaVermelhaXO[muda]),tabela.pop(4),tabela.insert(4,listaVermelhaXO[muda]),tabela.pop(6),tabela.insert(6,listaVermelhaXO[muda])
			ganhou,muda,nomeDoVencedor = ganhou+1,muda+1, jogadores[muda]
		#Verificação de empate
		if len(camposJaEscolhidos) == 9:
			print(espaco+"Deu velha!!")
			ganhou = 10
			break
		muda += 1
if ganhou == 1:
	limparTerminal()
	print(mensagemFinal%nomeDoVencedor.lower().capitalize())
	mostrarTabuleiro()