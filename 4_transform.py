from manim import *

class Todo(Scene):
    
    def construct(self):
        self.show_nombre()
        self.transformation_text1_v1()
        self.transformation_text1_v2()
        self.transformation_text2()
        self.copy_text_v1()
        self.copy_text_v2()
        self.copy_text_v3()
        self.change_text_color_animation()
        self.change_size_animation()
        self.move_text()
        self.change_color_and_size_animation()
        
        self.show_nombres()
    

    def transformation_text1_v1(self):
        self.camera.background_color = PURPLE
        texto1 = Text("First text")
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()
        self.play(FadeOut(texto1))

    def transformation_text1_v2(self):
        self.camera.background_color = BLUE
        texto1 = Text("First text").to_edge(UP)
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()
        self.play(FadeOut(texto1))

    def transformation_text2(self):
        self.camera.background_color = GREEN
        text1 = Text("Function")
        text2 = Text("Derivative")
        text3 = Text("Integral")
        text4 = Text("Transformation")

        self.play(Write(text1))
        self.wait()
        self.play(ReplacementTransform(text1, text2))
        self.wait()
        self.play(ReplacementTransform(text2, text3))
        self.wait()
        self.play(ReplacementTransform(text3, text4))
        self.wait()
        self.play(FadeOut(text4))

    def copy_text_v1(self):
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", 
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        ).scale(2)
        self.camera.background_color = BLUE
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9])
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10])
        )
        self.wait()
        self.play(FadeOut(formula))

    def copy_text_v2(self):
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", 
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        ).scale(2)
        self.camera.background_color = BLACK
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()
        self.play(FadeOut(formula))

    def copy_text_v3(self):
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", 
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        ).scale(2)

        formula[8].set_color(PINK)
        formula[11].set_color(BLUE)

        self.camera.background_color = GREEN

        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()
        self.play(FadeOut(formula))

    def change_text_color_animation(self):
        self.camera.background_color = RED
        text = Text("Text").scale(3)
        self.play(Write(text))
        self.wait()
        self.play(text.animate.set_color(YELLOW), run_time=2)
        self.wait()
        self.play(FadeOut(text))

    def change_size_animation(self):
        self.camera.background_color = PINK
        text = Text("Text").scale(2)
        self.play(Write(text))
        self.wait()
        self.play(text.animate.scale(1.5), run_time=2)
        self.wait()
        self.play(FadeOut(text))

    def move_text(self):
        self.camera.background_color = ORANGE
        text = Text("Text").scale(2).shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        self.play(text.animate.shift(RIGHT * 2), run_time=2, path_arc=0)
        self.wait()
        self.play(FadeOut(text))

    def change_color_and_size_animation(self):
        self.camera.background_color = WHITE
        text = Text("Text").scale(2).shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.shift(RIGHT * 2).scale(2).set_color(RED),
            run_time=2
        )
        self.wait()
        self.play(FadeOut(text))
        
    def show_nombre(self):
        credit_text = Text("Hecho por Eric Carmen Soto")
        credit_text.to_edge(UP)
        self.play(Write(credit_text))
        self.wait(2)
        self.play(FadeOut(credit_text))
        
        
    def show_nombres(self):
        self.camera.background_color = "#406715"  
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

    

    






	
        
        
