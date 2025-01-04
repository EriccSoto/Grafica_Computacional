#!/usr/bin/env python

from manim import *

class Shapes(Scene):
    def construct(self):
        
        cuadrado = Square(side_length=2, color=BLUE)
        cuadrado2 = Square(side_length=2, color=GREEN)
        cuadrado3 = Square(side_length=2, color=RED)
        cuadrado4 = Square(side_length=2, color=PINK)
        cuadrado5 = Square(side_length=2, color=YELLOW)

        cuadrado.move_to(np.array([-4, 2, 0]))
        cuadrado2.to_edge(UP)
        cuadrado3.to_edge(RIGHT)
        cuadrado4.to_edge(DOWN)
        cuadrado5.to_edge(LEFT)

        self.play(Create(cuadrado), Create(cuadrado2),
                  Create(cuadrado3), Create(cuadrado4),
                  Create(cuadrado5))

        self.wait(2)

        self.play(FadeOut(cuadrado), FadeOut(cuadrado2),
                  FadeOut(cuadrado3), FadeOut(cuadrado4),
                  FadeOut(cuadrado5))

        self.wait()
