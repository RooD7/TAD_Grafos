import grafo

class main(object):
	"""docstring for main"""
	def __init__(self, arg):
		self.arg = arg

	gf = grafo.grafo()

	while(1):
		print("1. Criar grafo")
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
			v1 = input("Digite o vertice de origem:")
			v2 = input("Digite o vertice de destino:")
			gf.insertA(v1,v2)
		elif (op == 3):
			v1 = input("Digite o vertice de origem:")
			v2 = input("Digite o vertice de destino:")
			if(gf.searchA(v1,v2)):
				print("A aresta ("+v1+","+v2+") existe.")
			else:
				print("A aresta ("+v1+","+v2+") nao existe.")
		elif (op == 4):
			v1 = input("Digite o vertice de origem:")
			v2 = input("Digite o vertice de destino:")
			gf.removeA(v1,v2)
			print("A aresta ("+v1+","+v2+") foi removida.")
		elif (op == 5):
			v1 = input("Digite o vertice:")
			gf.printV(v1)
		elif (op == 6):
			gf.printG(g)
		elif (op == 0):
			exit()