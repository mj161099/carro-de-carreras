from animaciones import KartAnimacion
from lakitu import Lakitu
from kart import Kart
from barajas import Baraja

import os
import time
import random


class Carrera:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.KartAnimacion_1 = KartAnimacion()
        self.KartAnimacion_2 = KartAnimacion()
        self.lakitu = Lakitu(2)

    def limpiar_consola(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def comparar_atributos(self):
        if not isinstance(self.equipo1, Kart) or not isinstance(self.equipo2, Kart):
            raise TypeError("Los equipos deben ser instancias de la clase KartCarreras")

        puntos_kart1 = self.equipo1.velocidad_maxima + self.equipo1.aceleracion - self.equipo1.peso_inicial
        puntos_kart2 = self.equipo2.velocidad_maxima + self.equipo2.aceleracion - self.equipo2.peso_inicial

        print(f"Puntos de {self.equipo1.jugador}: {puntos_kart1}")
        print(f"Puntos de {self.equipo2.jugador}: {puntos_kart2}")

        if puntos_kart1 > puntos_kart2:
            return self.equipo1, self.equipo2
        elif puntos_kart2 > puntos_kart1:
            return self.equipo2, self.equipo1
        else:
            return None, None

    def iniciar(self):
        time.sleep(5)
        mensaje_inicial = f'{self.equipo1.jugador} VS {self.equipo2.jugador}\n'

        posicion_kart1 = 0
        posicion_kart2 = 0

        carrera_terminada = False

        while True:
            self.limpiar_consola()
            self.KartAnimacion_1.dibujar_lakitu()
            self.KartAnimacion_1.dibujar_inicio_pista()
            self.KartAnimacion_1.dibujar_kart(0, f'{self.equipo1.jugador}')
            self.KartAnimacion_1.dibujar_inicio_pista()
            self.KartAnimacion_2.dibujar_kart(0, f'{self.equipo2.jugador}')
            self.KartAnimacion_1.dibujar_inicio_pista()

            if not carrera_terminada:
                # Incrementar las posiciones basadas en los atributos
                puntos_kart1 = self.equipo1.velocidad_maxima + self.equipo1.aceleracion - self.equipo1.peso_inicial
                puntos_kart2 = self.equipo2.velocidad_maxima + self.equipo2.aceleracion - self.equipo2.peso_inicial

                if puntos_kart1 > puntos_kart2:
                    posicion_kart1 += 2
                    posicion_kart2 += 1
                elif puntos_kart2 > puntos_kart1:
                    posicion_kart1 += 1
                    posicion_kart2 += 2
                else:
                    posicion_kart1 += 1
                    posicion_kart2 += 1

                self.KartAnimacion_1.posicion = posicion_kart1
                self.KartAnimacion_2.posicion = posicion_kart2

                if posicion_kart1 >= 100 or posicion_kart2 >= 100:
                    carrera_terminada = True
                    if posicion_kart1 >= 100:
                        print(f'¡¡¡{self.equipo1.jugador} GANA!!!')
                        self.equipo1.ascii_ganador()
                        self.lakitu.remolcar_carro(self.equipo2)
                    else:
                        print(f'¡¡¡{self.equipo2.jugador} GANA!!!')
                        self.equipo2.ascii_ganador()
                        self.lakitu.remolcar_carro(self.equipo1)
                    time.sleep(2)
                    break

            time.sleep(0.1)