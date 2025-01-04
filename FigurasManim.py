from manim import *

class AllShapes(Scene):
    def construct(self):
        nombre = Text("Eric Carmen Soto", font_size=24)
        nombre.to_edge(UP)  
        self.add(nombre)

        self.anim(Arc(radius=0.5, color=RED, fill_color=GREEN, fill_opacity=1))
        self.anim(ArcBetweenPoints(np.array([2,0,0]), np.array([-2,0,0]), color=YELLOW))
        self.anim(CurvedArrow(np.array([2,0,0]), np.array([-2,0,0]), color=ORANGE))
        self.anim(CurvedDoubleArrow(np.array([2,0,0]), np.array([-2,0,0]), color=PINK))
        self.anim(Circle(color=BLUE, fill_color=WHITE, fill_opacity=1))
        self.anim(Dot(radius=0.1, color=PURPLE, fill_color=BLACK, fill_opacity=1))
        self.anim(Ellipse(color=GREY, fill_color=RED, fill_opacity=1))
        self.anim(AnnularSector(color=GOLD, fill_color=BLUE, fill_opacity=1))
        self.anim(Sector(color=GREEN, fill_color=YELLOW, fill_opacity=1))
        self.anim(Line(np.array([2,0,0]), np.array([-2,0,0]), color=BLACK))
        self.anim(DashedLine(np.array([2,0,0]), np.array([-2,0,0]), color=WHITE))

        # Creación de los polígonos con un color único y relleno
        self.anim(Polygon(np.array([2, 0, 0]), np.array([-2, 0, 0]), np.array([1, 1, 0]), np.array([-2, -3, 0]), color=ORANGE, fill_color=ORANGE, fill_opacity=1))
        self.anim(RegularPolygon(n=5, color=PURPLE, fill_color=PURPLE, fill_opacity=1))
        self.anim(Triangle(color=BLACK, fill_color=BLACK, fill_opacity=1))
        self.anim(Rectangle(color=RED, fill_color=RED, fill_opacity=1))
        self.anim(Square(color=GREEN, fill_color=GREEN, fill_opacity=1))
        self.anim(RoundedRectangle(color=YELLOW, fill_color=YELLOW, fill_opacity=1))

    def anim(self, mob):
        self.play(Create(mob))
        self.play(FadeOut(mob))
