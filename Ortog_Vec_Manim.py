from manim import *

class VectoresEjemplos(Scene):
    def construct(self):
        # Título
        titulo = Text("Ejemplos de Vectores Ortogonales y Paralelos").scale(0.6).to_edge(UP)  # Escala reducida
        self.play(Write(titulo))
        
        # Titulo 2 Vectores Ortogonales
        ejemplo_ortogonal = Text("Ejemplo 1: Vectores Ortogonales", color=BLUE).scale(0.5).next_to(titulo, DOWN)  # Escala reducida
        self.play(Write(ejemplo_ortogonal))
        
        # Plano a escala 0.2
        plano = NumberPlane(
            x_range=[-20, 20], 
            y_range=[-20, 20], 
            background_line_style={"stroke_opacity": 0.4}
        )
        # Reducir la escala y cenntrar plano 
        plano.scale(0.2)
        plano.move_to(ORIGIN)

        
        self.play(Create(plano))

        # Crear los vectores, ahora ajustados a las unidades del plano
        vector_u = Arrow(start=ORIGIN, end=[4 * 0.2, -1 * 0.2, 0], buff=0, color=GREEN, stroke_width=4)
        vector_v = Arrow(start=ORIGIN, end=[2 * 0.2, 8 * 0.2, 0], buff=0, color=RED, stroke_width=4)
        
        # Etiquetas para los vectores
        label_u = MathTex(r"\vec{u} = \langle 4, -1 \rangle").scale(0.6).next_to(vector_u, RIGHT + DOWN)  # Escala reducida
        label_v = MathTex(r"\vec{v} = \langle 2, 8 \rangle").scale(0.6).next_to(vector_v, RIGHT)  # Escala reducida
        
        # Animar la creación de los vectores y sus etiquetas
        self.play(GrowArrow(vector_u), Write(label_u))
        self.play(GrowArrow(vector_v), Write(label_v))
        
        # Fórmula del producto escalar y resultado
        formula_ortogonal = MathTex(r"4 \cdot 2 + (-1) \cdot 8 = 0").scale(0.6).to_edge(DOWN)  # Escala reducida
        resultado_ortogonal = Text("Producto escalar = 0, son ortogonales", color=YELLOW).scale(0.5).next_to(formula_ortogonal, UP)  # Escala reducida

        self.play(Write(formula_ortogonal))
        self.play(Write(resultado_ortogonal))
        
        # Esperar un momento antes de pasar al siguiente ejemplo
        self.wait(2)
        
        # Borrar el primer ejemplo
        self.play(FadeOut(ejemplo_ortogonal), FadeOut(vector_u), FadeOut(vector_v), FadeOut(label_u), FadeOut(label_v), FadeOut(formula_ortogonal), FadeOut(resultado_ortogonal))

        # Ejemplo de Vectores Paralelos
        ejemplo_paralelo = Text("Ejemplo 2: Vectores Paralelos", color=BLUE).scale(0.5).next_to(titulo, DOWN)  # Escala reducida
        self.play(Write(ejemplo_paralelo))
        
        vector_a = Arrow(start=ORIGIN, end=[6 * 0.2, -18 * 0.2, 0], buff=0, color=GREEN, stroke_width=4)
        vector_b = Arrow(start=ORIGIN, end=[-4 * 0.2, 12 * 0.2, 0], buff=0, color=RED, stroke_width=4)
        
        # Etiquetas para los nuevos vectores
        label_a = MathTex(r"\vec{a} = \langle 6, -18 \rangle").scale(0.6).next_to(vector_a, RIGHT)  # Escala reducida
        label_b = MathTex(r"\vec{b} = \langle -4, 12 \rangle").scale(0.6).next_to(vector_b, RIGHT)  # Escala reducida
        
        # Animar la creación de los vectores y sus etiquetas
        self.play(GrowArrow(vector_a), Write(label_a))
        self.play(GrowArrow(vector_b), Write(label_b))
        
        # Fórmula de proporción y resultado
        formula_paralelo = MathTex(r"\frac{6}{-4} = \frac{-18}{12} = -1.5").scale(0.6).to_edge(DOWN).shift(LEFT).shift(LEFT).shift(LEFT)  # Escala reducida
        resultado_paralelo = Text("Razón constante, son paralelos", color=YELLOW).scale(0.5).next_to(formula_paralelo, UP)  # Escala reducida

        self.play(Write(formula_paralelo))
        self.play(Write(resultado_paralelo))
        
        # Finalización de la escena
        self.wait(2)
        self.play(FadeOut(ejemplo_paralelo), FadeOut(vector_a), FadeOut(vector_b), FadeOut(label_a), FadeOut(label_b), FadeOut(formula_paralelo), FadeOut(resultado_paralelo), FadeOut(plano), FadeOut(titulo))
