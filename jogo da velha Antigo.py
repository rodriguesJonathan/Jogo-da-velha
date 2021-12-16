import colorama
colorama.init()

espaco = "              "
print("\n"+espaco+"Jogo da velha!\n")
Jogador1 = str(input("Nome de um jogador: "))
Jogador2 = str(input("Nome do outro jogador: "))
buffer = input("Clique enter para iniciar o jogo.\n")
xAzul,oAzul = '\033[34m'+'X'+'\033[0;0m',    '\033[34m'+'O'+'\033[0;0m'
final,final2 = '\033[31m'+ Jogador1+" ganhou!\nFim de jogo."'\033[0;0m','\033[31m'+ Jogador2+" ganhou!\nFim de jogo."'\033[0;0m'

if buffer == "conf":
	num = int(input("Digite o numero de espaços desejados\n"))
	espaco = num*" "
print("\n"+espaco+Jogador1+" será "+xAzul+"\n"+espaco+Jogador2+" será "+oAzul)
a,b,c,d,e,f,g,h,i = 1,2,3,4,5,6,7,8,9
print("\n"+espaco,a,"|",b,"|",c,"\n"+espaco+"---|---|---\n"+espaco,d,"|",e,"|",f,"\n"+espaco+"---|---|---\n"+espaco,g,"|",h,"|",i,"\n")
usado = []
while True:
	j1 = int(input(Jogador1+", em que numero vai pôr X? "))
	while j1 in usado or j1 < 1 or j1 > 9:
		print("Opção inválida.\nOu esse espaço já foi preenchido,\nOu o numero não é de 1 à 9.")
		j1 = int(input("Por favor "+Jogador1+", diga outro numero. "))
	if j1 == 1 and j1 not in usado:
		a = xAzul
		usado.append(j1)
	elif j1 == 2 and j1 not in usado:
		b = xAzul
		usado.append(j1)
	elif j1 == 3 and j1 not in usado:
		c = xAzul
		usado.append(j1)
	elif j1== 4 and j1 not in usado:
		d = xAzul
		usado.append(j1)
	elif j1 == 5 and j1 not in usado:
		e = xAzul
		usado.append(j1)
	elif j1 == 6 and j1 not in usado:
		f = xAzul
		usado.append(j1)
	elif j1 == 7 and j1 not in usado:
		g = xAzul
		usado.append(j1)
	elif j1 == 8 and j1 not in usado:
		h = xAzul
		usado.append(j1)
	elif j1 == 9 and j1 not in usado:
		i = xAzul
		usado.append(j1)
	print("\n\n\n\n\n\n"+espaco,a,"|",b,"|",c,"\n"+espaco+"---|---|---\n"+espaco,d,"|",e,"|",f,"\n"+espaco+"---|---|---\n"+espaco,g,"|",h,"|",i,"\n\n\n\n\n\n")
	if a == d == g == xAzul:
		print(final)
		a = d = g = '\033[31m'+'X'+'\033[0;0m'
		break
	elif b == e == h == xAzul:
		print(final)
		b = e = h = '\033[31m'+'X'+'\033[0;0m'
		break
	elif c == f == i == xAzul:
		print(final)
		c = f = i = '\033[31m'+'X'+'\033[0;0m'
		break
	elif a == b == c == xAzul:
		print(final)
		a = b = c = '\033[31m'+'X'+'\033[0;0m'
		break
	elif d == e == f == xAzul:
		print(final)
		d = e = f = '\033[31m'+'X'+'\033[0;0m'
		break
	elif g == h == i == xAzul:
		print(final)
		g = h = i = '\033[31m'+'X'+'\033[0;0m'
		break
	elif a == e == i == xAzul:
		print(final)
		a = e = i = '\033[31m'+'X'+'\033[0;0m'
		break
	elif c == e == g == xAzul:
		print(final)
		c = e = g = '\033[31m'+'X'+'\033[0;0m'
		break
	elif len(usado) == 9:
		print(espaco+"Deu velha:")
		break
	j2 = int(input(Jogador2+", em que numero vai pôr O? "))
	if j2 in usado or j2 < 1 or j2 > 9:
		while j2 in usado or j2 < 1 or j2 > 9:
			print("Opção inválida.\nOu esse espaço já foi preenchido,\nOu o numero não é de 1 à 9.")
			j2 = int(input("Por favor"+Jogador2+", diga outro numero. "))
	if j2 == 1 and j2 not in usado:
		a = oAzul
		usado.append(j2)
	elif j2 == 2 and j2 not in usado:
		b = oAzul
		usado.append(j2)
	elif j2 == 3 and j2 not in usado:
		c = oAzul
		usado.append(j2)
	elif j2 == 4 and j2 not in usado:
		d = oAzul
		usado.append(j2)
	elif j2 == 5 and j2 not in usado:
		e = oAzul
		usado.append(j2)
	elif j2 == 6 and j2 not in usado:
		f = oAzul
		usado.append(j2)
	elif j2 == 7 and j2 not in usado:
		g = oAzul
		usado.append(j2)
	elif j2 == 8 and j2 not in usado:
		h = oAzul
		usado.append(j2)
	elif j2 == 9 and j2 not in usado:
		i = oAzul
		usado.append(j2)
	print("\n\n\n\n\n\n"+espaco,a,"|",b,"|",c,"\n"+espaco+"---|---|---\n"+espaco,d,"|",e,"|",f,"\n"+espaco+"---|---|---\n"+espaco,g,"|",h,"|",i,"\n\n\n\n\n\n")
	if a == d == g == oAzul:
		print(final2)
		a = d = g = '\033[31m'+'O'+'\033[0;0m'
		break
	elif b == e == h == oAzul:
		print(final2)
		b = e = h = '\033[31m'+'O'+'\033[0;0m'
		break
	elif c == f == i == oAzul:
		print(final2)
		c = f = i = '\033[31m'+'O'+'\033[0;0m'
		break
	elif a == b == c == oAzul:
		print(final2)
		a = b = c = '\033[31m'+'O'+'\033[0;0m'
		break
	elif d == e == f == oAzul:
		print(final2)
		d = e = f = '\033[31m'+'O'+'\033[0;0m'
		break
	elif g == h == i == oAzul:
		print(final2)
		g = h = i = '\033[31m'+'O'+'\033[0;0m'
		break
	elif a == e == i == oAzul:
		print(final2)
		a = e = i = '\033[31m'+'O'+'\033[0;0m'
		break
	elif c == e == g == oAzul:
		print(final2)
		c = e = g = '\033[31m'+'O'+'\033[0;0m'
		break
print("\n"+espaco,a,"|",b,"|",c,"\n"+espaco+"---|---|---\n"+espaco,d,"|",e,"|",f,"\n"+espaco+"---|---|---\n"+espaco,g,"|",h,"|",i,"\n")