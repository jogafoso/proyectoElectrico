
from manimlib.imports import *
from manim import *
from numpy import *
from pathlib import Path

#Se configura un fondo de color gris claro
config.background_color = LIGHT_GRAY

class animacionDoss(Scene):
    def construct(self):

        ############## Objetos ############

        ### Objeto: Creación de flechas
        curvedArrow1=CurvedArrow(start_point=np.array([-4.5,0,0]),end_point=np.array([-1,-3,0]))
        Arrow2 = Arrow([-4.5, 0, 0], [-1, 0, 0], buff=0)
        curvedArrow3=CurvedArrow(start_point=np.array([-4.5,0,0]),end_point=np.array([-1,2.5,0]), angle= -TAU/4)

        Arrow4a = Arrow([-1, 2.5, 0], [2.5, 3.5, 0], buff=0)
        Arrow4b = Arrow([-1, 2.5, 0], [2.5, 2, 0], buff=0)

        Arrow5a = Arrow([-1, 0, 0], [2.5, 0.7, 0], buff=0)
        Arrow5b = Arrow([-1, 0, 0], [2.5, -0.7, 0], buff=0)

        Arrow6a = Arrow([-1, -3, 0], [2.5, -2, 0], buff=0)
        Arrow6b = Arrow([-1, -3, 0], [2.5, -3.5, 0], buff=0)

         ### Objeto: Textos

        #Se crean objetos de texto
        t0 = Text('Teorema de Bayes', color=BLACK).scale(0.85)
        t1 = Text('Se tiene una enfermedad en una determinada población', color=BLACK).scale(0.6).shift(UP*3)
        t1a = Text('Y puede presentar 3 estados:', color=BLACK).scale(0.6).shift(UP*3)

        t2 = Text('Evento A: Enfermo, con una probabilidad del 70%', color=BLACK).scale(0.6).shift(UP)
        t3 = Text('Evento B: Contagiado, con una probabilidad del 20%', color=BLACK).scale(0.6)
        t4 = Text('Evento C: No enfermo, con una probablidad del 10%', color=BLACK).scale(0.6).shift(DOWN)

        t5 = Text('Además, si se realiza una prueba médica ', color=BLACK).scale(0.6).shift(UP*3)
        t5a = Text('para determinar si el sujeto se encuentra enfermo', color=BLACK).scale(0.6).shift(UP*3)
 
        t6 = Text('existe una probabilidad de error en la prueba' , color=BLACK).scale(0.6).shift(UP*3)
        t7 = Text('Si está enfermo, la probabilidad de error es del 1%', color=BLACK).scale(0.6).shift(UP)
        t8 = Text('Si se está incubando, la probabilidad de error es del 10%', color=BLACK).scale(0.6)
        t9 = Text('Si no se está enfermo, la probabilidad de error es del 5%', color=BLACK).scale(0.6).shift(DOWN)

        t10 = Text('Mediante un esquema, se puede observar de la siguiente forma', color=BLACK).scale(0.6)
        
        t11 = Text('Evento A: Enfermo P(A)=70%', color=BLACK).scale(0.6).shift(LEFT*4, UP*3)
        t12 = Text('Evento B: Incubando P(B)=20%', color=BLACK).scale(0.6).shift(LEFT*4, DOWN*0.5)
        t13 = Text('Evento C: No enfermo P(C)=10%', color=BLACK).scale(0.6).shift(LEFT*4, DOWN*3.5)


        t11a = MathTex("P(A)=70\\%", color=BLACK).scale(0.75).shift(LEFT*4, UP*2.5)
        t12a = MathTex("P(B)=20\\%", color=BLACK).scale(0.75).shift(LEFT*5.5)
        t13a = MathTex("P(C)=10\\%", color=BLACK).scale(0.75).shift(LEFT*4, DOWN*3.5)

        
        t14 = Text('Sea P(D) la probabilidad de error en la prueba', color=BLACK).scale(0.6).shift(LEFT*3, UP*3.5)
        t15 = MathTex("P(D|A) = 1\\%", color=BLACK).scale(0.75).shift(RIGHT*4, UP*3.5)
        t16 = MathTex("P(D|B) = 10\\%", color=BLACK).scale(0.75).shift(RIGHT*4, UP*0.7)
        t17 = MathTex("P(D|C) = 5\\%", color=BLACK).scale(0.75).shift(RIGHT*4, DOWN*2)

        eqt15=MathTex("\\overline{P(D|A)} = 99\\%", color=BLACK).scale(0.75).shift(RIGHT*4, UP*2)
        eqt16=MathTex("\\overline{P(D|B)} = 90\\%", color=BLACK).scale(0.75).shift(RIGHT*4, UP*-0.7)
        eqt17=MathTex("\\overline{P(D|C)} = 95\\%", color=BLACK).scale(0.75).shift(RIGHT*4, DOWN*3.5)

        t15new = MathTex("P(D|A) = 1\\%", color=BLACK).scale(0.75).shift(RIGHT*5, UP*3.5)
        t16new = MathTex("P(D|B) = 10\\%", color=BLACK).scale(0.75).shift(RIGHT*5, UP*3)
        t17new = MathTex("P(D|C) = 5\\%", color=BLACK).scale(0.75).shift(RIGHT*5, UP*2.5)

        t11new = MathTex("P(A)=70\\%", color=BLACK).scale(0.75).shift(RIGHT*5, UP*2)
        t12new = MathTex("P(B)=20\\%", color=BLACK).scale(0.75).shift(RIGHT*5, UP*1.5)
        t13new = MathTex("P(C)=10\\%", color=BLACK).scale(0.75).shift(RIGHT*5, UP*1)

        t18 = Text('¿Cuál es la probabilidad de que exista un error en una persona no enferma?', color=BLACK).scale(0.6)
        t19 = Text('Por el teorema de Bayes:', color=BLACK).scale(0.6)

        eqBayes=MathTex("P(B_{N} \\mid A) = \\frac{P(A \\mid B_{N})P(B_{N})}{P(A \\mid B_{1})P(B_{1})+ ... + P(A \\mid B_{N})P(B_{N}) }", color=BLACK).scale(0.75)
        t20 = Text('Se calcula P(D|C):', color=BLACK).scale(0.6)
        t21 = Text('El evento que quiero que suceda, dividido entre todos los eventos posibles:', color=BLACK).scale(0.5)
        t22 = Text('Probabilidad de error siendo no enfermo, dividido entre todas las probabilidades', color=BLACK).scale(0.5)
        eqC=MathTex("P(C \\mid D) = \\frac{P(D \\mid C)P(C)}{P(D \\mid A)P(A)  +  P(D \\mid B)P(B) + P(D \\mid C)P(C) }", color=BLACK).scale(0.75).shift(DOWN*1)
        eqCdespejada=MathTex(" P(Error \\mid No \\: Enfermo) = \\frac{(0.05) (0.1)}{(0.01)(0.7)  +  (0.1) (0.2) + (0.1)(0.05) } ", color=BLACK).scale(0.75).shift(DOWN*1)
        tfinal = Text('Por lo tanto, la probabilidad es:', color=BLACK).scale(0.6).shift(DOWN*1)
        resultadoFinal=MathTex(" P(Error \mid No \\: Enfermo) = 0.15625 ", color=BLACK).scale(0.75).shift(DOWN*1)
        

        #######    Animaciones    ########

        #Texto: Teorema de Bayes
        self.play(Write(t0))
        self.wait()

        #Texto: Se tiene una enfermedad en una determinada población
        self.play(Transform(t0,t1))
        self.wait(3)
        self.play(Transform(t0,t1a))
        self.wait(3)

        #Texto: Eventos A, B y C
        self.play(Write(t2))
        self.play(Write(t3)) 
        self.play(Write(t4))
        self.wait(3)

        self.play(FadeOut(t2))
        self.play(FadeOut(t3))
        self.play(FadeOut(t4))

        #Texto:Además se realiza una prueba médica
        self.play(Transform(t0,t5))
        self.wait(1)

        #Texto: Existe una probabilidad de error en la prueba
        self.play(Transform(t0,t5a))
        self.wait(1)


        #Texto: La probabilidad que la prueba se equivoque varía
        self.play(Transform(t0,t6))
        self.wait(3)

        #Texto: Se muestran las probabilidades de error
        self.play(Write(t7))
        self.play(Write(t8))
        self.play(Write(t9))
        self.wait(3)

        #Desaparecen los textos
        self.play(FadeOut(t6))
        self.play(FadeOut(t7))
        self.play(FadeOut(t8))
        self.play(FadeOut(t9))
        self.play(FadeOut(t0))

        #Texto: Mediante un esquema, se puede observar así
        self.play(Write(t10))
        self.play(FadeOut(t10))

 
        #Se muestran las primera tres flechas
        self.play(ShowCreation(curvedArrow1))
        self.play(ShowCreation(Arrow2))
        self.play(ShowCreation(curvedArrow3))

        #Texto:
        # Evento A: Enfermo P(A)=70%
        # Evento B: Enfermo P(B)=20%
        # Evento C: Enfermo P(C)=10%
        self.play(Write(t11))
        self.play(Write(t12))
        self.play(Write(t13))

        #Texto:
        # P(A)=70%
        # P(B)=20%
        # P(C)=10%
        self.play(Transform(t11, t11a))
        self.play(Transform(t12, t12a))
        self.play(Transform(t13, t13a))

        #Texto: Sea P(D) la probabilidad de error:
        self.play(Write(t14))
        self.play(FadeOut(t14))
  
        #Se muestran las flechas para el evento D a partir de A
        self.play(ShowCreation(Arrow4a))
        self.play(ShowCreation(Arrow4b))
        self.play(Write(t15))
        self.play(Write(eqt15))

        #Texto: Se muestran los P(D)

        #Se muestran las flechas para el evento D a partir de B
        self.play(ShowCreation(Arrow5a))
        self.play(ShowCreation(Arrow5b))
        #Texto: Se muestran los P(D)
        self.play(Write(t16))
        self.play(Write(eqt16))

        #Se muestran las flechas para el evento D a partir de C
        self.play(ShowCreation(Arrow6a))
        self.play(ShowCreation(Arrow6b))
        #Texto: Se muestran los P(D)
        self.play(Write(t17))
        self.play(Write(eqt17))


        #Se borra diagrama y titulos, y se colocan probabilidades a la derecha

        self.play(FadeOut(Arrow4a))
        self.play(FadeOut(Arrow4b))
        self.play(FadeOut(eqt15))

        self.play(FadeOut(Arrow5a))
        self.play(FadeOut(Arrow5b))
        self.play(FadeOut(eqt16))

        self.play(FadeOut(Arrow6a))
        self.play(FadeOut(Arrow6b))
        self.play(FadeOut(eqt17))

        self.play(FadeOut(curvedArrow1))
        self.play(FadeOut(Arrow2))
        self.play(FadeOut(curvedArrow3))

        self.play(Transform(t15, t15new))
        self.play(Transform(t16, t16new))
        self.play(Transform(t17, t17new))

        self.play(Transform(t11, t11new))
        self.play(Transform(t12, t12new))
        self.play(Transform(t13, t13new))

        #Texto: ¿Cuál es la probabilidad de que exista un error en una persona no enferma?
        self.play(Write(t18))
        self.wait(2)
        #Texto: Por el teorema de Bayes: 
        self.play(Transform(t18,t19))
        self.wait(1)

        #Se muestra la ecuación de Bayes
        self.play(Transform(t18,eqBayes))
        #Se dirige a la parte inferior la ecuación de Bayes
        self.play(t18.animate.shift(DOWN*3))
        
        #Texto:Se calcula P(D|C) 
        self.play(Write(t20))
        self.wait(1)
        
        #El evento que quiero que suceda, dividido entre
        #todos los eventos posibles:
        self.play(Transform(t20,t21))
        self.wait(3)
        
        #Texto: Probabilidad de haber un error estando no enfermo,
        #dividido entre todas las probabilidades
        self.play(Transform(t20,t22))
        self.wait(3)
        self.play(FadeOut(t18))
        
        #Se muestra ecuación de Bayes aplicada al ejercicio
        self.play(Transform(t20,eqC))
        self.wait(3)

        #Se muestra los valores sustituidos
        self.play(Transform(t20,eqCdespejada))
        self.wait(4)

        #Texto: Se muestra el resultado final
        self.play(Transform(t20,tfinal))
        self.wait(4)

        #Se muestra el resultado final
        self.play(Transform(t20,resultadoFinal))
        self.wait(4)