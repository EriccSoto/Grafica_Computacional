from manim import *

class Saladito(Scene):
    def construct(self):
        
        #1 Pie izquierdo
        
        nombre = Text("Pie izquierdo", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)
        pataD = Rectangle(
            width=0.15, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([-0.8, -2, 0.5])
        self.anim(pataD)
        self.play(FadeOut(nombre))
        

        #2 Pie izquierdo y derecho
        
        nombre = Text("Pie izquierdo y derecho", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)
        pataIZ = Rectangle(
            width=0.15, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([0.8, -2, 0.5])
        self.anim(pataIZ)
        self.play(FadeOut(nombre))
        
        
        #3 CUERPO
        
        nombre = Text("Cuerpo", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)
        rombo = Polygon(
            [-2, 0, 0],  # Punto izquierdo
            [0, 2, 0],   # Punto superior
            [2, 0, 0],   # Punto derecho
            [0, -2, 0],  # Punto inferior
            color=YELLOW,
            fill_opacity=1
        )
        self.anim(rombo)
        self.play(FadeOut(nombre))
        
        
        #4 BRAZO Izquierdo
        
        nombre = Text("Brazo izquierdo", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)
        brazo_izquierdo = Rectangle(
            width=0.15, height=1.5, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([1.5, -1.4, 0]).rotate(PI/4, about_point=[1.5, -1, 0]) 
        self.anim(brazo_izquierdo)
        self.play(FadeOut(nombre))
        
        
        #5 BRAZO Derecho
        
        nombre = Text("Brazo derecho", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)
        brazo_derecho = Rectangle(
            width=0.15, height=1.5, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([-1.5, -1.4, 0]).rotate(-PI/4, about_point=[-1.5, -1, 0])
        self.anim(brazo_derecho)
        self.play(FadeOut(nombre))
        
        
        #6 BOCA
        
        nombre = Text("Boca", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)
        
        boca = Ellipse(
            width=1, height=2, color=GOLD, fill_opacity=1, stroke_color=BLACK, stroke_width=5
        ).shift([0, -0.3, 0])
        self.anim(boca)
        self.play(FadeOut(nombre))
        
        
        #7 OJO Derecho
        
        nombre = Text("Ojo derecho", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)
        
        
        ojo1 = Ellipse(
            width=0.6, height=0.7, color=BLACK, fill_opacity=1
        ).shift([-0.5, 1, 0])
        self.anim(ojo1)
        self.play(FadeOut(nombre))
        
        
        #8 OJO Izquierdo
        
        nombre = Text("Ojo izquierdo", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)
        
        
        ojo2 = Ellipse(
            width=0.6, height=0.7, color=BLACK, fill_opacity=1
        ).shift([0.5, 1, 0])
        self.anim(ojo2)
        self.play(FadeOut(nombre))
        
        
        
        #9 PARTE DE ATRÁS DE SALADITO
        
        nombre = Text("Parte de atras de saladito", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)
        
        parte_atras = Polygon(
            [-2, 0, 0],  # Punto izquierdo
            [0, 2, 0],   # Punto superior
            [2, 0, 0],   # Punto derecho
            [0, -2, 0],  # Punto inferior
            color=YELLOW,
            fill_opacity=1
        ).shift([0, 0, -0.5])
        self.anim(parte_atras)
        
        
        elementos1 = [boca, ojo1, ojo2, pataD, pataIZ, brazo_izquierdo, brazo_derecho, parte_atras,rombo]
        self.play(FadeOut(*elementos1))
        self.play(FadeOut(nombre))





       #10 Lado derecho 
       
        nombre = Text("Lado derecho de saladito", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)
        
        arriba = Rectangle(
            width=.7, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, fill_color=YELLOW, stroke_width=3
        ).shift([0, 1, 0])
        self.anim(arriba)

        abajo = Rectangle(
            width=.7, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, fill_color=GOLD, stroke_width=3
        ).shift([0, -1, 0])
        self.anim(abajo)

        pie = Rectangle(
            width=.35, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([0, -2.7, 0])
        self.anim(pie)

        brazo_lateral_D = Rectangle(
            width=.35, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([.7, -1.5, 0])
        brazo_lateral_D.rotate(PI/3)
        self.anim(brazo_lateral_D)

        self.play(
            FadeOut(arriba),
            FadeOut(abajo),
            FadeOut(pie),
            FadeOut(brazo_lateral_D)
        )
        self.play(FadeOut(nombre))

        #11 Lado izquierdo 
        
        nombre = Text("Lado izquierdo de saladito", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)
        arriba = Rectangle(
            width=.7, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, fill_color=YELLOW, stroke_width=3
        ).shift([0, 1, 0])
        self.anim(arriba)

        abajo = Rectangle(
            width=.7, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, fill_color=GOLD, stroke_width=3
        ).shift([0, -1, 0])
        self.anim(abajo)

        pie = Rectangle(
            width=.35, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([0, -2.7, 0])
        self.anim(pie)

        brazo_lateral_Z = Rectangle(
            width=.35, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([-.7, -1.5, 0])
        brazo_lateral_Z.rotate(-PI/3)
        self.anim(brazo_lateral_Z)

        self.play(
            FadeOut(arriba),
            FadeOut(abajo),
            FadeOut(pie),
            FadeOut(brazo_lateral_Z)
        )
        self.play(FadeOut(nombre))
        
        
        
        
        
        #12 Saludo:

        nombre = Text("Saladito saludando", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)

 
        # Pie izquierdo
        pataD = Rectangle(
            width=0.15, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([-0.8, -2, 0.5])
        self.anim(pataD)

        # Pie izquierdo y derecho
        pataIZ = Rectangle(
            width=0.15, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([0.8, -2, 0.5])
        self.anim(pataIZ)

        # CUERPO
        rombo = Polygon(
            [-2, 0, 0],  # Punto izquierdo
            [0, 2, 0],   # Punto superior
            [2, 0, 0],   # Punto derecho
            [0, -2, 0],  # Punto inferior
            color=YELLOW,
            fill_opacity=1
        )
        self.anim(rombo)

        # BRAZO Izquierdo
        brazo_izquierdo = Rectangle(
            width=0.15, height=1.5, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([1.7, -0.5, 0]).rotate(-PI/3) 
        self.anim(brazo_izquierdo)

        # BRAZO Derecho
        brazo_derecho = Rectangle(
            width=0.15, height=1.5, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3
        ).shift([-1.5, -1.4, 0]).rotate(-PI/4, about_point=[-1.5, -1, 0])
        self.anim(brazo_derecho)

        # BOCA
        boca = Ellipse(
            width=1, height=2, color=GOLD, fill_opacity=1, stroke_color=BLACK, stroke_width=5
        ).shift([0, -0.3, 0])
        self.anim(boca)

        # OJO Derecho
        ojo1 = Ellipse(
            width=0.6, height=0.7, color=BLACK, fill_opacity=1
        ).shift([-0.5, 1, 0])
        self.anim(ojo1)

        # OJO Izquierdo
        ojo2 = Ellipse(
            width=0.6, height=0.7, color=BLACK, fill_opacity=1
        ).shift([0.5, 1, 0])
        self.anim(ojo2)

        
        
        elementos1 = [boca, ojo1, ojo2, pataD, pataIZ, brazo_izquierdo, brazo_derecho,rombo]
        self.play(FadeOut(*elementos1))


        self.play(FadeOut(nombre))


    def anim(self, mob):
        self.play(Create(mob))
        # self.play(FadeOut(mob))
