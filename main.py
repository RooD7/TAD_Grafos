import grafo

class main(object):
	"""docstring for main"""
	def __init__(self, arg):
		self.arg = arg

	gf = grafo.grafo()

	while(1):
		print("\n1. Criar grafo")
		print("2. Inserir aresta")
		print("3. Pesquisar aresta")
		print("4. Remover aresta")
		print("5. Mostrar vertice")
		print("6. Imprimir grafo")
		print("0. Sair")
		op = int(input("Digite a opcao desejada:"))

		if (op == 1):
			g = gf.create()
		elif (op == 2):
			v1 = int(input("Digite o vertice de origem:"))
			v2 = int(input("Digite o vertice de destino:"))
			gf.insertA(g,v1,v2)
		elif (op == 3):
			v1 = int(input("Digite o vertice de origem:"))
			v2 = int(input("Digite o vertice de destino:"))
			if(gf.searchA(g,v1,v2)):
				print("A aresta ("+str(v1)+","+str(v2)+") existe.")
			else:
				print("A aresta ("+str(v1)+","+str(v2)+") nao existe.")
		elif (op == 4):
			v1 = int(input("Digite o vertice de origem:"))
			v2 = int(input("Digite o vertice de destino:"))
			gf.removeA(g,v1,v2)
			print("A aresta ("+str(v1)+","+str(v2)+") foi removida.")
		elif (op == 5):
			v1 = int(input("Digite o vertice:"))
			gf.printV(g,v1)
		elif (op == 6):
			gf.printG(g)
		elif (op == 0):
			exit()