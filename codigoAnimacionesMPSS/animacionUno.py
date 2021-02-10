from manim import *

#Se configura un fondo de color gris claro
config.background_color = LIGHT_GRAY


class animacionUno(Scene):
    def construct(self):

    ##### Objetos textos #####

        #Se crean objetos de texto
        t1 = Text('Supongamos que existen 7 bolas', color=BLACK).scale(0.75).shift(DOWN*3)
        t2 = Text('Y se dividen en colores', color=BLACK).scale(0.75).shift(DOWN*3)
        t3 = Text('3 naranjas', color=BLACK).scale(0.75).shift(DOWN*3)
        t4 = Text('3 azules', color=BLACK).scale(0.75).shift(DOWN*3)
        t5 = Text(' y 1 blanca', color=BLACK).scale(0.75).shift(DOWN*3)
        t6 = Text('Si guardamos las 7 bolas en un caja', color=BLACK).scale(0.75).shift(DOWN*3)
 
        t7 = Text('¿Cuál es la probabilidad de sacar una bola blanca?', color=BLACK).scale(0.75).shift(DOWN*3)
        t8 = Text('Por la definción de probabilidad estadística: ', color=BLACK).scale(0.75).shift(UP*3, RIGHT*1)
        t9 = Text('Donde:', color=BLACK).scale(0.75).shift(DOWN)

        t10 = Text('n(A): Es el número ocurrencias', color=BLACK).scale(0.75).shift(DOWN*2)
        t11 = Text('n: Es el número total de pruebas', color=BLACK).scale(0.75).shift(DOWN*3)
        t12 = Text('En particular, para encontrar la bola blanca', color=BLACK).scale(0.75).shift(UP*3, RIGHT*1)

        t13 = Text('El numero de ocurrencias para una bola blanca es 1', color=BLACK).scale(0.75).shift(DOWN*2)
        t14 = Text('El numero de total experimentos es la cantidad de bolas, 7', color=BLACK).scale(0.75).shift(DOWN*3)
        t15 = Text('Entonces, para sacar una bola blanca:', color=BLACK).scale(0.75).shift(UP*3)
        
        #Objetos Ecuaciones
        eq1=TextMobject("$P(A) = \\lim_{n\\rightarrow \\infty} \\frac{n(A)}{n}$")
        eq2=TextMobject("$P(A) = \\frac{1}{7}$").scale(1.5)
        

        ############ Objetos círculos ######################

        #Creación de los círculos, a escala y con color 
        # (Representando la cantidad de bolas)
        
        circle1 = Circle()                  
        circle1.set_fill(RED, opacity=1).scale(0.3)
        circle1.shift(RIGHT*6)
        
        circle2 = Circle()                  
        circle2.set_fill(RED, opacity=1).scale(0.3)
        circle2.shift(RIGHT*4)
        
        circle3 = Circle()                  
        circle3.set_fill(RED, opacity=1).scale(0.3)
        circle3.shift(RIGHT*2)
        
        circle4 = Circle()                  
        circle4.set_fill(DARK_BLUE, opacity=1).scale(0.3)
        
        circle5 = Circle()                  
        circle5.set_fill(DARK_BLUE, opacity=1).scale(0.3)
        circle5.shift(LEFT*2)
        
        circle6 = Circle()                  
        circle6.set_fill(DARK_BLUE, opacity=1).scale(0.3)
        circle6.shift(LEFT*4)
        
        circle7 = Circle()                  
        circle7.set_fill(WHITE, opacity=1).scale(0.3)
        circle7.shift(LEFT*6)

        #Creación de la caja
        caja = Square(color=BLACK, fill_opacity=0).shift(UP)

        ######################################################
        # Animaciones:
        ######################################################

        #Texto: Supongamos que existen 7 bolas
        self.play(Write(t1))
            
        # Aparecen las bolas
        self.play(ShowCreation(circle1))     # Muesta circle1 en pantalla
        self.play(ShowCreation(circle2))     # Muesta circle2 en pantalla
        self.play(ShowCreation(circle3))     # Muesta circle3 en pantalla
        self.play(ShowCreation(circle4))     # Muesta circle4 en pantalla
        self.play(ShowCreation(circle5))     # Muesta circle5 en pantalla
        self.play(ShowCreation(circle6))     # Muesta circle6 en pantalla
        self.play(ShowCreation(circle7))     # Muesta circle7 en pantalla
        
        #Texto: Y se dividen en colores
        self.play(Transform(t1,t2))
        
        #Suben los círculos 1,2 y 3
        self.play(circle1.animate.shift(UP*3.5))
        self.play(circle2.animate.shift(UP*3.5))
        self.play(circle3.animate.shift(UP*3.5))
        #Texto: 3 naranjas
        self.play(Transform(t1,t3))
        self.wait(1)

        #Suben los círculos 4,5 y 6
        self.play(circle4.animate.shift(UP*3.5))
        self.play(circle5.animate.shift(UP*3.5))
        self.play(circle6.animate.shift(UP*3.5))
        #Texto: 3 azules
        self.play(Transform(t1,t4))
        self.wait(1)
        
        #Suben círculo 7
        self.play(circle7.animate.shift(UP*3.5))
        self.play(Transform(t1,t5))
        self.wait(1)

        #Aparece la caja
        self.play(caja.animate.shift(LEFT*5))
        
        #Texto: Si guardamos las 7 bolas en una caja
        self.play(Transform(t1,t6))
        self.wait(1)

        # Todos los círculos a la caja
        self.play(circle1.animate.move_to(caja))
        self.play(circle2.animate.move_to(caja))
        self.play(circle3.animate.move_to(caja))
        self.play(circle4.animate.move_to(caja))
        self.play(circle5.animate.move_to(caja))
        self.play(circle6.animate.move_to(caja))
        self.play(circle7.animate.move_to(caja))

        #Se muestra texto: ¿Cuál es la probabilidad de sacar la bola blanca?
        self.play(Transform(t1,t7))
        self.wait(1)

        #Se muestra texto: Por la definción de probabilidad estadística: 
        self.play(Transform(t1,t8))
        self.wait(1)


        #Se muestra ecuación 1 : 
        self.play(Write(eq1))
        self.wait(1) 

        #Texto: Donde:
        self.play(Write(t9))

        #Texto: Se define n(A) y n: 
        self.play(Write(t11), Write(t10))  
        self.wait(2)

        self.play(FadeOut(t9))
        self.play(FadeOut(t10))
        self.play(FadeOut(t11))

        #Texto: En particular para encontrar la bola blanca:
        self.play(Transform(t1,t12))
        self.wait(1)

        # n(A) y n para una bola blanca    
        self.play(Write(t13), Write(t14))  
        self.wait(2)

        self.play(FadeOut(t13))
        self.play(FadeOut(t14))

        #Texto: Entonces, la probabilidad para encontrar la bola blanca es:
        self.play(Transform(t1,t15))
        self.wait(1)


        # Transformación de la ecuación 1 en la ecuación 2
        self.play(FadeOut(eq1))
        self.play(Write(eq2))
        self.wait(2)