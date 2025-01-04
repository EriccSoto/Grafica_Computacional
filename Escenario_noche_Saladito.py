from manim import *

# Clase para los árboles
class Arbol:
    def __init__(self, posicion_x):
        self.posicion_x = posicion_x
        self.tronco = None
        self.copa_1 = None
        self.copa_2 = None
        self.copa_3 = None

    def crear_arbol(self):
        # Tronco del árbol
        self.tronco = Rectangle(width=0.3, height=1, color=DARK_BROWN, fill_opacity=1)
        self.tronco.set_stroke(color=BLACK, width=2)
        self.tronco.shift(DOWN * 1 + self.posicion_x)

        # Copa del árbol (tres óvalos verdes)
        self.copa_1 = Ellipse(width=1, height=0.6, color=GREEN, fill_opacity=1).next_to(self.tronco, UP, buff=0)
        self.copa_2 = Ellipse(width=1.2, height=0.7, color=GREEN, fill_opacity=1).next_to(self.copa_1, UP * 0.3)
        self.copa_3 = Ellipse(width=0.8, height=0.5, color=GREEN, fill_opacity=1).next_to(self.copa_2, UP * 0.2)

    def dibujar(self, escena):
        escena.add(self.tronco, self.copa_1, self.copa_2, self.copa_3)

# Clase para la luna
class Luna:
    def __init__(self):
        self.luna = None

    def crear_luna(self):
        self.luna = Circle(radius=0.5, color=WHITE, fill_opacity=1)
        self.luna.set_stroke(color=WHITE, width=2)
        self.luna.to_corner(UP + RIGHT)

    def dibujar(self, escena):
        escena.add(self.luna)

# Clase para el pasto
class Pasto:
    def __init__(self):
        self.pasto = None

    def crear_pasto(self):
        self.pasto = Rectangle(width=config.frame_width, height=2, color=GREEN, fill_opacity=1)
        self.pasto.shift(DOWN * 2.5)

    def dibujar(self, escena):
        escena.add(self.pasto)

# Clase para la escena nocturna
class NocheScene:
    @staticmethod
    def crear_fondo():
        # Crear el cielo oscuro como fondo
        cielo = Rectangle(width=config.frame_width, height=config.frame_height, color=DARK_BLUE, fill_opacity=1)

        # Crear el pasto
        pasto = Pasto()
        pasto.crear_pasto()

        # Crear los árboles
        posiciones_arboles = [LEFT * 3, LEFT * 1, RIGHT * 1.5, RIGHT * 3.5]
        arboles = [Arbol(pos) for pos in posiciones_arboles]
        for arbol in arboles:
            arbol.crear_arbol()

        # Crear la luna
        luna = Luna()
        luna.crear_luna()

        # Devolver todos los elementos del fondo
        return VGroup(cielo, pasto.pasto, *[a.tronco for a in arboles], *[a.copa_1 for a in arboles],
                      *[a.copa_2 for a in arboles], *[a.copa_3 for a in arboles], luna.luna)

