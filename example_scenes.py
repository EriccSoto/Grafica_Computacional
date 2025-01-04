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

class SquareToCircle(Scene):
    def construct(self):
        # Crear los objetos
        circle = Circle()
        square = Square()
        
        # Transformaciones del cuadrado
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        
        # Establecer el relleno del círculo
        circle.set_fill(PINK, opacity=0.5)

        # Mostrar el cuadrado y luego transformarlo en círculo
        self.play(Create(square))  # ShowCreation -> Create en Manim Community
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class WarpSquare(Scene):
    def construct(self):
        # Crear el cuadrado
        square = Square()
        
        # Aplicar transformación punto a punto
        self.play(square.animate.apply_function(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point)))
        ))
        self.wait()

class WriteStuff(Scene):
    def construct(self):
        # Texto de ejemplo con colores
        example_text = Tex(
            "This is some text",
            tex_to_color_map={"text": YELLOW}
        )
        
        # Fórmula matemática
        example_tex = MathTex(
            r"\sum_{k=1}^\infty {1 \over k^2} = {\pi^2 \over 6}",
        )
        
        # Agrupar ambos elementos
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(config.frame_width - 2 * LARGE_BUFF)  # Usar config.frame_width

        # Animaciones
        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()

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


