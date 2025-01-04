#!/usr/bin/env python

from manim import *


class WarpSquare(Scene):
    def construct(self):
        # Crear el cuadrado
        square = Square()
        
        # Aplicar transformación punto a punto
        self.play(square.animate.apply_function(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point)))
        ))
        self.wait()
