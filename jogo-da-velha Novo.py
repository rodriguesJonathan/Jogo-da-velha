import colorama
colorama.init()

espaco = "             "
print("\n"+espaco+"Jogo da velha!\n")
Jogador1,Jogador2,buffer = str(input("Nome do primeiro jogador: ")),str(input("Nome do segundo jogador: ")),str(input("Clique enter para iniciar o jogo.\n"))
va,xa,oa,final,final2 =['X','O'], '\033[34m'+'X'+'\033[0;0m','\033[34m'+'O'+'\033[0;0m',espaco+'\033[31m'+Jogador1+" ganhou!\n"+espaco+"Fim de jogo."'\033[0;0m',espaco+'\033[31m'+ Jogador2+" ganhou!\n"+espaco+"Fim de jogo."'\033[0;0m'
if buffer == "configurar":
	num = int(input("Digite o numero de espaços desejados\n"))
	espaco = num*" "
print("\n"+espaco+Jogador1+" será "+xa+"\n"+espaco+Jogador2+" será "+oa)
a,x,xv,ov = 0,[1,2,3,4,5,6,7,8,9],'\033[31m'+'X'+'\033[0;0m','\033[31m'+'O'+'\033[0;0m'
print("\n"+espaco,x[0],"|",x[1],"|",x[2],"\n"+espaco+"---|---|---\n"+espaco,x[3],"|",x[4],"|",x[5],"\n"+espaco+"---|---|---\n"+espaco,x[6],"|",x[7],"|",x[8],"\n")
usado,xo,finais,xov,jogadores,ganhou,muda = [],[xa,oa],[final,final2],[xv,ov],[Jogador1,Jogador2],0,2
while ganhou < 1:
	muda -= 2
	while muda < 2:
		nj = int(input(jogadores[muda]+", em que numero vai pôr "+va[muda]+"? "))
		while nj in usado or nj < 1 or nj > 9:
			print("Opção inválida.\nOu esse espaço já foi preenchido,\nOu o numero não é de 1 à 9.")
			nj = int(input("Por favor "+jogadores[muda]+", diga outro numero. "))
		while nj != x[a]:
			a += 1
		x.pop(a),x.insert(a,xo[muda]),usado.append(nj)
		a = 0
		print("\n\n\n\n\n\n\n\n\n\n\n\n"+espaco,x[0],"|",x[1],"|",x[2],"\n"+espaco+"---|---|---\n"+espaco,x[3],"|",x[4],"|",x[5],"\n"+espaco+"---|---|---\n"+espaco,x[6],"|",x[7],"|",x[8],"\n\n\n\n\n\n")
		j,o,n = 0,1,2
		for i in range(3):    
			if x[j] == x[o] == x[n] == xo[muda]:
				print(finais[muda])
				x.pop(j),x.insert(j,xov[muda]),x.pop(o),x.insert(o,xov[muda]),x.pop(n),x.insert(n,xov[muda])
				ganhou,muda = ganhou+1,muda+1
			j,o,n = j+3,o+3,n+3
		j,o,n = 0,3,6
		for i in range(3):
			if x[j] == x[o] == x[n] == xo[muda]:
				print(finais[muda])
				x.pop(j),x.insert(j,xov[muda]),x.pop(o),x.insert(o,xov[muda]),x.pop(n),x.insert(n,xov[muda])
				ganhou,muda = ganhou+1,muda+1
			j,o,n = j+1,o+1,n+1
		if x[0] == x[4] == x[8] == xo[muda]:
			print(finais[muda])
			x.pop(0),x.insert(0,xov[muda]),x.pop(4),x.insert(4,xov[muda]),x.pop(8),x.insert(8,xov[muda])
			ganhou,muda = ganhou+1,muda+1
		elif x[2] == x[4] == x[6] == xo[muda]:
			print(finais[muda])
			x.pop(2),x.insert(2,xov[muda]),x.pop(4),x.insert(4,xov[muda]),x.pop(6),x.insert(6,xov[muda])
			ganhou,muda = ganhou+1,muda+1
		elif len(usado) == 9:
			print(espaco+"Deu velha:")
			ganhou,muda = ganhou+1,muda+1
		muda += 1
print("\n"+espaco,x[0],"|",x[1],"|",x[2],"\n"+espaco+"---|---|---\n"+espaco,x[3],"|",x[4],"|",x[5],"\n"+espaco+"---|---|---\n"+espaco,x[6],"|",x[7],"|",x[8],"\n")