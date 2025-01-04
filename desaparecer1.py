#!/usr/bin/env python

from manim import *

class Shapes(Scene):
  def construct(self):
    circulo = Circle() # Creación de circulo
    createCircle = Create(circulo) # Animación de creación
    self.play(createCircle) # Mostrar la animación
    
    
    fadeOutCircle = FadeOut(circulo) # Animación de desaparición
    self.play(fadeOutCircle) # Mostrar la animación
    
    