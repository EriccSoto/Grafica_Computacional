from manim import *
import numpy as np

class Todo(Scene):
    def construct(self):
        self.show_nombre()
        self.plot_graph()
        self.plot1()
        self.plot1v2()
        self.plot2()
        self.plot3()
        self.plot4()
        self.plot5()
        self.show_nombres()
        
        
    def show_nombre(self):
        credit_text = Text("Hecho por Eric Carmen Soto")
        credit_text.to_edge(UP)
        self.play(Write(credit_text))
        self.wait(2)
        self.play(FadeOut(credit_text))  
    def plot_graph(self):
        self.camera.background_color = "#783b3b"  
        y_max = 50
        y_min = 20
        x_max = 7
        x_min = 4
        y_tick_frequency = 5
        x_tick_frequency = 0.5
        axes_color = WHITE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
        )
        
        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )
        
        axes.x_axis.add_numbers([4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
        axes.y_axis.add_numbers([30, 40, 50])

        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[5, 7]) 

        p = Dot().move_to(axes.c2p(x_min, y_min))
        
        self.add(axes, axes_labels, p)
               
        self.play(Create(graph), run_time=2)
        self.wait()
        self.play(FadeOut(graph), FadeOut(axes), FadeOut(axes_labels), FadeOut(p))
        
    def plot1(self):
        self.camera.background_color = "#406715"  
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 5
        x_tick_frequency = 0.5
        axes_color = WHITE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips=False
        )
        
        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )

        axes.x_axis.add_numbers([2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
        axes.y_axis.add_numbers([20, 30, 40, 50])

        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[2, 4])

        self.play(Write(axes), Write(axes_labels), run_time=4)
        self.play(Create(graph), run_time=2)
        self.wait()
        self.play(FadeOut(graph), FadeOut(axes), FadeOut(axes_labels))
        
    def plot1v2(self):
        self.camera.background_color = "#152667"  
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 5
        x_tick_frequency = 1
        axes_color = WHITE

        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips=False
        ).scale(0.5) 
        
        axes.to_corner(UR)
        
        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[2, 4])

        self.play(Write(axes), Write(axes_labels), Create(graph), run_time=2)
        self.wait()
        self.play(FadeOut(graph), FadeOut(axes), FadeOut(axes_labels))
        
    def plot2(self):
        self.camera.background_color = "#34495e"  
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 5
        x_tick_frequency = 1
        axes_color = WHITE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips=False
        )

        axes.x_axis.add_numbers([2, 3, 4, 5 ,6 ,7])
        axes.y_axis.add_numbers([20, 30, 40, 50])

        graph = axes.plot(lambda x: x**2, color=GREEN)

        axes_labels = axes.get_axis_labels(
            x_label=Tex("t"),
            y_label=Tex("f(t)")
        )

        self.add(axes, axes_labels)

        self.play(Write(axes), Write(axes_labels), run_time=2)
        self.play(Create(graph), run_time=2)

        self.wait()
        self.play(FadeOut(graph), FadeOut(axes), FadeOut(axes_labels))
        
    def plot3(self):
        self.camera.background_color = "#581567"  
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 5
        x_tick_frequency = 1
        axes_color = WHITE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips=False
        )

        axes.x_axis.add_numbers([0, 2, 4, 5])
        axes.y_axis.add_numbers([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

        graph = axes.plot(lambda x: x**2, color=GREEN)

        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )

        self.add(axes, axes_labels)

        self.play(Write(axes), Write(axes_labels), run_time=2)
        self.play(Create(graph), run_time=2)

        self.wait()
        self.play(FadeOut(graph), FadeOut(axes), FadeOut(axes_labels))
        
    def plot4(self):
        self.camera.background_color = "#676315"  
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 10
        x_tick_frequency = 1
        axes_color = WHITE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips=False
        )

        axes.x_axis.add_numbers([3.5, 4, 5])
        axes.y_axis.add_numbers([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

        graph = axes.plot(lambda x: x**2, color=GREEN)

        axes_labels = axes.get_axis_labels(
            x_label=Tex("x"),
            y_label=Tex("y")
        )

        self.add(axes, axes_labels)

        self.play(Write(axes), Write(axes_labels), run_time=2)
        self.play(Create(graph), run_time=2)

        self.wait()
        self.play(FadeOut(graph), FadeOut(axes), FadeOut(axes_labels))
        
    def plot5(self):
        self.camera.background_color = "#671515"  
        y_max = 50
        y_min = 0
        x_max = 7
        x_min = 0
        y_tick_frequency = 10
        x_tick_frequency = 0.5
        axes_color = WHITE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
            tips=False
        )

        x_labels = VGroup()  
        
        label_3_5 = Tex("3.5")
        label_3_5.scale(0.7)
        label_3_5.next_to(axes.coords_to_point(3.5, 0), DOWN)
        x_labels.add(label_3_5)

        label_4_5 = MathTex("\\frac{9}{2}")
        label_4_5.scale(0.7)
        label_4_5.next_to(axes.coords_to_point(4.5, 0), DOWN)
        x_labels.add(label_4_5)
        
        self.play(Write(x_labels))
        self.wait()
        self.play(FadeOut(x_labels))
        
    def show_nombres(self):
        self.camera.background_color = "#614b8f"  
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
        
    
