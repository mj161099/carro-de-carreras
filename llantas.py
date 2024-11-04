from excepciones import ImproperTireException

class Llantas:
    MICHELIN = "Michelin"
    PIRELLI = "Pirelli"
    GOODYEAR = "Goodyear"
    BRIDGESTONE = "Bridgestone"

    TRACCIONES = {
        MICHELIN: "Buena",
        PIRELLI: "Excelente",
        GOODYEAR: "Regular",
        BRIDGESTONE: "Regular"
    }

    PESO_EXTRA = {
        MICHELIN: 0.10,
        PIRELLI: 0.05,
        GOODYEAR: 0.00,
        BRIDGESTONE: 0.00
    }

    GASOLINA_EXTRA = {
        MICHELIN: 0.00,
        PIRELLI: 0.00,
        GOODYEAR: 0.20,
        BRIDGESTONE: 0.30
    }

    def __init__(self, llantas):
        if llantas not in self.TRACCIONES:
            raise ImproperTireException("Tipo de llantas desconocido!")
        self.llantas = llantas
        self.traccion = self.TRACCIONES[llantas]
        self.peso_extra = self.PESO_EXTRA[llantas]
        self.gasolina_extra = self.GASOLINA_EXTRA[llantas]

    def __str__(self):
        return self.llantas
