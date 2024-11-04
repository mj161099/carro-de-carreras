from llantas import Llantas
from eje import Eje

class Kart:
    def __init__(self, jugador, velocidad_maxima, aceleracion, llantas, numero_ejes, kilometraje, peso_inicial, nivel_gasolina_inicial, **kwargs):
        self.jugador = jugador
        self.velocidad_maxima = velocidad_maxima
        self.aceleracion = aceleracion
        self.llantas = Llantas(llantas)
        self.numero_ejes = numero_ejes
        self.eje = Eje(numero_ejes)
        self.numero_llantas = self.eje.numero_llantas
        self.traccion = self.llantas.TRACCIONES[llantas]
        self.kilometraje = kilometraje
        self.nivel_gasolina_inicial = nivel_gasolina_inicial
        self.peso_inicial = peso_inicial
        self.peso_extra = self.llantas.PESO_EXTRA[llantas]
        self.gasolina_extra = self.llantas.GASOLINA_EXTRA[llantas]

        for llave, valor in kwargs.items():
            setattr(self, llave, valor)

    @property
    def peso_actual(self):
        return self.peso_inicial + self.peso_inicial * self.peso_extra

    @property
    def gasolina_actual(self):
        return self.nivel_gasolina_inicial - self.nivel_gasolina_inicial * self.gasolina_extra

    def __str__(self):
        detalles = f"\nEl kart tiene como valor inicial los siguientes atributos: \n\n- Jugador: {self.jugador}\n- Velocidad máxima: {self.velocidad_maxima} km/h\n- Aceleración: {self.aceleracion} km/h²\n- Llantas: {self.llantas}\n- Numero de ejes: {self.numero_ejes}\n- Kilometraje: {self.kilometraje}\n- Nivel de gasolina: {self.nivel_gasolina_inicial}\n- Peso: {self.peso_inicial}\n- Habilidad especial: {self.usar_habilidad_especial()}\n"

        detalles += "\n- Características e incidencias en sus llantas -\n"

        detalles += f"* Cantidad de llantas del kart de carreras es: {self.numero_llantas}\n"

        detalles += f"* La tracción del kart según sus llantas {self.llantas} es: {self.traccion}\n"

        detalles += f"* Peso inicial: {self.peso_inicial}\n"
        detalles += f"* Peso actual: {self.peso_actual}\n"

        detalles += f"* Nivel de gasolina inicial: {self.nivel_gasolina_inicial}\n"
        detalles += f"* Nivel de gasolina actual: {self.gasolina_actual}\n"
        return detalles

    def medidor_gasolina(self):
        if self.nivel_gasolina_inicial <= 2:
            return "Alerta! El nivel de gasolina está por debajo del rango."
        else:
            return"Nivel de gasolina normal." 

    def usar_habilidad_especial(self):
        pass

    def ascii_ganador(self):
        pass

    @staticmethod
    def calcular_duracion_gasolina(nivel_gasolina_actual, consumo_por_km):
        if consumo_por_km == 0:
            return "\nEl consumo por kilómetro debe ser mayor que cero."
        duracion = nivel_gasolina_actual / consumo_por_km
        return f"\nDuración estimada de la gasolina: {duracion} km"