# Clase para Saladito
class Saladito(Scene):
    def construct(self):
        # Crear y añadir el fondo
        fondo = NocheScene.crear_fondo()
        self.add(fondo)

        #  elementos de Saladito
        pataD = Rectangle(width=0.15, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3).shift([-0.8, -2, 0.5])
        pataIZ = Rectangle(width=0.15, height=2, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3).shift([0.8, -2, 0.5])
        rombo = Polygon([-2, 0, 0], [0, 2, 0], [2, 0, 0], [0, -2, 0], color=YELLOW, fill_opacity=1)
        brazo_izquierdo = Rectangle(width=0.15, height=1.5, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3).shift([1.7, -0.5, 0]).rotate(-PI/3)
        brazo_derecho = Rectangle(width=0.15, height=1.5, color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=3).shift([-1.5, -1.4, 0]).rotate(-PI/4, about_point=[-1.5, -1, 0])
        boca = Ellipse(width=1, height=2, color=GOLD, fill_opacity=1, stroke_color=BLACK, stroke_width=5).shift([0, -0.3, 0])
        ojo1 = Ellipse(width=0.6, height=0.7, color=BLACK, fill_opacity=1).shift([-0.5, 1, 0])
        ojo2 = Ellipse(width=0.6, height=0.7, color=BLACK, fill_opacity=1).shift([0.5, 1, 0])

        # Animaciones de  elementos
        self.anim(pataD)
        self.anim(pataIZ)
        self.anim(rombo)
        self.anim(brazo_izquierdo)
        self.anim(brazo_derecho)
        self.anim(boca)
        self.anim(ojo1)
        self.anim(ojo2)

        #salto de Saladito
        
        
        self.play(
            AnimationGroup(
                rombo.animate.shift(UP * 0.5),
                pataD.animate.shift(UP * 0.5),
                pataIZ.animate.shift(UP * 0.5),
                brazo_izquierdo.animate.shift(UP * 0.5),
                brazo_derecho.animate.shift(UP * 0.5),
                boca.animate.shift(UP * 0.5),
                ojo1.animate.shift(UP * 0.5),
                ojo2.animate.shift(UP * 0.5),
                lag_ratio=0, 
            ),
            run_time=0.5  
        )

        self.play(
            AnimationGroup(
                rombo.animate.shift(DOWN * 0.5),
                pataD.animate.shift(DOWN * 0.5),
                pataIZ.animate.shift(DOWN * 0.5),
                brazo_izquierdo.animate.shift(DOWN * 0.5),
                brazo_derecho.animate.shift(DOWN * 0.5),
                boca.animate.shift(DOWN * 0.5),
                ojo1.animate.shift(DOWN * 0.5),
                ojo2.animate.shift(DOWN * 0.5),
                lag_ratio=0, 
            ),
            run_time=0.5  
        )
        
        
        self.play(
            AnimationGroup(
                rombo.animate.shift(UP * 0.5),
                pataD.animate.shift(UP * 0.5),
                pataIZ.animate.shift(UP * 0.5),
                brazo_izquierdo.animate.shift(UP * 0.5),
                brazo_derecho.animate.shift(UP * 0.5),
                boca.animate.shift(UP * 0.5),
                ojo1.animate.shift(UP * 0.5),
                ojo2.animate.shift(UP * 0.5),
                lag_ratio=0,  
            ),
            run_time=0.5
        )

        self.play(
            AnimationGroup(
                rombo.animate.shift(DOWN * 0.5),
                pataD.animate.shift(DOWN * 0.5),
                pataIZ.animate.shift(DOWN * 0.5),
                brazo_izquierdo.animate.shift(DOWN * 0.5),
                brazo_derecho.animate.shift(DOWN * 0.5),
                boca.animate.shift(DOWN * 0.5),
                ojo1.animate.shift(DOWN * 0.5),
                ojo2.animate.shift(DOWN * 0.5),
                lag_ratio=0,  
            ),
            run_time=0.5 
        )
        
        
        self.play(
            AnimationGroup(
                rombo.animate.shift(UP * 0.5),
                pataD.animate.shift(UP * 0.5),
                pataIZ.animate.shift(UP * 0.5),
                brazo_izquierdo.animate.shift(UP * 0.5),
                brazo_derecho.animate.shift(UP * 0.5),
                boca.animate.shift(UP * 0.5),
                ojo1.animate.shift(UP * 0.5),
                ojo2.animate.shift(UP * 0.5),
                lag_ratio=0,  
            ),
            run_time=0.5 
        )

        self.play(
            AnimationGroup(
                rombo.animate.shift(DOWN * 0.5),
                pataD.animate.shift(DOWN * 0.5),
                pataIZ.animate.shift(DOWN * 0.5),
                brazo_izquierdo.animate.shift(DOWN * 0.5),
                brazo_derecho.animate.shift(DOWN * 0.5),
                boca.animate.shift(DOWN * 0.5),
                ojo1.animate.shift(DOWN * 0.5),
                ojo2.animate.shift(DOWN * 0.5),
                lag_ratio=0, 
            ),
            run_time=0.5 
        )
        
        
        
        # saludo
        texto = Text("Soy Saladito y Me hizo Eric Carmen Soto", font_size=24).to_edge(UP)
        self.anim(texto)

        # Desaparecer elementos
        elementos1 = [boca, ojo1, ojo2, pataD, pataIZ, brazo_izquierdo, brazo_derecho, rombo]
        self.play(FadeOut(*elementos1))

    def anim(self, mob):
        self.play(Create(mob))
