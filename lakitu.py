from kart import Kart
from eje import Eje

class Lakitu:

    def __init__(self, peso_carga):
    	self.peso_carga = peso_carga

    def remolcar_carro(self, carro):
        if self.peso_carga > carro.peso_actual:
            print(f"Lakitu está remolcando al perdedor {carro.jugador}.")
            print("""
    █████▀█████████████████████
    █─▄▄▄▄██▀▄─██▄─▀█▀─▄█▄─▄▄─█
    █─██▄─██─▀─███─█▄█─███─▄█▀█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀
    ████████████████████████
    █─▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█
    █─██─██▄▀▄███─▄█▀██─▄─▄█
    ▀▄▄▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀
""")
        else:
            print("El peso del carro de carreras es demasiado para Lakitu.")