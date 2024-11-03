from barajas import Baraja
from kart import Kart
from mario import Mario
from luigi import Luigi
from peach import Peach
from toad import Toad
from llantas import Llantas
from carrera import Carrera

class Menu:

	def __init__(self, nombre, version):
		self.nombre = nombre
		self.version = version
		self.baraja = Baraja()

		print(r""" 

			 _____ ______   ________  ________  ___  ________          ___  __    ________ ________     
|\   _ \  _   \|\   __  \|\   __  \|\  \|\   __  \        |\  \|\  \ |\   __  \|\   __  \ |\___   ___\    
\ \  \\\__\ \  \ \  \|\  \ \  \|\  \ \  \ \  \|\  \       \ \  \/  /|\ \  \|\  \ \  \|\  \\|___ \  \_| 
 \ \  \\|__| \  \ \   __  \ \   _  _\ \  \ \  \\\  \       \ \   ___  \ \   __  \ \   _  _\    \ \  \ 
  \ \  \    \ \  \ \  \ \  \ \  \\  \\ \  \ \  \\\  \       \ \  \\ \  \ \  \ \  \ \  \\  \|    \ \  \
   \ \__\    \ \__\ \__\ \__\ \__\\ _\\ \__\ \_______\       \ \__\\ \__\ \__\ \__\ \__\\ _\     \ \__\
    \|__|     \|__|\|__|\|__|\|__|\|__|\|__|\|_______|        \|__| \|__|\|__|\|__|\|__|\|__|     \|__| 


    					-   Press Enter to continue	 -
    """)                                                                                    
                                                                                             
		input()
		self.mostrar_menu()

	def mostrar_menu(self):

		print("""

				========================================
				|            MENU DE JUEGO             |
				========================================
				|          1. Iniciar juego            |
				|          2. Salir                    |
				|                                      |
				========================================)
""")
		opciones = int(input("\nEscoge una opcion (1/2): "))
		if opciones == 1:
			self.iniciar()
		elif opciones == 2:
			self.terminar()
		else:
			print("Opción no válida. Por favor, elige 1, 2 o 3.")

	def iniciar(self):
		while True:

			print("""

	        ========================================
                |      MENU INTERACTIVO MARIO KART     |
                ========================================
                |        1. Agregar kart               |
                |        2. Eliminar kart              |
                |        3. Listar karts               |
                |        4. Comparar karts             |
                |        5. Iniciar carrera            |
                |        6. Calcular consumo (gas)     |
                |        7. Salir                      |
                ========================================

                """)

			opciones_jugadores = input("Selecciona una opción: ")

			if opciones_jugadores == "1":
				self.agregar_kart()
			elif opciones_jugadores == "2":
				self.eliminar_kart()
			elif opciones_jugadores == "3":
				self.listar_karts()
			elif opciones_jugadores == "4":
				self.comparar_karts()
			elif opciones_jugadores == "5":
				self.iniciar_carrera()
			elif opciones_jugadores == "6":
				self.calcular_comsumo_gas()
			elif opciones_jugadores == "7":
				print("Saliendo del juego.")
				break

	def terminar(self):
		print(f"El juego {self.nombre} ha terminado, ¡hasta luego!")
		exit()

	def agregar_kart(self):
		print("Selecciona el tipo de kart:")
		print("1. Mario")
		print("2. Luigi")
		print("3. Peach")
		print("4. Toad")
		tipo_kart = int(input("Tipo de kart (1-4): "))
		if tipo_kart == 1:
			nuevo_kart = Mario()
		elif tipo_kart == 2:
			nuevo_kart = Luigi()
		elif tipo_kart == 3:
			nuevo_kart = Peach()
		elif tipo_kart == 4:
			nuevo_kart = Toad()
		else:
			print("Selección inválida. Creando un kart genérico.")
			nuevo_kart = Kart("Genérico", 150, 8, "Pirelli", 2, 1000, 500, 50)
		self.baraja.agregar_carta(nuevo_kart)
		

	def eliminar_kart(self):
		jugador = input("Nombre del jugador del kart a eliminar: ")
		kart_a_eliminar = next((kart for kart in self.baraja.cartas if kart.jugador == jugador), None)
		if kart_a_eliminar:
			self.baraja.eliminar_carta(kart_a_eliminar)
		else:
			print("Kart no encontrado.")
			

	def listar_karts(self):
		self.baraja.listar_cartas()
		

	def comparar_karts(self):
		atributo = input("Atributo para comparar (velocidad/aceleración): ")
		self.baraja.comparar_cartas(atributo)

	def calcular_comsumo_gas(self):
		nivel_gasolina = int(input("\nIntroduzca el nivel de gasolina actual de su kart: "))
		consumo_km = int(input("Introduzca el consumo de su kart por km: "))
		print(Kart.calcular_duracion_gasolina(nivel_gasolina, consumo_km))
		

	def iniciar_carrera(self):
		if len(self.baraja.cartas) < 2:
			print("Necesitas al menos 2 karts para iniciar una carrera.")
		else:
			equipo1 = self.baraja.cartas[0]
			equipo2 = self.baraja.cartas[1]
			carrera = Carrera(equipo1, equipo2)
			carrera.iniciar()