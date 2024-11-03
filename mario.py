from kart import Kart
from eje import Eje
from llantas import Llantas

class Mario(Kart, Eje):

    def __init__(self):
        super().__init__("Mario", 200, 10, "Pirelli", 1, 1000, 1, 50)

    def usar_habilidad_especial(self):
        super().usar_habilidad_especial()
        return (f"{self.jugador} activa Super Estrella! Invencibilidad temporal.")

    def ascii_ganador (self):
        super().ascii_ganador()
        print ("""
▒▒▒▒▒▒▒▒▒▄▄▄▄▒▒▒▒▒▒▒
▒▒▒▒▒▒▄▀▀▓▓▓▀█▒▒▒▒▒▒
▒▒▒▒▄▀▓▓▄██████▄▒▒▒▒
▒▒▒▄█▄█▀░░▄░▄░█▀▒▒▒▒
▒▒▄▀░██▄░░▀░▀░▀▄▒▒▒▒
▒▒▀▄░░▀░▄█▄▄░░▄█▄▒▒▒
▒▒▒▒▀█▄▄░░▀▀▀█▀▒▒▒▒▒
▒▒▒▄▀▓▓▓▀██▀▀█▄▀▀▄▒▒
▒▒█▓▓▄▀▀▀▄█▄▓▓▀█░█▒▒
▒▒▀▄█░░░░░█▀▀▄▄▀█▒▒▒
▒▒▒▄▀▀▄▄▄██▄▄█▀▓▓█▒▒
▒▒█▀▓█████████▓▓▓█▒▒
▒▒█▓▓██▀▀▀▒▒▒▀▄▄█▀▒▒
▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ \n""")