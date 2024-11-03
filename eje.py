class Eje:
    def __init__(self, numero_ejes):
        self.numero_ejes = numero_ejes
        self.numero_llantas = self.definir_numero_llantas()

    def definir_numero_llantas(self):
        if self.numero_ejes == 1:
            return 4
        elif self.numero_ejes == 2:
            return 8
        elif self.numero_ejes == 3:
            return 12
        else:
            return 0
