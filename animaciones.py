
LONGITUD_PISTA = 50


class KartAnimacion:
    def __init__(self):
        self.posicion = 0

    @staticmethod
    def dibujar_inicio_pista():
        print('-' * LONGITUD_PISTA + "MARIO KART GO!!" + "-" * LONGITUD_PISTA)

    def dibujar_kart(self, desfase, nombre):
        self.posicion += desfase
        print(' ' * self.posicion + nombre)
        print(' ' * self.posicion + '   ______')
        print(' ' * self.posicion + '  /|_||_\\`.__')
        print(' ' * self.posicion + ' (   _    _ _\\')
        print(' ' * self.posicion + ' =`-(_)--(_)-\'')
        print(' ' * self.posicion + '------------')

    @staticmethod
    def dibujar_final_pista():
        print('-' * LONGITUD_PISTA)


    def dibujar_lakitu(self):
        print(' ' * self.posicion + "Lakitu ")
        print(' ' * self.posicion + '        .-~~~-.')
        print(' ' * self.posicion + '    .-~~~     ~~~-.')
        print(' ' * self.posicion + ' .-~               ~-.')
        print(' ' * self.posicion + ':                   :')
        print(' ' * self.posicion + '\\  .-~ ~~-.__.-~~-.  /')
        print(' ' * self.posicion + ' \\  `-.__.-~~-.__.-')
        print(' ' * self.posicion + '    `-.__.-~~-.__.-')