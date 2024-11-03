from kart import Kart


class Baraja:
    total_karts = 0

    def __init__(self):
        self.cartas = []

    def agregar_carta(self, kart):
        if isinstance(kart, Kart):
            self.cartas.append(kart)
            Baraja.total_karts += 1
            print(f"{kart.jugador}Kart agregado a la baraja.")
        else:
            print("Solo se pueden agregar instancias de la clase Kart.")

    def eliminar_carta(self, kart):
        if kart in self.cartas:
            self.cartas.remove(kart)
            Baraja.total_karts -= 1
            print(f"{kart.jugador}Kart eliminado de la baraja.")
        else:
            print("El kart no está en la baraja.")

    def listar_cartas(self):
        print("Cartas en la baraja:\n")
        for kart in self.cartas:
            print(f"::: {kart.jugador} :::")
            print(kart)
            print(Baraja.contar_total_karts())

    def comparar_cartas(self, atributo):
        if not self.cartas:
            print("La baraja está vacía.")
            return

        mejor_kart = max(self.cartas, key=lambda kart: getattr(kart, atributo, 0))
        print(f"El kart con mejor {atributo} es {mejor_kart.jugador}Kart con {getattr(mejor_kart, atributo)}.")

    @classmethod
    def contar_total_karts(cls):
        return f"Hay un total de {cls.total_karts} karts en todas las barajas."
