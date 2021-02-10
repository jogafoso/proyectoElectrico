
from manimlib.imports import *
from manim import *
from numpy import *
from pathlib import Path

#Se configura un fondo de color gris claro
config.background_color = LIGHT_GRAY

class animacionTres(Scene):
    def construct(self):

                          ############## Objetos ############

        ### Objeto: Creación de figuras

        cuadroW = Square()                  
        cuadroW.shift(LEFT*3.5).scale(0.6)

        cuadroX = Square()                  
        cuadroX.shift(LEFT*1.5, UP*1.5).scale(0.6)

        cuadroY = Square()                  
        cuadroY.shift(RIGHT*1.5, UP*1.5).scale(0.6)

        cuadroZ = Square()                  
        cuadroZ.shift(DOWN*1).scale(0.6)


        ### Objeto: Creación de flechas
        flechaEaW = Line([-5.5, 0, 0], [-4.1, 0, 0], buff=0)
        linea0 = Line([-2.9, 0, 0], [-2.5, 0, 0], buff=0)
        linea1 = Line([-2.5, 0, 0], [-2.5, 1.5, 0], buff=0)
        linea2 = Line([-2.5, 1.5, 0], [-2.1, 1.5, 0], buff=0)
        linea3 = Line([-0.9, 1.5, 0], [0.9, 1.5, 0], buff=0)
        linea4 = Line([2.1, 1.5, 0], [2.9, 1.5, 0], buff=0)        
        linea5 = Line([2.9, 1.5, 0], [2.9, 0, 0], buff=0)
        linea6 = Line([2.9, 0, 0], [4, 0, 0], buff=0)
        linea7 = Line([-2.5, 0, 0], [-2.5, -0.9, 0], buff=0)
        linea8 = Line([-2.5, -0.9, 0], [-0.6, -0.9, 0], buff=0)
        linea9 = Line([0.6, -0.9, 0], [2.9, -0.9, 0], buff=0)
        linea10 = Line([2.9, -0.9, 0], [2.9, 0, 0], buff=0)
        
        ### Objeto: Textos

        #Se crean objetos de texto y/o ecuaciones
        t0 = Text('Teorema de Bayes', color=BLACK).scale(0.85)
        t1 = Text('Ejemplo de subsistemas electrónicos', color=BLACK).scale(0.85)
        t2 = Text('Se tiene el siguiente subsistema electrónico ', color=BLACK).scale(0.85)

        tE = Text('E', color=BLACK).scale(0.85) 
        tW = Text('W', color=BLACK).scale(0.85)
        tX = Text('X', color=BLACK).scale(0.85)
        tY = Text('Y', color=BLACK).scale(0.85)
        tZ = Text('Z', color=BLACK).scale(0.85)
        tS = Text('S', color=BLACK).scale(0.85)

        t3 = Text('Las letras W, X, Y y Z operan de forma independiente', color=BLACK).scale(0.6).shift(DOWN*3)
        t4 = Text('W, X, Y y Z, cada una tiene su probabilidad de funcionamiento exitoso ', color=BLACK).scale(0.6).shift(DOWN*3)
        t4a = Text('El sistema funciona cuando hay un camino funcional entre E y S', color=BLACK).scale(0.6).shift(DOWN*3)

        t5 = Text('Se van a analizar 4 casos en el subsistema:', color=BLACK).scale(0.6)

                    ##### Caso 1 #####
        t6 = Text('Caso 1:', color=BLACK).scale(0.6).shift(UP*3.5)
        t7 = Text('Si P(Y)=0, ¿Cuál es la probabilidad P(C) de que el sistema funcione correctamente?', color=BLACK).scale(0.5).shift(UP*3.5)

        t8 = Text('El único camino funcional pasa a través de Z', color=BLACK).scale(0.6).shift(DOWN*3)
        t9 = Text('Entonces la probabilidad de éxito vendría dada por:', color=BLACK).scale(0.6).shift(DOWN*3)

        eqParte1a=MathTex("P(C) = P(W \cap Z)", color=BLACK).scale(1).shift(DOWN*3)

        t10 = Text('Y al operar cada evento de forma independiente:', color=BLACK).scale(0.6).shift(DOWN*3)
        eqParte1b=MathTex("P(W \cap Z) = P(W) P(Z)", color=BLACK).scale(1).shift(DOWN*3)
        
                    ##### Caso 2 #####
    
        t11 = Text('Caso 2:', color=BLACK).scale(0.6).shift(UP*3.5)
        t12 = Text(' Si P(W) = 1 y P(Y)>0, ¿Cuál es la probabilidad de que el sistema funcione correctamente? ', color=BLACK).scale(0.5).shift(UP*3.5)
        t13 = Text('El camino puede darse a través de  WXY y WZ, por lo tanto:', color=BLACK).scale(0.6).shift(DOWN*3)
        eqParte2a=MathTex("P(C) = P(Z \cup (X \cap Y ))", color=BLACK).scale(1).shift(DOWN*3)
        
        t14 = Text('Aplicando el teorema de Morgan, se tiene finalmente que:', color=BLACK).scale(0.6).shift(DOWN*3)
        eqParte2b=MathTex("P(C) = 1 - \left [ 1 - P(Z) \\right ]\\left [ 1 -P(X)P(Y) \\right ]", color=BLACK).scale(1).shift(DOWN*3)

                    ##### Caso 3 #####

        t15 = Text('Caso 3:', color=BLACK).scale(0.6).shift(UP*3.5)
        t16 = Text(' Si ahora:  0 < P(W),P(X),P(Y),P(Z)<1 ', color=BLACK).scale(0.5).shift(UP*3.5)
        t17 = Text('¿Cuál es la probabilidad de que el sistema funcione correctamente?', color=BLACK).scale(0.5).shift(UP*3)
        t17a = Text('El camino puede darse a través de WZ y WXY', color=BLACK).scale(0.5).shift(DOWN*3)
        t18 = Text(' Considerando que W está “en serie” con el subsistema “en paralelo” de X, Y y Z ', color=BLACK).scale(0.5).shift(DOWN*3)
        eqParte3a=MathTex(' P(C) = P(W) P(Z \cup  (X \cap Y) ) ', color=BLACK).scale(1).shift(DOWN*3)
        eqParte3b=MathTex(' P(C) = P(W) \\left \\{ 1-\\left [ 1- P(Z) \\right ]  \\left [ 1 - P(X)P(Y) \\right ] \\right \} ', color=BLACK).scale(1).shift(DOWN*3)

        t19 = Text('Lo cual entonces es equivalente a: ', color=BLACK).scale(0.5).shift(DOWN*3)
       
                    ##### Caso 4 #####
        t19a = Text('Caso 4:', color=BLACK).scale(0.6).shift(UP*3.5)
        t20 = Text('Para las probabilidades P(W) = 0,90, P(X) = 0,95, P(Y) = 0,90 y P(Z) = 0,85', color=BLACK).scale(0.5).shift(UP*3.5)
        t21 = Text('¿Cuál es la probabilidad de éxito anterior?', color=BLACK).scale(0.5).shift(UP*3)

        t22 = Text(' De la ecuación anterior obtenida en el caso 3: ', color=BLACK).scale(0.5).shift(DOWN*3)
        t23 = Text(' Utilizando los valores de probabilidad dados: ', color=BLACK).scale(0.5).shift(DOWN*3)
        eqParte4a=MathTex(' P(C) = (0.90) \\left \\{ 1-\\left [ 1- (0.85) \\right ]  \\left [ 1 - (0.95)(0.90) \\right ] \\right \\} ', color=BLACK).scale(1).shift(DOWN*3)

        t24 = Text(' Por lo tanto, la probabiliad de exito con los valores dados es: ', color=BLACK).scale(0.5).shift(DOWN*3)
        eqParte4b=MathTex(' P(C) = 0.880425 = 88 \\% ', color=BLACK).scale(1).shift(DOWN*3)

        #######    Animaciones    ########

        #Texto: Ejemplo de subsistemas electrónicos
        self.play(Write(t1))
        self.wait() 
        self.play(FadeOut(t1))

        #Texto: Se tiene el siguiente sistema electrónico
        self.play(t2.animate.shift(UP*3.5))
        self.wait()

        # Se muestran las figuras y uniones que conforman el sistema
        
        self.play(ShowCreation(flechaEaW))
        self.play(ShowCreation(cuadroW))     # Muesta cuadroW en pantalla
        self.play(ShowCreation(linea0))
        self.play(ShowCreation(linea1))
        self.play(ShowCreation(linea2))           

        self.play(ShowCreation(cuadroX))     # Muesta cuadroX en pantalla
        self.play(ShowCreation(linea3))

        self.play(ShowCreation(cuadroY))     # Muesta cuadroY en pantalla
        self.play(ShowCreation(linea4)) 
        self.play(ShowCreation(linea5))        
        self.play(ShowCreation(linea6))

        self.play(ShowCreation(cuadroZ))     # Muesta cuadroZ en pantalla
        self.play(ShowCreation(linea7))
        self.play(ShowCreation(linea8))
        self.play(ShowCreation(linea9))
        self.play(ShowCreation(linea10))

        #Se muestran y colocan las letras de cada parte del subsistema
        self.play(tE.animate.move_to(flechaEaW).shift(LEFT*1.2))
        self.play(tW.animate.move_to(cuadroW))
        self.play(tX.animate.move_to(cuadroX))
        self.play(tY.animate.move_to(cuadroY))
        self.play(tZ.animate.move_to(cuadroZ))
        self.play(tS.animate.move_to(linea6).shift(RIGHT*1))
        self.wait(1)

        #Texto: Las letras X, Y y Z operan de forma independiente
        self.play(FadeOut(t2))
        self.play(Write(t3))
        self.wait(3)

        #Texto: X, Y y Z, tienen una probabilidad de funcionamiento exitoso
        self.play(Transform(t3,t4))
        self.wait(3)

        #Texto: El sistema funciona cuando hay un camino funcional entre E y S
        self.play(Transform(t3,t4a))
        self.wait(3)
        self.play(FadeOut(t3))

        #Texto: Se van a analizar 4 casos en el subsistema
        self.play(t5.animate.shift(UP*3.5))
        self.wait(3)
    
                    ####### CASO 1 ####### 

        #Texto: Caso 1:
        self.play(Transform(t5,t6))
        self.wait(2)

        #Texto: Si P(Y)=0, ¿Cuál es la probabilidad de que el sistema funcione correctamente?
        self.play(Transform(t5,t7))
        self.wait(2)

        #Cuadro Y se pone en rojo
        cuadroY.set_fill(RED, opacity=1)

        #Texto: El único camino funcional pasa a través de Z
        self.play(ShowCreation(t8))
        self.wait(2)

        #Cuadro Z se pone en azul
        cuadroZ.set_fill(BLUE, opacity=1)
        self.wait(2)

        #Texto: Entonces la probabilidad de éxito vendría dada por:
        self.play(Transform(t8,t9))
        self.wait(2)

        #Se muestra ecuación eqParte1a
        self.play(Transform(t8,eqParte1a))
        self.wait(2)

        #Texto: Y al operar cada evento de forma independiente
        self.play(Transform(t8,t10))
        self.wait(2)

        #Se muestra ecuación eqParte1b
        self.play(Transform(t8,eqParte1b))
        self.wait(2)

        #Se eliminan los textos y colores de cuadros para entrar a caso 2:
        cuadroY.set_fill(RED, opacity=0)
        cuadroZ.set_fill(RED, opacity=0)        
        self.play(FadeOut(t8))
        self.play(FadeOut(t5))

                    ####### CASO 2 ####### 

        #Texto: Caso 2:
        self.play(Write(t11))
        self.wait(2)

        #Texto: Si P(W) = 1 y P(Y)>0, ¿Cuál es la probabilidad de que el sistema funcione correctamente?
        self.play(Transform(t11,t12))
        self.wait(3)

        #Cuadro W se pone en verde
        cuadroW.set_fill(GREEN, opacity=1)
        self.wait(2)

        #Texto: El camino puede darse a través de WXY y WZ
        self.play(ShowCreation(t13))
        self.wait(3)

        #Cuadro X, Y y Z se ponen en azul
        cuadroX.set_fill(BLUE, opacity=1)
        cuadroY.set_fill(BLUE, opacity=1)
        cuadroZ.set_fill(BLUE, opacity=1)
        self.wait(2)

        # Se muestra la ecuación de la parte 2
        self.play(Transform(t13,eqParte2a))
        self.wait(3)

        #Texto: Aplicando el teorema de Morgan, se tiene finalmente que:
        self.play(Transform(t13,t14))
        self.wait(3)

        # Se muestra la ecuación de la parte 2
        self.play(Transform(t13,eqParte2b))
        self.wait(3)

        #Se eliminan los textos y colores de cuadros para entrar a caso 3:
        cuadroW.set_fill(RED, opacity=0)
        cuadroX.set_fill(RED, opacity=0)
        cuadroY.set_fill(RED, opacity=0)
        cuadroZ.set_fill(RED, opacity=0)        
        self.play(FadeOut(t11))
        self.play(FadeOut(t13))

                    ####### CASO 3 ####### 

        #Texto: Caso 3:
        self.play(Write(t15))
        self.wait(2)
        
        #Texto: Si ahora 0 < P(W),P(X),P(Y),P(Z)<1 
        self.play(Transform(t15,t16))
        #Texto: ¿Cuál es la probabilidad de que el sistema funcione correctamente?
        self.play(Write(t17))
        self.wait(2)


        #Texto: El camino puede darse a través de WZ y WXY
        self.play(Write(t17a))
        self.wait(2)

        #Cuadro X, Y y Z se ponen en azul 
        cuadroW.set_fill(BLUE, opacity=1)
        cuadroX.set_fill(BLUE, opacity=1)
        cuadroY.set_fill(BLUE, opacity=1)
        cuadroZ.set_fill(BLUE, opacity=1)
        self.wait(2)


        #Texto:Considerando que W está “en serie” con el subsistema “en paralelo” de X, Y y Z 
        self.play(Transform(t17a,t18))
        self.wait(3)

        # Se muestra la ecuación de la parte 3A
        self.play(Transform(t17a,eqParte3a))
        self.wait(3)

        # Texto: Lo cual es equivalente entonces es equivalente a:
        self.play(Transform(t17a,t19))
        self.wait(3)

        # Se muestra la ecuación de la parte 3B
        self.play(Transform(t17a,eqParte3b))
        self.wait(3)
        
        #Se eliminan los textos y colores de cuadros para entrar a caso 3:
        cuadroW.set_fill(RED, opacity=0)
        cuadroX.set_fill(RED, opacity=0)
        cuadroY.set_fill(RED, opacity=0)
        cuadroZ.set_fill(RED, opacity=0)        
        self.play(FadeOut(t15))
        self.play(FadeOut(t17))
        self.play(FadeOut(t17a))


                    ####### CASO 4 ####### 
        
        #Texto: Caso 4:
        self.play(Write(t19a))
        self.wait(2)

        #Texto: Para las probabilidades P(W) = 0,90, P(X) = 0,95, P(Y) = 0,90 y P(Z) = 0,85, ¿cuál es la probabilidad anterior?
        self.play(Transform(t19a,t20))
        self.wait(2)
        #Texto: ¿Cuál es la probabilidad anterior?
        self.play(Write(t21))
        self.wait(2)

        #Texto: De la ecuación anterior obtenida en el caso 3:
        self.play(Write(t22))
        self.wait(3)

        #Texto: Se muestra ecuacion del caso 3 simplificada
        self.play(Transform(t22,eqParte3b))
        self.wait(3)

        #Texto: Utilizando los valores de probabilidad dados:
        self.play(Transform(t22,t23))
        self.wait(3)

        #Se muestran los valores de probabilidad del enunciado en la fórmula
        self.play(Transform(t22,eqParte4a))
        self.wait(3)

        #Se muestra ecuación P(C) = 0.880425 = 88 \\%:
        self.play(Transform(t22,eqParte4b))
        self.wait(3)



