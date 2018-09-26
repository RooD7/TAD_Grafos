
TAM = 20

class grafo(object):
	"""docstring for grafo"""
	
	def __init__(self):
		self.v = []
		for i in range(ord('A'),ord('U')):
			self.v.append(chr(i))

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
			# for j in i:
			# 	st += i+" "
		print(st)