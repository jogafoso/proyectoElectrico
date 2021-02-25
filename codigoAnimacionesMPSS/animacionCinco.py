#Se importa Manim y Numpy
from manim import *
from numpy import *

#Se configura un fondo de color gris claro
config.background_color = LIGHT_GRAY

#Se crea la clase mostrarGrafico, note que se importa una escena
# de tipo GraphScene para desplegar gráficos

class animacionCinco(GraphScene):

	#Mediante el __init__ se configura en los ejes sus divisiones,
	#  color y origen del gráfico en el espacio
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_axis_label=r"$F_{X}(x)$",
            x_axis_label=r"$x$",
            x_min=-2,
            x_max=71,
            y_min=-0.5,
            y_max=2,
            graph_origin=np.array([-6,-2.5,0]),
            axes_color=BLACK,
            y_labeled_nums=np.arange(0, 2, 1),
            x_labeled_nums=np.arange(0, 71, 10)
        )

	#Se inicia el constructor
    def construct(self):

        #Se inicia la configuración de ejes 
        self.setup_axes(animate=True)

        ###### GRAFICAS
		
        #Se crea una gráfica con la función de distribución uniforme con x menor que "a" y su etiqueta
        grafica1 = self.get_graph(lambda x: (1-exp((-(x**2))/(800))), WHITE, x_min=0, x_max=70)

        #Lineas amarillas para indicar 10m y 50m
        linea_10 = self.get_vertical_line_to_graph(10, grafica1, DashedLine, color=YELLOW)
        linea_50 = self.get_vertical_line_to_graph(50, grafica1, DashedLine, color=YELLOW)
        lineaY10 = DashedLine(start=[-6, -2.25, 0], end=linea_10, buff=0,)
        lineaY50 = DashedLine(start=[-6, -0.25, 0], end=linea_50, buff=0,)

        #Area bajo las curvas
        area = self.get_area(grafica1, 0, 70, dx_scaling=0.1, area_color=DARK_BLUE)


        ##### Objetos círculo

        #Animación caída paracaídista
        circulo = Circle(radius=1.25, color=BLACK).shift(RIGHT*3, UP*1)
        punto = Dot()
        circulo2 = Circle(radius=0.3, color=RED, fill_opacity=1).shift(RIGHT*3, UP*1)

        
        ##### TEXTO

        t0 = Text('Ejemplo de un paracaídista', color=BLACK).scale(0.6).shift(UP*3, RIGHT*3)
        t1 = Text('Se tiene la zona de aterrizaje ', color=BLACK).scale(0.6).shift(DOWN*1, RIGHT*2.75)
        t1a = Text('dada por la distribución de Rayleigh', color=BLACK).scale(0.6).shift(DOWN*1, RIGHT*2.75)
        t2 = Text('Y se señala que:', color=BLACK).scale(0.6).shift(DOWN*1, RIGHT*2.75)
        b = MathTex(" b = 800 m^{2}", color=BLACK).scale(0.6).shift(DOWN*1, RIGHT*2.75).scale(1.5)
        t3 = Text('El blanco tiene un radio de 50m', color=BLACK).scale(0.6).shift(DOWN*1, RIGHT*2.75)
        t4 = Text('Con un ojo de buey de 10m', color=BLACK).scale(0.6).shift(DOWN*1, RIGHT*2.75)
        a = MathTex(" a = 0", color=BLACK).scale(0.6).shift(DOWN*1, RIGHT*2.75).scale(1.5)
        t5 = Text('Según la función de distribución de Rayleigh:', color=BLACK).scale(0.6).shift(UP*3, RIGHT*1.5)
        t6 = Text('P(Caer en ojo) = 0.12', color=BLACK).scale(0.5).shift(UP*2, RIGHT*3)
        t7 = Text('P(Caer en el blanco) = 0.96', color=BLACK).scale(0.5).shift(UP*1, RIGHT*3)
        eqRay=MathTex(" F_{X}(x)=\\begin{Bmatrix} 1 - exp\\left ( -\\frac{x^{2}}{2\\sigma ^{2}} \\right ) & x\\geq 0 \\\ 0 & x < 0 \\end{Bmatrix} ", color=BLACK).scale(0.75).shift(RIGHT*3, UP*1.5)
        eqRayDesp=MathTex(" F_{X}(x)=\\begin{Bmatrix} 1 - exp\\left ( -\\frac{x^{2}}{800 } \\right ) & x\\geq 0 \\\ 0 & x < 0 \\end{Bmatrix} ", color=BLACK).scale(0.75).shift(RIGHT*3, UP*1.5)

        fx10 = Text('0.12', color=BLACK)
        fx50 = Text('0.96', color=BLACK)

        t8 = Text('P(Dar en el ojo de buey | aterrizaje da en el blanco)', color=BLACK).scale(0.7).shift(UP*3)
        eq9 = MathTex("P(\\{X \\leq 10\\}\\mid \\{X \\leq 50\\})", color=BLACK).scale(0.65).shift(UP*2)
        eq10 = MathTex("= \\frac{P(\\{ X \\leq 10\\} \\cap \\{X \\leq 50\})}{P(\\{X \\leq 50\\})}", color=BLACK).scale(0.65).shift(UP*1)
        eq11 = MathTex(" = \\frac{P(\\{X\\leq 10\\})}{P(\\{X\\leq 50\\})} ", color=BLACK).scale(0.65)
        eq12 = MathTex(" = \\frac{F_{X}(10)}{F_{X}(50)} ", color=BLACK).scale(0.65).shift(DOWN*1)
        eq13 = MathTex(" = \\frac{1 - e^{-100/800}}{1 - e^{-2500/800}} ", color=BLACK).scale(0.65).shift(DOWN*2)
        eq14 = MathTex(" = 0.1229 ", color=BLACK).scale(0.65).shift(DOWN*3)


        ####
        #Texto: Ejemplo de un paracaídista
        self.play(Write(t0))
        self.wait(2)        

        #Texto: Se tiene la zona de aterrizaje dada por la distribución de Rayleigh
        t1a.next_to(t1, DOWN)
        self.play(Write(t1a), Write(t1))
        self.wait(2)
        self.play(FadeOut(t1a))

        #Texto: Y se señala que:
        self.play(Transform(t1,t2))
        self.wait(2)        

        #Texto: b = 800m2:
        self.play(Transform(t1,b))
        self.wait(2)        

        #Texto: a = 0:
        self.play(Transform(t1,a))
        self.wait(2)

        #Texto: : El blanco tiene un radio de 50m
        self.play(Transform(t1,t3))
        self.wait(2)

        #Se muestra el círculo y un punto alrededor del círculo        
        self.play(GrowFromCenter(circulo))
        self.wait(2)
        self.play(MoveAlongPath(punto, circulo), run_time=3, rate_func=linear)        

        #Texto: Con un ojo de buey de 10m
        self.play(Transform(t1,t4))
        self.wait(2)

        #Se muestra el círculo2
        self.play(GrowFromCenter(circulo2))
        self.play(MoveAlongPath(punto, circulo2), run_time=3, rate_func=linear)
        self.play(FadeOut(punto))

        # Se desplazan los círculos juntos hacía la derecha  y a escala
        self.play(circulo.animate.shift(RIGHT*3, UP*2).scale(0.3), circulo2.animate.shift(RIGHT*3, UP*2).scale(0.3))
        self.play
        self.play(FadeOut(t1))

        #Texto: Según la función de distribución de Rayleigh:
        self.play(Transform(t0,t5))
        self.wait(3)

        #Se muestra la Fx(x)
        self.play(Write(eqRay))
        self.wait(2)        

        #Se muestra la Fx(x) despejada
        self.play(Transform(eqRay,eqRayDesp))
        self.wait(3)

        # Se muestra la gráfica1 en la escena
        self.play(ShowCreation(grafica1), ShowCreation(area))
        self.wait(3)

        #Se muestran lineas amarillas y blancas punteadas
        self.play(ShowCreation(linea_10))
        self.wait(1)
        self.play(ShowCreation(linea_50 ))
        self.wait(1)
        self.play(ShowCreation(lineaY10))
        self.wait(1)
        self.play(ShowCreation(lineaY50))
        self.wait(1)

        #Se muestran las probabilidades en las líneas punteadas
        fx10.next_to(lineaY10, UP).scale(0.5)
        fx50.next_to(lineaY50, UP).scale(0.5)
        self.add(fx10, fx50)
        self.wait(3)

        #Texto: P(Caer en ojo) = 0.12 y P(Caer en el blanco) = 0.96
        self.play(FadeOut(eqRay))
        self.play(Write(t7), Write(t6))
        self.wait(5)


        # Desaparecen todas las animaciones en pantalla 
#        self.play(FadeOut(eqRay, self.axes, t7, t6, fx10, fx50, linea_10, linea_50, lineaY10, lineaY50, grafica1, area, t0 ))
#        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        #Se muestra ecuacion-texto, P( \\text{Dar en el ojo de buey} \\mid \\text{aterrizaje da en el blanco} )
        self.play(Write(t8))
        self.wait(2)


        #Se muestran las ecuaciones eq9 a eq14 
        self.play(Write(eq9))
        self.wait(2)

        self.play(Write(eq10))
        self.wait(2)

        self.play(Write(eq11))
        self.wait(2)

        self.play(Write(eq12))
        self.wait(2)

        self.play(Write(eq13))
        self.wait(2)

        self.play(Write(eq14))
        self.wait(2)
