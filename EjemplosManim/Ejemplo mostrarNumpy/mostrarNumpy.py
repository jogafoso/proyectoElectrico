#Se importa Manim
from manim import *
from numpy import * 

#Se configura un fondo de color gris claro
config.background_color = LIGHT_GRAY

#Se crea la clase mostrarGrafico, note que se importa una escena
# de tipo GraphScene para desplegar gráficos

class mostrarNumpy(GraphScene):

	#Mediante el __init__ se configura en los ejes sus divisiones,
	#  color y origen del gráfico en el espacio
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-10,
            x_max=10,
            y_min=-6,
            y_max= 6,
            graph_origin=ORIGIN,
            axes_color=BLACK
        )

	#Se inicia el constructor
    def construct(self):

        #Se inicia la configuración de ejes 
        self.setup_axes(animate=True)

		#Se inicializan las funciones a graficar y sus respectivas etiquetas

        #Se crea una gráfica mediante NumPy con la función tangente
        grafica = self.get_graph(np.arctan, DARK_BLUE)
        graficaEtiqueta = self.get_graph_label(grafica, label='arcTan')

        #Se crea una gráfica mediante NumPy con la función seno
        grafica2 = self.get_graph(np.sin, GREEN_E)
        graficaEtiqueta2 = self.get_graph_label(grafica2, label='Sen')

        #Se crea una gráfica mediante NumPy con la función coseno
        grafica3 = self.get_graph(np.cos, RED_E)
        graficaEtiqueta3 = self.get_graph_label(grafica3, label='Cos')


        #Animación:
        # Se muestra la gráfica en la escena
        self.play(ShowCreation(grafica))
        self.wait(1)

        self.play(ShowCreation(grafica2))
        self.wait(1)

        self.play(ShowCreation(grafica3))
        self.wait(1)

        #Se muestran las etiquetas y desaparecen una por una

        self.play(Write(graficaEtiqueta))
        self.play(FadeOut(graficaEtiqueta))
        self.play(Write(graficaEtiqueta2))
        self.play(FadeOut(graficaEtiqueta2))
        self.play(Write(graficaEtiqueta3))
        self.play(FadeOut(graficaEtiqueta3))
        self.wait(1)
