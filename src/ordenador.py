class Ordenador:
    """Clase que implementa algoritmos de ordenamiento."""

    def bubble_sort(self, vet):
        n = len(vet)
        for i in range(n, 1, -1):          # i = n ... 2
            for j in range(0, i - 1):      # j = 0 ... i-2
                if vet[j] > vet[j + 1]:
                    aux = vet[j]
                    vet[j] = vet[j + 1]
                    vet[j + 1] = aux
        return vet
