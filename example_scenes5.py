#!/usr/bin/env python

from manim import *

class UpdatersExample(Scene):
    def construct(self):
        # Número decimal que cambia
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        
        # Crear el cuadrado
        square = Square().to_edge(UP)

        # Añadir actualizadores
        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))

        # Añadir el cuadrado y el decimal a la escena
        self.add(square, decimal)
        
        # Animación del cuadrado
        self.play(
            square.animate.to_edge(DOWN),  # Usamos animate
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()


