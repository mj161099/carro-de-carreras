from excepciones import ImproperTireException

class Llantas:
    def __init__(self, llantas):
        self.llantas = llantas
        self.traccion = self.definir_traccion()
        self.peso_extra = self.definir_peso_extra()
        self.gasolina_extra = self.definir_gasolina_extra()

    def definir_traccion(self):
        if self.llantas == "Michelin":
            return "Buena"
        elif self.llantas == "Pirelli":
            return "Excelente"
        elif self.llantas == "Goodyear":
            return "Regular"
        elif self.llantas == "Bridgestone":
            return "Regular"
        else:
            raise ImproperTireException("Tipo de llantas desconocido!")

    def __str__(self):
        return self.llantas

    def definir_peso_extra(self):
        #Aumenta peso 10%
        if self.llantas == "Michelin":
            return 0.10
        #Aumenta peso 5%
        elif self.llantas == "Pirelli":
            return 0.05
        else:
            return 0

    def definir_gasolina_extra(self):
        #Consume gasolina 20%
        if self.llantas == "Goodyear":
            return 0.20
        #Consume gasolina 30%
        elif self.llantas == "Bridgestone":
            return 0.30
        else:
            return 0