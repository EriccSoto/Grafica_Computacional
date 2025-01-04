from manim import * 
import numpy as np

class PruebaVectores3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add(axes)

        theta = PI / 4
        u = np.array([np.cos(theta), np.sin(theta), -1])
        v = np.array([np.sin(theta), -np.cos(theta), 0])

        u1, u2 = u[:2]
        v1, v2 = v[:2]

        formula_u = MathTex(r"\vec{u} = \langle \cos(\theta), \sin(\theta), -1 \rangle").scale(0.5).to_corner(UL)
        formula_v = MathTex(r"\vec{v} = \langle \sin(\theta), -\cos(\theta), 0 \rangle").scale(0.5).next_to(formula_u, DOWN, buff=0.4)
        valor_theta = MathTex(r"\theta = \frac{\pi}{4}").scale(0.5).next_to(formula_v, DOWN, buff=0.4)

        self.add_fixed_in_frame_mobjects(formula_u, formula_v, valor_theta)

        vector_u = Arrow3D(start=[0, 0, 0], end=u, color=BLUE)
        vector_v = Arrow3D(start=[0, 0, 0], end=v, color=RED)
        self.play(Create(vector_u), Create(vector_v))
        
        label_u = MathTex(r"\vec{u}").next_to(vector_u.get_end(), UP)
        label_v = MathTex(r"\vec{v}").next_to(vector_v.get_end(), UP)
        self.play(Write(label_u), Write(label_v))

        valores_componentes = MathTex(
            rf"u_1 = {u1:.2f}, u_2 = {u2:.2f}", rf"v_1 = {v1:.2f}, v_2 = {v2:.2f}"
        ).scale(0.5).to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(valores_componentes)

        producto_punto = np.dot(u, v)
        desarrollo_producto_punto = MathTex(
            r"\vec{u} \cdot \vec{v} = "
            r"\cos(\theta)\sin(\theta) + \sin(\theta)(-\cos(\theta)) + (-1)(0)"
        ).scale(0.5).to_corner( corner=LEFT, buff=0.5)

        resultado_producto_punto = MathTex(
            rf"\vec{u} \cdot \vec{v} = {producto_punto:.2f}"
        ).scale(0.5).next_to(desarrollo_producto_punto, DOWN, buff=0.4)

        texto_condicion = (
            MathTex(r"\text{Ortogonal: } \vec{u} \cdot \vec{v} = 0").scale(0.5)
            if np.isclose(producto_punto, 0)
            else MathTex(r"\text{No Ortogonal: } \vec{u} \cdot \vec{v} = " + f"{producto_punto:.2f}").scale(0.5)
        ).next_to(resultado_producto_punto, DOWN, buff=0.4)

        self.add_fixed_in_frame_mobjects(desarrollo_producto_punto, resultado_producto_punto, texto_condicion)

        self.wait()
