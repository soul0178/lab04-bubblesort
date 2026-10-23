import unittest
from src.ordenador import Ordenador


class TestBubbleSort(unittest.TestCase):
    """Suite de pruebas de caja blanca para bubble_sort.
    Un caso de prueba por cada camino independiente, V(G) = 4."""

    def setUp(self):
        # Inicializa el SUT antes de cada prueba
        self.ordenador = Ordenador()

    def tearDown(self):
        # Libera recursos después de cada prueba
        self.ordenador = None

    def test_cp1_camino_1_2_9_un_solo_elemento(self):
        """CP1 - C1: 1-2-9. El for externo no se ejecuta."""
        # Arrange
        vet = [5]
        esperado = [5]
        # Act
        resultado = self.ordenador.bubble_sort(vet)
        # Assert
        self.assertEqual(esperado, resultado)

    def test_cp2_camino_una_pasada_con_intercambio(self):
        """CP2 - C2: 1-2-3-4-5-6-7-4-8-2-9."""
        vet = [2, 1]
        esperado = [1, 2]
        resultado = self.ordenador.bubble_sort(vet)
        self.assertEqual(esperado, resultado)

    def test_cp3_camino_una_pasada_sin_intercambio(self):
        """CP3 - C3: 1-2-3-4-5-7-4-8-2-9."""
        vet = [1, 2]
        esperado = [1, 2]
        resultado = self.ordenador.bubble_sort(vet)
        self.assertEqual(esperado, resultado)

    def test_cp4_camino_dos_pasadas_con_y_sin_intercambio(self):
        """CP4 - C4: 1-2-3-4-5-6-7-4-5-6-7-4-8-2-3-4-5-7-4-8-2-9."""
        vet = [3, 1, 2]
        esperado = [1, 2, 3]
        resultado = self.ordenador.bubble_sort(vet)
        self.assertEqual(esperado, resultado)


if __name__ == "__main__":
    unittest.main()
