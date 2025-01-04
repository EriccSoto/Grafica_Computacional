from manim import *

COLOR_P = "#3EFC24"

class Todo(Scene):
    def construct(self):
        self.show_nombre()
        self.text_color()
        self.formula_color_1()
        self.formula_color_2()
        self.formula_color_3()
        self.formula_color_3_fixed()
        self.formula_color_3_fixed_2()
        self.formula_color_4()
        self.formula_color_5()
        self.color_by_character()
        self.color_by_character_fixed()
        self.list_for()
        self.for_range_1()
        self.for_range_2()
        self.for_two_variables()
        self.change_size()
        self.add_and_remove_text()
        self.fade_text()
        self.fade_text_from_direction()
        self.grow_object_from_center()
        self.show_creation_object()
        self.coloring_text()
        self.cross_text_1()
        self.cross_text_2()
        self.frame_box_1()
        self.frame_box_2()
        self.brace_text()
        self.show_nombres()
        
    def show_nombre(self):
        self.camera.background_color = "#00008B"  # Azul oscuro
        credit_text = Text("Hecho por Eric Carmen Soto")
        credit_text.to_edge(UP)
        self.play(Write(credit_text))
        self.wait(2)
        self.play(FadeOut(credit_text))  

    def text_color(self):
        self.camera.background_color = "#FF6347"  # Fondo rojo
        text = Tex("A", "B", "C", "D", "E", "F")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")  # Hexadecimal color
        text[5].set_color(COLOR_P)
        self.play(Write(text))
        self.wait(2)
        self.clear()  

    def formula_color_1(self):
        self.camera.background_color = "#7FFFD4"  # Fondo aqua
        text = MathTex("x", "=", "{a", "\\over", "b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")
        self.play(Write(text))
        self.wait(2)
        self.clear()  

    def formula_color_2(self):
        self.camera.background_color = "#FFD700"  # Fondo dorado
        text = MathTex("x", "=", "\\frac{a}{b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        self.play(Write(text))
        self.wait(2)
        self.clear()  

    def formula_color_3(self):
        self.camera.background_color = "#8A2BE2"  # Fondo azul violeta
        text = MathTex("\\sqrt{", "\\int_{", "a}^", "{b}", "\\left(", "\\frac{x}{y}", "\\right)", "dx}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(2)
        self.clear()  

    def formula_color_3_fixed(self):
        self.camera.background_color = "#00FA9A"  # Fondo verde claro
        text = MathTex("\\sqrt{", "\\int_{", "a}^", "{b}", "\\left(", "\\frac{x}{y}", "\\right)", "dx.}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(3)
        self.clear()  

    def formula_color_3_fixed_2(self):
        self.camera.background_color = "#D2691E"  # Fondo marrón
        text = MathTex("\\sqrt{", "\\int_", "{a}^", "{b}", "{\\left(", "{x", "\\over", "y}", "\\right)}", "d", "x", ".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        self.play(Write(text))
        self.wait(3)
        self.clear()  

    def formula_color_4(self):
        self.camera.background_color = "#DC143C"  # Fondo rojo oscuro
        text = MathTex("\\sqrt{", "\\int_", "{a","+","c}^", "{b}", "{\\left(", "{x", "\\over", "y}", "\\right)}", "d", "x", ".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        text[10].set_color(GRAY)
        text[11].set_color(RED)
        self.play(Write(text))
        self.wait(3)
        self.clear()  

    def formula_color_5(self):
        self.camera.background_color = "#40E0D0"  # Fondo turquesa
        text = MathTex("\\sqrt{", "\\int_", "{a","+","c}^", "{b}", "{\\left(", "{x", "\\over", "y}", "\\right)}", "d", "x", ".}")
        text[0].set_color(PURPLE)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        self.play(Write(text))
        self.wait(3)
        self.clear()  

    def color_by_character(self):
        self.camera.background_color = "#F0E68C"  # Fondo caqui
        text = MathTex("{d", "\\over", "d", "x", "}","\\int_", "{a}^", "{x}", "f(", "t", ")d", "t", "=", "f(", "x", ")")
        text.set_color_by_tex("x", RED)
        self.play(Write(text))
        self.wait(2)
        self.clear()  

    def color_by_character_fixed(self):
        self.camera.background_color = "#E6E6FA"  # Fondo lavanda
        text = MathTex("{d", "\\over", "d", "x", "}","\\int_", "{a}^", "{x}", "f(", "t", ")d", "t", "=", "f(", "x", ")")
        text.set_color_by_tex("x", RED)
        text[6].set_color(RED)
        text[8].set_color(WHITE)
        self.play(Write(text))
        self.wait(2)
        self.clear()  

    def list_for(self):
        self.camera.background_color = "#FF8C00"  # Fondo naranja
        text = Tex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        for i in [0, 1, 3, 4]:
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)
        self.clear()  

    def for_range_1(self):
        self.camera.background_color = "#ADFF2F"  # Fondo verde pasto
        text = Tex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        for i in range(3):
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)
        self.clear()  

    def for_range_2(self):
        self.camera.background_color = "#C71585"  # Fondo rosa fuerte
        text = Tex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        for i in range(2, 6):
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)
        self.clear()  

    def for_two_variables(self):
        self.camera.background_color = "#B0E0E6"  # Fondo azul claro
        text = Tex("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        text[2].set_color(RED)
        text[4].set_color(PINK)
        self.play(Write(text))
        self.wait(3)
        self.clear()  

    def change_size(self):
        self.camera.background_color = "#FF1493"  # Fondo fucsia
        text = Tex(r"$$\sum_{i=0}^n i = \frac{n(n+1)}{2}$$")
        text.scale(1.5)  
        self.play(Write(text))
        self.wait(2)
        self.clear()  

    def add_and_remove_text(self):
        self.camera.background_color = "#C0C0C0"  # Fondo gris
        text = Tex("Texto agregado")
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text)) 
        self.wait(2)
        self.clear()  

    def fade_text(self):
        self.camera.background_color = "#F08080"  # Fondo salmón
        text = Tex("Texto que se desvanece")
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))  
        self.wait(2)
        self.clear()  

    def fade_text_from_direction(self):
        self.camera.background_color = "#D3D3D3"  # Fondo gris claro
        text = Tex("Texto que se desvanece desde un lado")
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text, shift=UP)) 
        self.wait(2)
        self.clear()  

    def grow_object_from_center(self):
        self.camera.background_color = "#FF6347"  # Fondo rojo tomate
        square = Square()
        self.play(GrowFromCenter(square))  
        self.wait(2)
        self.clear()  

    def show_creation_object(self):
        self.camera.background_color = "#8A2BE2"  # Fondo azul violeta
        square = Square()
        self.play(Create(square))  
        self.wait(2)
        self.clear()  

    def coloring_text(self):
        self.camera.background_color = "#40E0D0"  # Fondo turquesa
        text = Tex("Texto que cambia de color")
        text.set_color(RED)
        self.play(Write(text))
        self.wait(2)
        self.clear()  

    def cross_text_1(self):
        self.camera.background_color = "#A52A2A"  # Fondo marrón
        text = MathTex(
                    r"\sum_{i=1}^{\infty} i = -\frac{1}{2}"
                )
        
        self.play(Write(text))  
        self.wait(2)
        
        self.play(FadeOut(text))  
        self.wait(2)
        
        self.clear() 

    def cross_text_2(self):
        self.camera.background_color = "#98FB98"  
        text = MathTex(r"\sum_{i=1}^{\infty} i = -\frac{1}{2}")  
        self.play(Write(text))  # Escribir el texto
        self.wait(2)
        
        
        self.play(Indicate(text))  
        self.wait(2)
        
        self.clear()  

    def frame_box_1(self):
        self.camera.background_color = "#8B4513"  # Fondo marrón oscuro
        text = MathTex(
    r"\hat{g}(", r"f", r")", r"=", r"\int_{t_1}^{t_2}",
    r"g(", r"t", r")", r"e^{-2\pi i f t}", r"dt"
)
        self.play(Write(text))
        self.wait(2)
        self.play(Create(SurroundingRectangle(text))) 
        self.wait(2)
        self.clear()  

    def frame_box_2(self):
        self.camera.background_color = "#20B2AA"  # Fondo verde mar
        text = MathTex(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        self.play(Write(text))
        self.wait(2)
        self.play(Create(SurroundingRectangle(text, color=BLUE)))  
        self.wait(2)
        self.clear()  

    def brace_text(self):
        self.camera.background_color = "#FF4500"  # Fondo naranja rojo
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))

       
        brace_top = Brace(text[1], UP, buff=SMALL_BUFF)
        brace_bottom = Brace(text[3], DOWN, buff=SMALL_BUFF)

        
        text_top = brace_top.get_text("$g'f$")
        text_bottom = brace_bottom.get_text("$f'g$")

        
        self.play(GrowFromCenter(brace_top), Write(text_top))
        self.play(GrowFromCenter(brace_bottom), Write(text_bottom))

        self.wait(2)
        
        
        self.wait(2)
        self.clear()  
        
        
    def show_nombres(self):
        self.camera.background_color = "#FF6347"  
        credit_text = Text(
            "Universidad Autónoma del Estado de México\n"
            "Centro Universitario UAEM Zumpango\n"
            "Ingeniería en Computación\n"
            "GRAFICACIÓN COMPUTACIONAL\n\n"
            "Alumno: Eric Carmen Soto\n"
            "Segundo Periodo\n\n"
            "Fecha: 25 de Noviembre 2024"
        ).scale(0.5) 
        credit_text.to_edge(ORIGIN)
        self.play(Write(credit_text))
        self.wait(5)  
        self.play(FadeOut(credit_text))  