from manim import *

class Todo(Scene):
    def construct(self):
        self.show_nombre()
        self.text_like_1d_arrays()
        self.text_like_2d_arrays_v1()
        self.text_like_2d_arrays_v2()
        self.text_like_2d_arrays_v3()
        self.transform_issues()
        self.transform_vgroup()
        self.transform_issues_solution1()
        self.transform_issues_solution_infallible()
        self.show_nombres()

    def show_nombre(self):
        credit_text = Text("Hecho por Eric Carmen Soto")
        credit_text.to_edge(UP)
        self.play(Write(credit_text))
        self.wait(2)
        self.play(FadeOut(credit_text))

    def text_like_1d_arrays(self):
        self.camera.background_color = "#FF1493"  
        text1 = Text("Te")
        text2 = Text("xt")
        text2.next_to(text1, RIGHT)
        self.play(FadeIn(text1))
        self.wait(0.5)
        self.play(FadeOut(text1))
        self.play(FadeIn(text2))
        self.wait(0.5)
        self.play(FadeOut(text2))

    def text_like_2d_arrays_v1(self):
        self.camera.background_color = "#09535b"  # Otro color oscuro
        text = [
            [Text("T"), Text("e")],
            [Text("x"), Text("t")]
        ]
        text[0][0].shift(LEFT + UP)
        text[0][1].next_to(text[0][0], RIGHT)
        text[1][0].next_to(text[0][0], DOWN)
        text[1][1].next_to(text[1][0], RIGHT)
        self.play(FadeIn(text[0][0]))
        self.play(FadeIn(text[0][1]))
        self.play(FadeIn(text[1][0]))
        self.play(FadeIn(text[1][1]))
        self.wait()
        self.play(FadeOut(text[0][0]), FadeOut(text[0][1]), FadeOut(text[1][0]), FadeOut(text[1][1]))

    def text_like_2d_arrays_v2(self):
        self.camera.background_color = "#FF4500"  # Otro color oscuro
        text1 = Text("Te")
        text2 = Text("xt")
        text2.next_to(text1, RIGHT, buff=0.2)
        for char in text1:
            self.play(FadeIn(char))
        for char in text2:
            self.play(FadeIn(char))
        self.wait()
        self.play(FadeOut(text1), FadeOut(text2))

    def text_like_2d_arrays_v3(self):
        self.camera.background_color = "#32CD32"  # Otro color oscuro
        text = [Text("Te"), Text("xt")]
        text[1].next_to(text[0], RIGHT, buff=0.2)
        for part in text:
            for char in part:
                self.play(FadeIn(char))
        self.wait()
        self.play(FadeOut(text[0]), FadeOut(text[1]))

    def transform_issues(self):
        self.camera.background_color = "#212F3D"  # Otro color oscuro
        text_1 = VGroup(Text("A"), Text("B"), Text("C"))
        text_2 = Text("B")
        text_1.arrange(RIGHT, buff=0.5)
        text_2.next_to(text_1, UP, buff=1)
        self.play(
            *[
                FadeIn(text_1[i])
                for i in [0, 2]
            ],
            FadeIn(text_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(text_2, text_1[1])
        )
        self.wait()
        self.play(FadeOut(text_1), FadeOut(text_2))

    def transform_vgroup(self):
        self.camera.background_color = "#FF6347"  # Otro color oscuro
        text_n = Text("A")
        text_v = VGroup(Text("A")).next_to(text_n, DOWN)
        self.play(Write(text_n))
        self.play(ReplacementTransform(text_n, text_v[0]))
        self.wait()
        self.play(FadeOut(text_v[0]))

    def transform_issues_solution1(self):
        self.camera.background_color = "#D2691E"  # Otro color oscuro
        text_1 = Text("ABC")
        text_2 = Text("B")
        text_2.next_to(text_1, UP, buff=1)
        self.play(
            *[
                FadeIn(text_1[i])
                for i in [0, 2]
            ],
            FadeIn(text_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(text_2, text_1[1])
        )
        self.wait()
        self.play(FadeOut(text_1), FadeOut(text_2))

    def transform_issues_solution_infallible(self):
        self.camera.background_color = "#DC143C"  
        text_1 = Text("ABC")
        text_2 = Text("B")
        text_2.next_to(text_1, UP, buff=1)
        text_1_1_c = Text("B") \
            .match_style(text_1[1]) \
            .match_width(text_1[1]) \
            .move_to(text_1[1])
        self.play(
            *[
                FadeIn(text_1[i])
                for i in [0, 2]
            ],
            FadeIn(text_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(text_2, text_1_1_c)
        )
        self.remove(text_1_1_c)
        self.add(text_1[1])
        self.wait()
        self.play(FadeOut(text_1), FadeOut(text_2))

    def show_nombres(self):
        self.camera.background_color = "#7FFF00"  
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
