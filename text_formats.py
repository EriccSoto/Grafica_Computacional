from manim import *

class Todo(Scene):

    def construct(self):
        self.show_initial_credit()
        self.write_text_with_background("#FFA500", "This is a regular text", 3)
        self.add_text_with_background("#32CD32", "This is a regular text", 3)
        self.write_text_with_formulas("#FF0000")
        self.write_text_with_latex("#800080")
        self.write_text_with_display_formula("#808080")
        self.write_centered_text("#FFFF00", "Text", 3)
        self.write_text_on_edge("#00FFFF", "Text", 3, position=UP)
        self.write_text_on_edge("#FF00FF", "Text", 3, position=DOWN)
        self.write_text_on_edge("#90EE90", "Text", 3, position=RIGHT)
        self.write_text_on_edge("#FFFFE0", "Text", 3, position=LEFT)
        self.write_text_on_corner("#ADD8E6", "Text", 3, position=UP+RIGHT)
        self.write_text_on_corner("#000000", "Text", 3, position=LEFT+DOWN)
        self.write_custom_position_text("#F5F5DC", 3)
        self.write_relative_position_text("#A9A9A9", 3)
        self.rotate_text("#FFC0CB")
        self.mirror_text("#2F4F4F")
        self.write_size_text("#800080")
        self.write_text_fonts("#800080")
        self.show_nombre()
    
    def show_initial_credit(self):
        self.camera.background_color = "#00008B"  
        credit_text = Text("Hecho por Eric Carmen Soto")
        credit_text.to_edge(UP)
        self.play(Write(credit_text))
        self.wait(2)
        self.play(FadeOut(credit_text))  

    def write_text_with_background(self, color, text, wait_time):
        self.camera.background_color = color
        text_object = Text(text)
        self.play(Write(text_object))
        self.wait(wait_time)
        self.play(FadeOut(text_object))  

    def add_text_with_background(self, color, text, wait_time):
        self.camera.background_color = color
        text_object = Text(text)
        self.add(text_object)
        self.wait(wait_time)
        self.play(FadeOut(text_object))  

    def write_text_with_formulas(self, color):
        self.camera.background_color = color
        typesOfText = Text(""" 
            This is a regular text,
            $this is a formula$,
            $$this is a formula$$
            """)
        self.play(Write(typesOfText))
        self.wait(3)
        self.play(FadeOut(typesOfText))  

    def write_text_with_latex(self, color):
        self.camera.background_color = color
        typesOfText2 = Tex(""" 
            This is a regular text,
            $\\frac{x}{y}$,
            $$x^2+y^2=a^2$$
            """)
        self.play(Write(typesOfText2))
        self.wait(3)
        self.play(FadeOut(typesOfText2))  

    def write_text_with_display_formula(self, color):
        self.camera.background_color = color
        typesOfText3 = Tex(""" 
            This is a regular text,
            $\\displaystyle\\frac{x}{y}$,
            $$x^2+y^2=a^2$$
            """)
        self.play(Write(typesOfText3))
        self.wait(3)
        self.play(FadeOut(typesOfText3))  

    def write_centered_text(self, color, text, wait_time):
        self.camera.background_color = color
        text_object = Text(text)
        text_object.set_color(BLACK)
        self.play(Write(text_object))
        self.wait(wait_time)
        self.play(FadeOut(text_object))  

    def write_text_on_edge(self, color, text, wait_time, position):
        self.camera.background_color = color
        text_object = Text(text)
        text_object.set_color(BLACK)
        text_object.to_edge(position)
        self.play(Write(text_object))
        self.wait(wait_time)
        self.play(FadeOut(text_object))  

    def write_text_on_corner(self, color, text, wait_time, position):
        self.camera.background_color = color
        text_object = Text(text) 
        text_object.to_edge(position)
        self.play(Write(text_object))
        self.wait(wait_time)
        self.play(FadeOut(text_object))  

    def write_custom_position_text(self, color, wait_time):
        self.camera.background_color = color
        text1 = Text("Text")
        text2 = Text("Central text")
        text1.set_color(BLACK)
        text2.set_color(BLACK)
        text1.move_to(1*UP) 
        self.play(Write(text1),Write(text2))
        self.wait(wait_time)
        self.play(FadeOut(text1), FadeOut(text2))  

    def write_relative_position_text(self, color, wait_time):
        self.camera.background_color = color
        text1 = Text("Text")
        text2 = Text("Reference text")
        text1.set_color(BLACK)
        text2.set_color(BLACK)
        text1.next_to(text2,LEFT,buff=1) 
        self.play(Write(text1),Write(text2))
        self.wait(wait_time)
        self.play(FadeOut(text1), FadeOut(text2))  

    def rotate_text(self, color):
        self.camera.background_color = color
        text1 = Text("Text")
        text2 = Text("Reference text")
        text1.shift(UP)
        text1.rotate(PI/4) 
        self.play(Write(text1),Write(text2))
        self.wait(2)
        text1.rotate(PI/4)
        self.wait(2)
        text1.rotate(PI/4)
        self.wait(2)
        text1.rotate(PI/4)
        self.wait(2)
        text1.rotate(PI)
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(text2))  

    def mirror_text(self, color):
        self.camera.background_color = color
        text1 = Text("Text")
        text1.flip(UP)
        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(text1))  

    def write_size_text(self, color):
        self.camera.background_color = color
        textHuge = Tex("{\\Huge Huge Text 012.\\#!?} Text")
        texthuge = Tex("{\\huge huge Text 012.\\#!?} Text")
        textLARGE = Tex("{\\LARGE LARGE Text 012.\\#!?} Text")
        textLarge = Tex("{\\Large Large Text 012.\\#!?} Text")
        textlarge = Tex("{\\large large Text 012.\\#!?} Text")
        textNormal = Tex("{\\normalsize normal Text 012.\\#!?} Text")
        textsmall = Tex("{\\small small Text 012.\\#!?} Texto normal")
        textfootnotesize = Tex("{\\footnotesize footnotesize Text 012.\\#!?} Text")
        textscriptsize = Tex("{\\scriptsize scriptsize Text 012.\\#!?} Text")
        texttiny = Tex("{\\tiny tiny Texto 012.\\#!?} Text normal")
        textHuge.to_edge(UP)
        texthuge.next_to(textHuge,DOWN,buff=0.1)
        textLARGE.next_to(texthuge,DOWN,buff=0.1)
        textLarge.next_to(textLARGE,DOWN,buff=0.1)
        textlarge.next_to(textLarge,DOWN,buff=0.1)
        textNormal.next_to(textlarge,DOWN,buff=0.1)
        textsmall.next_to(textNormal,DOWN,buff=0.1)
        textfootnotesize.next_to(textsmall,DOWN,buff=0.1)
        textscriptsize.next_to(textfootnotesize,DOWN,buff=0.1)
        texttiny.next_to(textscriptsize,DOWN,buff=0.1)
        self.add(textHuge,texthuge,textLARGE,textLarge,textlarge,textNormal,textsmall,textfootnotesize,textscriptsize,texttiny)
        self.wait(3)
        self.play(FadeOut(textHuge), FadeOut(texthuge), FadeOut(textLARGE), FadeOut(textLarge), FadeOut(textlarge), FadeOut(textNormal), FadeOut(textsmall), FadeOut(textfootnotesize), FadeOut(textscriptsize), FadeOut(texttiny))  

    def write_text_fonts(self, color):
        self.camera.background_color = color
        textNormal = Tex("{Roman serif text 012.\\#!?} Text")
        textItalic = Tex("\\textit{Italic text 012.\\#!?} Text")
        textBold = Tex("\\textbf{Bold text 012.\\#!?} Text")
        textSlanted = Tex("\\textsl{Slanted text 012.\\#!?} Text")
        textTypewriter = Tex("\\texttt{Typewriter text 012.\\#!?} Text")
        textSans = Tex("\\textsf{Sans serif text 012.\\#!?} Text")
        textNormal.to_edge(UP)
        textItalic.next_to(textNormal,DOWN,buff=0.1)
        textBold.next_to(textItalic,DOWN,buff=0.1)
        textSlanted.next_to(textBold,DOWN,buff=0.1)
        textTypewriter.next_to(textSlanted,DOWN,buff=0.1)
        textSans.next_to(textTypewriter,DOWN,buff=0.1)
        self.add(textNormal,textItalic,textBold,textSlanted,textTypewriter,textSans)
        self.wait(3)
        self.play(FadeOut(textNormal), FadeOut(textItalic), FadeOut(textBold), FadeOut(textSlanted), FadeOut(textTypewriter), FadeOut(textSans))  


    def show_nombre(self):
        self.camera.background_color = "#00008B"  
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