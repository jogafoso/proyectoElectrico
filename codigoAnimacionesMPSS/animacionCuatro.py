#Se importa Manim
from manim import *
from numpy import *

#Se configura un fondo de color gris claro
config.background_color = LIGHT_GRAY

#Se crea la clase mostrarGrafico, note que se importa una escena
# de tipo GraphScene para desplegar gráficos

class animacionCuatro(GraphScene):

	#Mediante el __init__ se configura en los ejes sus divisiones,
	#  color y origen del gráfico en el espacio
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-7,
            x_max=7,
            y_min=-1,
            y_max=2,
            graph_origin=np.array([2,-0.7,0]),
            axes_color=BLACK,
            x_labeled_nums=[0,1,4],
            y_labeled_nums=[0,1]
        )

	#Se inicia el constructor
    def construct(self):

        #Se inicia la configuración de ejes 
        self.setup_axes(animate=True)

        ###### GRAFICAS
		
        #Se crea una gráfica con la función de distribución uniforme con x menor que "a" y su etiqueta
        grafica1 = self.get_graph(lambda x: 0, WHITE, x_min=0, x_max=1)
        graficaEtiqueta1 = self.get_graph_label(grafica1, label='1').shift(LEFT*4.5, UP*0.5)

		#Se crea una gráfica con la función de distribución uniforme con x entre "a" y "b", y su etiqueta
        grafica2 = self.get_graph(lambda x: ((1/3)*x)-(1/3), WHITE, x_min=1, x_max=4)
        graficaEtiqueta2 = self.get_graph_label(grafica2, label='2').shift(LEFT*3.3, DOWN*2.5)

		#Se crea una gráfica con la función de distribución uniforme con x mayor que "b", y su etiqueta
        grafica3 = self.get_graph(lambda x: 1, WHITE, x_min=4, x_max=7)
        graficaEtiqueta3 = self.get_graph_label(grafica3, label='3').shift(LEFT*1.3, UP*0.3)

        #Lineas amarillas para indicar a y b
        linea_a = self.get_vertical_line_to_graph(1, grafica1, DashedLine, color=YELLOW)
        linea_b = self.get_vertical_line_to_graph(4, grafica2, DashedLine, color=YELLOW)

        #Area bajo las curvas
        area1 = self.get_area(grafica1, 0, 1, dx_scaling=10, area_color=DARK_BLUE)
        area2 = self.get_area(grafica2, 1, 4, dx_scaling=2, area_color=DARK_BLUE)
        area3 = self.get_area(grafica3, 4, 7, dx_scaling=2, area_color=DARK_BROWN)


        ##### TEXTO

        t0 = Text('Función de distribución uniforme', color=BLACK).scale(0.6).shift(UP*3, LEFT*3)
        t1 = Text('Se da de la forma:', color=BLACK).scale(0.6).shift(UP*2, LEFT*4)    
        eq1=MathTex(" F_{X}(x)= \\left\{\\begin{matrix} 0 &  & x<a \\\ \\frac{(x-a)}{(b-a)} & si, &  a \\leq x <b \\\ 1 &  & b \\leq x\end{matrix}\\right. ", color=BLACK).scale(0.75).shift(LEFT*3, UP*1.25)
        t2 = Text('Sea a = 1 y b =4', color=BLACK).scale(0.6).shift(DOWN*0.7, LEFT*5)
        t3 = Text('El área azul muestra como aumenta la probabilidad con el aumento de x', color=BLACK).scale(0.6).shift(DOWN*3.5)
        t4 = Text('Cuando x crece, acumula la probabilidad anterior  ', color=BLACK).scale(0.6).shift(DOWN*3.5)
        t5 = Text('Hasta llegar a una probabilidad de 1 como indican los axiomas', color=BLACK).scale(0.6).shift(DOWN*3.5)
        t6 = Text('Y como también se observa en el área café', color=BLACK).scale(0.6).shift(DOWN*3.5)

 


        ####
        #Texto: Función de distribución uniforme
        self.play(Write(t0))

        #Texto: Se da de la forma:
        self.play(Write(t1))

        #Se muestra ecuacion por partes de la función de distribución uniforme
        self.play(Transform(t1,eq1))
        self.wait(3)

        #Texto: Sea a=1 y b=4:
        self.play(Write(t2))
        self.wait(2)        

        # Se muestra la gráfica1 en la escena
#        self.play(ShowCreation(grafica1), Write(graficaEtiqueta1))
        self.play(ShowCreation(grafica1))
        self.wait(1)

        # Se muestra la gráfica2 en la escena
#        self.play(ShowCreation(grafica2), Write(graficaEtiqueta2))
        self.play(ShowCreation(grafica2))
        self.wait(1)

        # Se muestra la gráfica3 en la escena
#        self.play(ShowCreation(grafica3), Write(graficaEtiqueta3))
        self.play(ShowCreation(grafica3))
        self.wait(1)

        #Se muestran lineas amarillas
        self.play(ShowCreation(linea_a))
        self.wait(1)
        self.play(ShowCreation(linea_b))
        self.wait(1)

        self.play(FadeOut(t2))

        #Se muestran las áreas bajo las curvas
        self.play(ShowCreation(area1))
        self.wait(1)
        self.play(ShowCreation(area2))
        self.wait(1)
        
        #Texto: El área azul muestra como aumenta la probabilidad con el aumento de x
        self.play(Write(t3))
        self.wait(3)

        #Texto: Cuando x crece, acumula la probabilidad anterior
        self.play(Transform(t3,t4))
        self.wait(3)
        
        #Texto: Hasta llegar a una probabilidad de 1 como indican los axiomas
        self.play(Transform(t3,t5))
        self.wait(3)

        self.play(ShowCreation(area3))
        self.wait(3)

        #Texto: Y como también se observa en el área café
        self.play(Transform(t3,t6))
        self.wait(3)

