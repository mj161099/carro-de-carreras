from kart import Kart
from eje import Eje
from llantas import Llantas

class Toad(Kart, Eje):

    def __init__(self):
        super().__init__("Toad", 220, 12, "Bridgestone", 1, 900, 1, 60)

    def usar_habilidad_especial(self):
        super().usar_habilidad_especial()
        return (f"{self.jugador} activa Turbo! Velocidad máxima aumentada temporalmente.")
    def ascii_ganador (self):
        super().ascii_ganador()
        print("""                                                                                        
                                        ██████████                                      
                                    ████          ████                                  
                                  ██      ▒▒▒▒▒▒      ██                                
                                ██      ▒▒▒▒▒▒▒▒▒▒      ██                              
                                ██      ▒▒▒▒▒▒▒▒▒▒        ██                            
                              ██▒▒      ▒▒▒▒▒▒▒▒▒▒      ▒▒██                            
                              ██▒▒▒▒      ▒▒▒▒▒▒        ▒▒▒▒██                          
                              ██▒▒▒▒                    ▒▒▒▒██                          
                              ██▒▒      ████████        ▒▒▒▒██                          
                              ██    ██████░░░░██████      ▒▒██                          
                              ██  ██░░░░██░░░░██░░░░██      ██                          
                                ████░░░░██░░░░██░░░░░░██  ██                            
                                  ██░░░░░░░░░░░░░░░░░░██  ██                            
                                  ██░░░░████████░░░░░░████                              
                                    ██░░░░░░░░░░░░░░████                                
                                    ████████████████████                                
                                  ████▓▓██░░░░██▓▓██░░░░██                              
                                ██░░██▓▓██░░░░██▓▓▓▓██░░░░██                            
                              ██░░██▓▓██░░░░░░██▓▓▓▓██░░░░██                            
                              ██░░██▓▓██████████▓▓▓▓▓▓██░░░░██                          
                              ██░░██▓▓██        ██▓▓▓▓██░░░░██                          
                                ██████    ██      ██████████                            
                                    ██      ██        ██                                
                                  ██▓▓▓▓▓▓████▓▓▓▓██████                                
                                ██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██                                
                                ████████████████████████  \n """)