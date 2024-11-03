from kart import Kart
from eje import Eje
from llantas import Llantas

class Peach(Kart, Eje):

    def __init__(self):
        super().__init__("Peach", 190, 9, "Michelin", 1, 1050, 1, 45)

    def usar_habilidad_especial(self):
        super().usar_habilidad_especial()
        return (f"{self.jugador} activa Corazón! Protección temporal contra ataques.")

    def ascii_ganador (self):
        super().ascii_ganador()
        print(r""".....
         WWWWW
        ((. .))    
       ))) - (((      
     ((((`...')))       
      ))))\  /(((             
      /    \/    \
     / /\      /\ \
    / /  \    /  \ \
   @@@@  / \/ \  @@@@
   (v   /      \   v)  
       @@@@@@@@@@s
      /          \
     /            \
    @@@@@@@@@@@@@@@@
   /                \
  /                  \
 @@@@@@@@@@@@@@@@@@@@@@
 /                    \
@@@@@@@@@@@@@@@@@@@@@@@@  
         v  v\n""")
