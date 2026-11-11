import unittest
from py.calculadora import sumar


class TestCalculadora(unittest.TestCase):
	def test_suma(self):
		self.assertEqual(sumar(2, 3), 5)

	def test_numeros_negativos(self):
		self.assertEqual(sumar(-2, -3), -5)


if __name__ == "__main__":
   unittest.main()
