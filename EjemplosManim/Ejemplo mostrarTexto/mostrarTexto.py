#Se importa Manim
from manim import *

#Se configura un fondo de color gris claro
config.background_color = LIGHT_GRAY


class mostrarTexto(Scene):
	
    #Se crea el constructor
    def construct(self):

        # Se crean objetos de texto
        nombreVariable1 = Text('Aquí se introduce el texto', color=BLACK)
        nombreVariable2 = Text('Aquí se introduce el segundo texto', color=RED)

        # Para colocar una línea debajo de la otra
        nombreVariable2.next_to(nombreVariable1, DOWN)

        # Para mostrar el texto en la animación
        self.play(Write(nombreVariable2), Write(nombreVariable1))

        # Para guardar un tiempo de espera
        self.wait(1)
	        