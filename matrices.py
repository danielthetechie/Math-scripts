"""Crea una función que, dada una matriz cuadrada A, compruebe si es invertible o no; y en caso afirmativo, calcule la inversa de A mediante el método de los adjuntos."""

def esMatrizCuadrada (mat):
	filas = len (mat)
	for fila in range (len (mat)):
		columnas = len (mat[fila])
		if (filas != columnas):
			return False
	return True

def det2x2 (mat):
	if (not esMatrizCuadrada (mat) or len (mat) != 2):
		return "Error: la matriz no es 2x2."

	return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

def detMatriz (mat):
	n = len (mat)
	if n == 1:
		return mat[0][0]

	if (not esMatrizCuadrada (mat)):
		return "Error: la matriz no es cuadrada."

	resultado = 0

	if n == 2:
		resultado += det2x2 (mat)

	else:
		# Sea mat una matriz n x n, entonces all_mat_sub contendrá las submatrices (n - 1) x (n - 1).
		all_mat_sub = []

		mat_sub = []
		row_sub = []

		for i in range (n):
			for j in range (1, n):
				row_sub = mat[j][:i] + mat[j][i + 1:]
				mat_sub.append (row_sub)
			all_mat_sub.append (mat_sub)
			resultado += (((-1)**(i + 2)) * mat[0][i] * detMatriz (mat_sub))
			mat_sub = []

	return resultado

# Dada una matriz A, devuelve la matriz que se obtiene de eliminar la fila i la columna j de A.
def matrizAdjuntaElementoIJ (i, j, mat):
	
	if (not esMatrizCuadrada (mat)):
		return "Error: la matriz no es cuadrada."

	n = len (mat)
	mat_sub = []
	row_sub = []

	for x in range (n):
		if x == i:
			continue
		row_sub = mat[x][:j] + mat[x][j + 1:]
		mat_sub.append (row_sub)

	return mat_sub

def matrizAdjuntaTraspuesta (mat):

	if (not esMatrizCuadrada (mat)):
		return "Error: la matriz no es cuadrada."

	n = len (mat)

	mat_adj = []
	mat_sub = []

	for j in range (n):
		for i in range (n):
			mat_adj_ij = matrizAdjuntaElementoIJ (i, j, mat)
			adj = ((-1)**(i + j + 2)) * detMatriz (mat_adj_ij)
			mat_sub.append (adj)
		mat_adj.append (mat_sub)
		mat_sub = []

	return mat_adj

def matrizInversa (mat):

	if (not esMatrizCuadrada (mat)):
		return "Error: la matriz no es cuadrada."

	det_matriz = detMatriz (mat)

	if (det_matriz == 0):
		return "Esta matriz no tiene inversa."

	n = len (mat)
	mat_original = mat
	mat = matrizAdjuntaTraspuesta (mat_original)

	for i in range (n):
		for j in range (n):
			mat[i][j] = mat[i][j] / det_matriz

	return mat

####################################
########### ¡A jugar! ##############
####################################

m6 = [	
		[4, 3, -1, 4, 2, 3],
		[0, 8, -7, -5, 3, 2],  
		[4, 3, -6, 8, 5, 1], 
		[7, -4, 0, 3, -9, 5],
		[2, -1, 8, 6, -7, 0],
		[3, 8, 11, 4, -2, 1]
	]
print (matrizInversa (m6))


m7 = [
		[1, 2, 3], 
		[3, 2, 1], 
		[1, 0, 1]
	]
print ("\n----\n")
print (matrizInversa (m7))

m1 = [
		[2, 3], 
		[4, 5]
	]
print ("\n----\n")
print (matrizInversa (m1))


