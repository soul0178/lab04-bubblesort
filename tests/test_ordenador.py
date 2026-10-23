import unittest
from src.ordenador import Ordenador


class TestBubbleSort(unittest.TestCase):
    """Suite de pruebas de caja blanca para bubble_sort."""

    def setUp(self):
        # Inicializa el SUT antes de cada prueba
        self.ordenador = Ordenador()

    def tearDown(self):
        # Libera recursos después de cada prueba
        self.ordenador = None

    def test_cp1_lista_con_un_elemento(self):
        # Arrange
        entrada = [7]
        esperado = [7]
        # Act
        resultado = self.ordenador.bubble_sort(entrada)
        # Assert
        self.assertEqual(esperado, resultado)

    def test_cp2_lista_ya_ordenada(self):
        entrada = [1, 2]
        esperado = [1, 2]
        resultado = self.ordenador.bubble_sort(entrada)
        self.assertEqual(esperado, resultado)

    def test_cp3_dos_elementos_desordenados(self):
        entrada = [2, 1]
        esperado = [1, 2]
        resultado = self.ordenador.bubble_sort(entrada)
        self.assertEqual(esperado, resultado)

    def test_cp4_lista_mixta_varios_elementos(self):
        entrada = [5, 1, 4, 2, 8]
        esperado = [1, 2, 4, 5, 8]
        resultado = self.ordenador.bubble_sort(entrada)
        self.assertEqual(esperado, resultado)


if __name__ == "__main__":
    unittest.main()
