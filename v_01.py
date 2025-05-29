from manim import *

class prueba(Scene):
    def construct(self):
        t = Text('Hola a todos otra vez')
        t1 = Text('Esta es una nueva prueba')
        t2 = Text('Seguiremos creando nuevas presentaciones')
        self.add(t)
        self.wait(3)
        self.add(t1)
        self.wait(3)
        self.add(t2)
        self.wait(3)
