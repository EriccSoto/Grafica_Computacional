#!/usr/bin/env python

from manim import *


class WriteStuff(Scene):
    def construct(self):
        # Texto de ejemplo con colores
        example_text = Tex(
            "This is some text",
            tex_to_color_map={"text": YELLOW}
        )
        
        # Fórmula matemática
        example_tex = MathTex(
            r"\sum_{k=1}^\infty {1 \over k^2} = {\pi^2 \over 6}",
        )
        
        # Agrupar ambos elementos
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(config.frame_width - 2 * LARGE_BUFF)  # Usar config.frame_width

        # Animaciones
        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()



