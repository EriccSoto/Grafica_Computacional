from manim import *

class QuadraticFormulaScene(Scene):
    
    def construct(self):
        # Escribe la fórmula general para resolver ecuaciones cuadráticas
        formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"
        )
        
        # Muestra la fórmula en la pantalla
        self.add(formula)
        
        # Centra la fórmula en la pantalla
       # formula.move_to(ORIGIN)
        
        # Pausa para que se vea la fórmula
        #self.wait()
