#!/usr/bin/env python

from manim import *


class OpeningManimExample(Scene):
    def construct(self):
        # Título usando Tex
        title = Tex("This is some ", r"\LaTeX")
        
        # Fórmula de la serie de Basel
        basel = MathTex(
            r"\sum_{n=1}^\infty "
            r"\frac{1}{n^2} = \frac{\pi^2}{6}"
        )

        # Organizar los elementos verticalmente
        VGroup(title, basel).arrange(DOWN)

        # Animaciones
        self.play(Write(title))  # Escribe el título
        self.play(FadeIn(basel, shift=UP))  # Aparece la fórmula desde arriba
        self.wait()

        # Transformación del título
        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)

        self.play(title.animate.become(transform_title))  # Transforma el título
        self.play(FadeOut(basel, shift=DOWN))  # Desvanece el basel hacia abajo
        self.wait()

        # Añadir el plano de números (grid)
        grid = NumberPlane()
        grid_title = Tex("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Asegura que el título esté sobre el grid
        self.play(FadeOut(title), FadeIn(grid_title, shift=DOWN), Write(grid))  # Animaciones del grid
        self.wait()

        # Transformación no lineal aplicada al grid
        grid_transform_title = Tex(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()

        # Aplicar transformación no lineal al grid
        self.play(
            grid.animate.apply_function(
                lambda p: p + np.array([
                    np.sin(p[1]),
                    np.sin(p[0]),
                    0,
                ])
            ),
            run_time=3,
        )
        self.wait()

        # Transformación del título del grid
        self.play(grid_title.animate.become(grid_transform_title))
        self.wait()
