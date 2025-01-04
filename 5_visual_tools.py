from manim import *

def move_braces(scene):
    scene.camera.background_color = "#406715"  # Fondo oscuro gris
    text = MathTex(
        r"\frac{d}{dx}f(x)g(x)=",  # 0
        r"f(x)\frac{d}{dx}g(x)",   # 1
        r"+",                      # 2
        r"g(x)\frac{d}{dx}f(x)"    # 3
    )
    scene.play(Write(text))
    brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
    brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
    t1 = brace1.get_text(r"$g'f$")
    t2 = brace2.get_text(r"$f'g$")
    scene.play(GrowFromCenter(brace1), FadeIn(t1))
    scene.wait()
    scene.play(ReplacementTransform(brace1, brace2), ReplacementTransform(t1, t2))
    scene.wait()
    scene.play(FadeOut(text), FadeOut(brace2), FadeOut(t2))


def move_braces_copy(scene):
    scene.camera.background_color = "#783b3b"  # Fondo oscuro gris más claro
    text = MathTex(
        r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", r"+",
        r"g(x)\frac{d}{dx}f(x)"
    )
    scene.play(Write(text))
    brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
    brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
    t1 = brace1.get_text(r"$g'f$")
    t2 = brace2.get_text(r"$f'g$")
    scene.play(GrowFromCenter(brace1), FadeIn(t1))
    scene.wait()
    scene.play(ReplacementTransform(brace1.copy(), brace2), ReplacementTransform(t1.copy(), t2))
    scene.wait()
    scene.play(FadeOut(text), FadeOut(brace1), FadeOut(brace2), FadeOut(t1), FadeOut(t2))


def move_frame_box(scene):
    scene.camera.background_color = "#152667"  # Fondo oscuro gris más claro
    text = MathTex(
        r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", r"+",
        r"g(x)\frac{d}{dx}f(x)"
    )
    scene.play(Write(text))
    framebox1 = SurroundingRectangle(text[1], buff=0.1)
    framebox2 = SurroundingRectangle(text[3], buff=0.1)
    scene.play(Create(framebox1))
    scene.wait()
    scene.play(ReplacementTransform(framebox1, framebox2))
    scene.wait()
    scene.play(FadeOut(text), FadeOut(framebox1), FadeOut(framebox2))


def move_frame_box_copy(scene):
    scene.camera.background_color = "#34495e"  # Fondo gris más oscuro
    text = MathTex(
        r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", r"+",
        r"g(x)\frac{d}{dx}f(x)"
    )
    scene.play(Write(text))
    framebox1 = SurroundingRectangle(text[1], buff=0.1)
    framebox2 = SurroundingRectangle(text[3], buff=0.1)
    scene.play(Create(framebox1))
    scene.wait()
    scene.play(ReplacementTransform(framebox1.copy(), framebox2, path_arc=-PI))
    scene.wait()
    scene.play(FadeOut(text), FadeOut(framebox1), FadeOut(framebox2))


def arrow1(scene):
    scene.camera.background_color = "#581567"  # Fondo gris aún más oscuro
    step1 = Text("Step 1")
    step2 = Text("Step 2")
    arrow = Arrow(LEFT, RIGHT)
    step1.move_to(LEFT * 2)
    arrow.next_to(step1, RIGHT, buff=0.1)
    step2.next_to(arrow, RIGHT, buff=0.1)
    scene.play(Write(step1))
    scene.wait()
    scene.play(GrowArrow(arrow))
    scene.play(Write(step2))
    scene.wait()
    scene.play(FadeOut(step1), FadeOut(step2), FadeOut(arrow))


def arrow2(scene):
    scene.camera.background_color = "#676315"  # Fondo gris aún más oscuro
    step1 = Text("Step 1")
    step2 = Text("Step 2")
    step1.move_to(LEFT * 2 + DOWN * 2)
    step2.move_to(4 * RIGHT + 2 * UP)
    arrow1 = Arrow(step1.get_right(), step2.get_left(), buff=0.1, color=RED)
    arrow2 = Arrow(step1.get_top(), step2.get_bottom(), buff=0.1, color=BLUE)
    scene.play(Write(step1), Write(step2))
    scene.play(GrowArrow(arrow1))
    scene.play(GrowArrow(arrow2))
    scene.wait()
    scene.play(FadeOut(step1), FadeOut(step2), FadeOut(arrow1), FadeOut(arrow2))


class Todo(Scene):
    def construct(self):
        self.show_nombre()
        move_braces(self)
        move_braces_copy(self)
        move_frame_box(self)
        move_frame_box_copy(self)
        arrow1(self)
        arrow2(self)
        self.show_nombres()

    def show_nombre(self):
        credit_text = Text("Hecho por Eric Carmen Soto")
        credit_text.to_edge(UP)
        self.play(Write(credit_text))
        self.wait(2)
        self.play(FadeOut(credit_text))
        
        
    def show_nombres(self):
        self.camera.background_color = "#406714"  
        credit_text = Text(
            "Universidad Autónoma del Estado de México\n"
            "Centro Universitario UAEM Zumpango\n"
            "Ingeniería en Computación\n"
            "GRAFICACIÓN COMPUTACIONAL\n\n"
            "Alumno: Eric Carmen Soto\n"
            "Segundo Periodo\n\n"
        ).scale(0.5)

        credit_text.to_edge(ORIGIN)

        self.play(Write(credit_text))
        self.wait(5)
        self.play(FadeOut(credit_text))

    

    






	
        
        
