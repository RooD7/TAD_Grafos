

class grafo(object):
	"""docstring for grafo"""
	
	TAM = 20
	def __init__(self):
		self.v = [0] * self.TAM
		for i in range(self.TAM):
			self.v[i] = [0] * self.TAM

		char = ord('A')
		for i in range(self.TAM):
			self.v[i].append(chr(i))
			char += 1

	def create(self):
		return self.v

	def insertA(self, v1, v2):
		""" Insere arestas no grafo """
		pass

	def searchA(self, v1, v2):
		""" Pesquisa aresta (verifica ligacao) """
		pass

	def removeA(self, v1, v2):
		""" Remove aresta """
		pass

	def printV(self, v):
		""" Exibir Vertices """
		pass

	def printG(self, grafo):
		""" imprime o grafo """
		st = ""
		for i in grafo:
			st += i+" -> "
			for j in i:
				st += j+" "
		print(st)