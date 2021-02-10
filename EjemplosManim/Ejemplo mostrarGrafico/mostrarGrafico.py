#Se importa Manim
from manim import *

#Se configura un fondo de color gris claro
config.background_color = LIGHT_GRAY

#Se crea la clase mostrarGrafico, note que se importa una escena
# de tipo GraphScene para desplegar gráficos

class mostrarGrafico(GraphScene):

	#Mediante el __init__ se configura en los ejes sus divisiones,
	#  color y origen del gráfico en el espacio
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-3,
            x_max=3,
            y_min=-5,
            y_max=5,
            graph_origin=ORIGIN,
            axes_color=BLACK
        )

	#Se inicia el constructor
    def construct(self):

        #Se inicia la configuración de ejes 
        self.setup_axes(animate=True)

		#Se inicializan las funciones a graficar y sus respectivas etiquetas

		#Se crea una gráfica con la función x^{4} y su etiqueta
        grafica = self.get_graph(lambda x: x, WHITE)
        graficaEtiqueta = self.get_graph_label(grafica, label='y=x')

		#Se crea una gráfica con la función x^{4} y su etiqueta
        grafica2 = self.get_graph(lambda x: x**4, WHITE)
        graficaEtiqueta2 = self.get_graph_label(grafica2, label='y=x^{4}')

        # Se muestra la gráfica en la escena
        self.play(ShowCreation(grafica), Write(graficaEtiqueta))
        self.wait(1)

		#Trancisión: Se transforma gráfica1 en gráfica2
        self.play(Transform(grafica, grafica2), 
		Transform(graficaEtiqueta, graficaEtiqueta2))
        self.wait(1)