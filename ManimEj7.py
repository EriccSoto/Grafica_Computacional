from manim import *
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(RED, opacity=0.5)  # set the color and transparency
        
        circle2 = Circle()  # create a circle
        circle2.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(GREEN, opacity=0.5)  # set the color and transparency
        
        square2 = Square()  # create a square
        square2.set_fill(YELLOW, opacity=0.5)  # set the color and transparency
        
        '''
        square.move_to([-5, 2, 0])
        circle.move_to([5, 2, 0])
        square2.move_to([5, -2, 0])
        circle2.move_to([-5, -2, 0])
        '''
        square.to_corner(UP+LEFT)
        circle.to_corner(UP+RIGHT)
        square2.to_corner(DOWN+RIGHT)
        circle2.to_corner(DOWN+LEFT)

        self.play(Create(circle), Create(square),Create(square2), Create(circle2))  # show the shapes on screen