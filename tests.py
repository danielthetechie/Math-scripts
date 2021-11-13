from matrices import *
import unittest

####### Unit tests ########
class TestMatrices (unittest.TestCase):

	def test1_esMatrizCuadrada (self):
		m = [[0, 1, 2], [2, 3]]
		self.assertEqual (esMatrizCuadrada (m), False, "Tiene que dar False")

	def test2_esMatrizCuadrada (self):
		m1 = [[2, 3], [4, 5]]
		self.assertEqual (esMatrizCuadrada (m1), True, "Tiene que dar True")

	def test3_det2x2 (self):
		m1 = [[2, 3], [4, 5]]
		self.assertEqual (det2x2 (m1), -2, "Tiene que dar -2")

	def test4_det2x2 (self):
		m2 = [[1, 0], [0, 1]]
		self.assertEqual (det2x2 (m2), 1, "Tiene que dar 1")

	def test5_detMatriz (self):
		m3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
		self.assertEqual (detMatriz (m3), 0, "Tiene que dar 0")

	def test6_detMatriz (self):
		m4 = [[2, -3, 1], [2, 0, -1], [1, 4, 5]]
		self.assertEqual (detMatriz (m4), 49, "Tiene que dar 49")

	def test7_detMatriz (self):
		m5 = [[2, 3, 3, 1], [1, 5, 4, 3], [4, 6, 8, 5], [-2, -3, -3, 4]]
		self.assertEqual (detMatriz (m5), 70, "Tiene que dar 70")

	def test8_detMatriz (self):
		m6 = [[4, 3, -1, 4, 2, 3], [0, 8, -7, -5, 3, 2], [4, 3, -6, 8, 5, 1], [7, -4, 0, 3, -9, 5], [2, -1, 8, 6, -7, 0], [3, 8, 11, 4, -2, 1]]
		self.assertEqual (detMatriz (m6), 59818, "Tiene que dar 59818")

	def test9_matrizAdjuntaElementoIJ (self):
		m7 = [[1, 2, 3], [3, 2, 1], [1, 0, 1]]
		self.assertEqual (matrizAdjuntaElementoIJ (2, 2, m7), [[1, 2], [3, 2]], "Tiene que dar [[1, 2], [3, 2]]")

	def test10_matrizAdjuntaElementoIJ (self):
		m7 = [[1, 2, 3], [3, 2, 1], [1, 0, 1]]
		self.assertEqual (matrizAdjuntaElementoIJ (1, 1, m7), [[1, 3], [1, 1]], "Tiene que dar [[1, 3], [1, 1]]")

	def test11_matrizAdjuntaElementoIJ (self):
		m7 = [[1, 2, 3], [3, 2, 1], [1, 0, 1]]
		self.assertEqual (matrizAdjuntaElementoIJ (1, 0, m7), [[2, 3], [0, 1]], "Tiene que dar [[1, 3], [1, 1]]")
	
	def test12_matrizAdjuntaTraspuesta (self):
		m7 = [[1, 2, 3], [3, 2, 1], [1, 0, 1]]
		self.assertEqual (matrizAdjuntaTraspuesta (m7), [[2, -2, -4], [-2, -2, 8], [-2, 2, -4]], "Tiene que dar [[2, -2, -2], [-2, -2, 2], [-4, 8, -4]]")

	def test13_matrizInversa (self):
		m7 = [[1, 2, 3], [3, 2, 1], [1, 0, 1]]
		self.assertEqual (matrizInversa (m7), [[-0.25, 0.25, 0.5], [0.25, 0.25, -1.0], [0.25, -0.25, 0.5]], "Tiene que dar [[-0.25, 0.25, 0.5], [0.25, 0.25, -1.0], [0.25, -0.25, 0.5]]")

	def test14_matrizInversa (self):
		m1 = [[2, 3], [4, 5]]
		self.assertEqual (matrizInversa (m1), [[-2.5, 1.5], [2.0, -1.0]], "Tiene que dar [[-2.5, 1.5], [2, 1]]")

if __name__ == '__main__':
    unittest.main()