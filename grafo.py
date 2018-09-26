

class grafo(object):
	"""docstring for grafo"""
	
	TAM = 20
	def __init__(self):
		pass

	def create(self):
		self.v = [0] * self.TAM
		for i in range(self.TAM):
			self.v[i] = [0] * self.TAM
		return self.v


	def insertA(self, g, v1, v2):
		""" Insere arestas no grafo """
		g[v1][v2] += 1
		g[v2][v1] += 1

	def searchA(self, g, v1, v2):
		""" Pesquisa aresta (verifica ligacao) """
		if (g[v1][v2] > 0):
			return True

	def removeA(self, g, v1, v2):
		""" Remove aresta """
		g[v1][v2] = 0
		g[v2][v1] = 0

	def printV(self, g, v):
		""" Exibir Vertices """
		print(g[v])

	def printG(self, grafo):
		""" imprime o grafo """
		print(grafo)