#Se importa Manim
from manim import *

#Se configura un fondo de color gris claro
config.background_color = LIGHT_GRAY

#Escena: Se crea la clase y el constructor 
class mostrarEcuaciones(Scene):
    def construct(self):
        
        #Objeto: Se guarda la ecuación en una variable llamada eq, note que la
        # ecuación es creada en LaTeX y debe hacer el cambio de \ a doble \\
        eq1=MathTex("\\displaystyle P\\{x_1 < {X} \\leq x_2\\}", "=",
        "\\int_{x_1}^{x_2}f_{X}(x)~\\mathsf{d}x")

        #Se reproduce el tex
        self.play(Write(eq1))

        #Objeto: Se encierra en un rectángulo la parte deseada de la ecuación
        framebox1 = SurroundingRectangle(eq1[0], buff = .1)
        framebox2 = SurroundingRectangle(eq1[2], buff = .1)
       
        #Animación: Se muestra el framebox1 y se guarda un tiempo de espera
        self.play(ShowCreation(framebox1),)
        self.wait()

        #Animación: Se muestra el framebox2 y se guarda un tiempo de espera
        self.play(ReplacementTransform(framebox1,framebox2),)
        self.wait()