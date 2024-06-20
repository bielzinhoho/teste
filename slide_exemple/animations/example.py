from manim import *
from manim_revealjs import PresentationScene, COMPLETE_LOOP
from random import shuffle

config.video_dir = "./videos"
#manim -v WARNING --disable_caching -pqh example.py DemoScene
def piramyd(n):
    return VGroup(*[
        VGroup(*[Square() for _ in range(j)]).arrange(RIGHT,buff=0)
        for j in range(1, n+1)
    ]).arrange(DOWN,buff=0)

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
class DemoScene(PresentationScene):

    def end_fragment_loop(self):
        self.end_fragment(fragment_type=COMPLETE_LOOP)
        self.end_fragment()
    def construct(self):
        A = np.array(
            [
                [2,3,5],
                [4,1,7],
                [1,7,6]
            ]
        )

        colunas = A[:, :2]

        # Concatenar essas colunas à matriz original
        A_extended = np.hstack([A,colunas])

        matriz_A = Matrix(A,left_bracket="|",right_bracket="|").shift(2*LEFT +0.7*UP).scale(0.5)
        MARCA_AGUA = Tex("@pcoelhog").scale(0.5)
        MARCA_AGUA.shift(3*RIGHT + 1.5*DOWN)
        self.add(MARCA_AGUA)
        titulo = Tex("CALCULANDO O DETERMINANTE DE UM MATRIZ 3X3").scale(0.5)
        titulo.shift(1.7*UP)
        self.add(titulo)



        nome_matriz = MathTex(r"A = ").next_to(matriz_A).shift(2.7*LEFT ).scale(0.5)
        self.add(nome_matriz)
        duas_linhas = matriz_A.copy()
        matriz_b = Matrix(A_extended, left_bracket="|", right_bracket="|")
        matriz_b.move_to(matriz_A.get_columns()[2]).scale(0.5)

        bra = duas_linhas.get_brackets()
        bra.set_color(BLACK)
        duas_linhas.next_to(matriz_A,1.2*RIGHT)

        determinante = int(np.linalg.det(A))
        ent = matriz_A.get_entries()
        ent2 = duas_linhas.get_entries()
        ent3 = matriz_b.get_entries()

        co = duas_linhas.get_columns()

        self.add(
            matriz_A
        )

        self.end_fragment()  #################################

        self.wait()    
        E = VGroup(ent[0],ent[1],ent[3],ent[4],ent[6],ent[7])
        self.play(Indicate(E))  
        self.end_fragment()  #################################

        ent2[0].move_to(ent3[3])
        ent2[1].move_to(ent3[4])

        ent2[3].move_to(ent3[8])
        ent2[4].move_to(ent3[9])

        ent2[6].move_to(ent3[13])
        ent2[7].move_to(ent3[14])

        self.play(ent[0].copy().animate.move_to(ent2[0]),
            ent[1].copy().animate.move_to(ent2[1]),
            ent[3].copy().animate.move_to(ent2[3]),
            ent[4].copy().animate.move_to(ent2[4]),
            ent[6].copy().animate.move_to(ent2[6]),
            ent[7].copy().animate.move_to(ent2[7]),
        )

        self.end_fragment()  #################################
        
        L = Line(matriz_A[0][0].get_center(), matriz_A[0][-1].get_center())
        L.set_z_index(-1).set_stroke(color=LIGHT_PINK, opacity=.5, width=25).set_cap_style(CapStyleType.ROUND)
        L.scale(1.1)


        L1 = Line(matriz_A[0][1].get_center(), duas_linhas[0][-3].get_center())
        L1.set_z_index(-1).set_stroke(color=LIGHT_PINK, opacity=.5, width=25).set_cap_style(CapStyleType.ROUND)
        L1.scale(1.1)

        L2 = Line(matriz_A[0][2].get_center(), duas_linhas[0][-2].get_center())
        L2.set_z_index(-1).set_stroke(color=LIGHT_PINK, opacity=.5, width=25).set_cap_style(CapStyleType.ROUND)
        L2.scale(1.1)

        Linhas = VGroup(L,L1,L2)
        seq = [
            0, 1, 2
        ]

        resultados = Tex("Resultados").scale(0.5)
        resultados.shift(3*RIGHT+1.3*UP)
        self.play(Write(resultados))
        r= MathTex(rf"i").next_to(resultados,0.5*DOWN).set_color(BLACK)
        r1= MathTex(rf"i").next_to(r,0.5*DOWN).set_color(BLACK)
        r2= MathTex(rf"i").next_to(r1,0.5*DOWN).set_color(BLACK)
        self.end_fragment()  #################################
        for i  in range(3):
            index = 0
            produto = A[0][seq[0]] * A[1][seq[1]] * A[2][seq[2]]
            eq = MathTex(rF"{A[0][seq[0]]} \cdot {A[1][seq[1]]} \cdot {A[2][seq[2]]} = {produto} ").scale(0.5)
            if i == 0:
                p = MathTex(f"{A[0][seq[0]]}").move_to(ent[seq[0]]).set_color(BLUE).scale(0.5)
                p1 = MathTex(f"{A[1][seq[1]]}").move_to(ent[seq[1] + 3]).set_color(RED).scale(0.5)
                p2 = MathTex(f"{A[2][seq[2]]}").move_to(ent[seq[2] + 6]).set_color(GREEN).scale(0.5)
            elif i == 1:
                p = MathTex(f"{A[0][seq[0]]}").move_to(ent[seq[0]]).set_color(BLUE).scale(0.5)
                p1 = MathTex(f"{A[1][seq[1]]}").move_to(ent[seq[1] + 3]).set_color(RED).scale(0.5)
                p2 = MathTex(f"{A[2][seq[2]]}").move_to(ent2[seq[2] + 6]).set_color(GREEN).scale(0.5)
            elif i == 2:
                p = MathTex(f"{A[0][seq[0]]}").move_to(ent[seq[0]]).set_color(BLUE).scale(0.5)
                p1 = MathTex(f"{A[1][seq[1]]}").move_to(ent2[seq[1] + 3]).set_color(RED).scale(0.5)
                p2 = MathTex(f"{A[2][seq[2]]}").move_to(ent2[seq[2] + 6]).set_color(GREEN).scale(0.5)

            eq.next_to(matriz_A,DOWN)  
            self.play(Create(Linhas[i]))
            self.wait()

            self.play(p.animate.move_to(eq[0][index:index +len(str(p.get_tex_string()))]))
            index += len(str(p.get_tex_string())) + 1
            a = eq[0][index-1]
            self.play(Create(a))
            self.play(p1.animate.move_to(eq[0][index:index + len(str(p1.get_tex_string()))]))
            index += len(str(p1.get_tex_string())) + 1
            b = eq[0][index-1]
            self.play(Create(b))
            self.play(p2.animate.move_to(eq[0][index:index+ len(str(p2.get_tex_string()))]))
            igual = eq[0][index+len(str(p2.get_tex_string()))]
            self.play(Create(igual))
            ultimo = eq[0][index+len(str(p2.get_tex_string())) +1:].set_color(LIGHT_PINK)
            self.play(Write(ultimo))
            if i == 0:
                ultimo1 = ultimo.copy().set_color(LIGHT_PINK)
                self.play(ultimo1.set_color(LIGHT_PINK).animate.move_to(r))
            if i == 1:
                ultimo2 = ultimo.copy().set_color(LIGHT_PINK)
                self.play(ultimo2.set_color(LIGHT_PINK).animate.move_to(r1))
            if i == 2:
                ultimo3 = ultimo.copy().set_color(LIGHT_PINK)
                self.play(ultimo3.set_color(LIGHT_PINK).animate.move_to(r2))
            y = seq.pop(0)
            seq.append(y)
            self.remove(p,p1,p2,a,b,igual,ultimo)

        self.end_fragment()  #################################
        seq = [0,1,2]
        produtos = []
        resul = 0
        for i in range(3):
            produto = f"{A[0][seq[0]] * A[1][seq[1]]* A[2][seq[2]]}"
            resul += A[0][seq[0]] * A[1][seq[1]]* A[2][seq[2]]
            produtos.append(produto)
            if i ==0:
                le = len(str(A[0][seq[0]] * A[1][seq[1]]* A[2][seq[2]]))
            if i == 1:
                le1 = len(str(A[0][seq[0]] * A[1][seq[1]]* A[2][seq[2]]))
            if i == 2:
                le2 = len(str(A[0][seq[0]] * A[1][seq[1]]* A[2][seq[2]]))
            y = seq.pop(0)
            seq.append(y)
        soma_str = " + ".join(produtos)
        soma = MathTex(rf"{soma_str} = {resul}").scale(0.5)
        soma.shift(2*LEFT + DOWN )


    
        index = 0
        P = Tex("Somando os resultados:").scale(0.5)
        P.shift(2*LEFT,0.5*DOWN)
        self.play(Write(P))
        for i in range(3):
            if i == 0:
                self.play(ultimo1.animate.move_to(soma[0][index:index + le]))
                index += le +1
                self.play(Create(soma[0][index-1]))
            if i == 1:
                self.play(ultimo2.animate.move_to(soma[0][index:index + le1]))
                index += le1 +1
                self.play(Create(soma[0][index-1]))
            if i == 2:
                self.play(ultimo3.animate.move_to(soma[0][index:index + le2]))
                self.play(Write(soma[0][index + le2:index + le2+1]))
                self.play(Write(soma[0][index + le2+1:].set_color(LIGHT_PINK)))
                resultado_final = soma[0][index + le2+1:].set_color(LIGHT_PINK)
        self.end_fragment()  #################################

 
        self.add(
            matriz_A,ent2[0],ent2[1],ent2[3],ent2[4],ent2[6],ent2[7],
        )   

        L3 = Line(ent[2].get_center(),ent[6].get_center())
        L3.set_z_index(-1).set_stroke(color=YELLOW, opacity=.5, width=25).set_cap_style(CapStyleType.ROUND)
        L3.scale(1.1)

        L4 = Line(ent2[0].get_center(),ent[7].get_center())
        L4.set_z_index(-1).set_stroke(color=YELLOW, opacity=.5, width=25).set_cap_style(CapStyleType.ROUND)
        L4.scale(1.1)
            
        L5 = Line(ent2[1].get_center(),ent[8].get_center())
        L5.set_z_index(-1).set_stroke(color=YELLOW, opacity=.5, width=25).set_cap_style(CapStyleType.ROUND)
        L5.scale(1.1)

#################################################################################
        Linhas = VGroup(L5,L4,L3)
        seq = [ 1,0,2
            
        ]


        r= MathTex(rf"i").next_to(resultados,0.5*DOWN).set_color(BLACK)
        r1= MathTex(rf"i").next_to(r,0.5*DOWN).set_color(BLACK)
        r2= MathTex(rf"i").next_to(r1,0.5*DOWN).set_color(BLACK)


        for i  in range(3):
            index = 0
            produto = A[0][seq[0]] * A[1][seq[1]] * A[2][seq[2]]
            eq = MathTex(rF"{A[0][seq[0]]} \cdot {A[1][seq[1]]} \cdot {A[2][seq[2]]} = {produto} ").scale(0.5)
            if i == 0:
                p = MathTex(f"{A[0][seq[0]]}").move_to(ent2[seq[0]]).set_color(BLUE).scale(0.5)
                p1 = MathTex(f"{A[1][seq[1]]}").move_to(ent2[seq[1] + 3]).set_color(RED).scale(0.5)
                p2 = MathTex(f"{A[2][seq[2]]}").move_to(ent[seq[2] + 6]).set_color(GREEN).scale(0.5)
            elif i == 1:
                p = MathTex(f"{A[0][seq[0]]}").move_to(ent2[seq[0]]).set_color(BLUE).scale(0.5)
                p1 = MathTex(f"{A[1][seq[1]]}").move_to(ent[seq[1] + 3]).set_color(RED).scale(0.5)
                p2 = MathTex(f"{A[2][seq[2]]}").move_to(ent[seq[2] + 6]).set_color(GREEN).scale(0.5)
            elif i == 2:
                p = MathTex(f"{A[0][seq[0]]}").move_to(ent[seq[0]]).set_color(BLUE).scale(0.5)
                p1 = MathTex(f"{A[1][seq[1]]}").move_to(ent[seq[1] + 3]).set_color(RED).scale(0.5)
                p2 = MathTex(f"{A[2][seq[2]]}").move_to(ent[seq[2] + 6]).set_color(GREEN).scale(0.5)


            eq.next_to(matriz_A,DOWN)  
            self.play(Create(Linhas[i]))
            self.wait()
            self.play(p.animate.move_to(eq[0][index:index +len(str(p.get_tex_string()))]))
            index += len(str(p.get_tex_string())) + 1
            a = eq[0][index-1]
            self.play(Create(a))
            self.play(p1.animate.move_to(eq[0][index:index + len(str(p1.get_tex_string()))]))
            index += len(str(p1.get_tex_string())) + 1
            b = eq[0][index-1]
            self.play(Create(b))
            self.play(p2.animate.move_to(eq[0][index:index+ len(str(p2.get_tex_string()))]))
            igual = eq[0][index+len(str(p2.get_tex_string()))]
            self.play(Create(igual))
            ultimo = eq[0][index+len(str(p2.get_tex_string())) +1:].set_color(YELLOW)
            self.play(Write(ultimo))
            if i == 0:
                ultimo1 = ultimo.copy().set_color(YELLOW)
                self.play(ultimo1.set_color(YELLOW).animate.move_to(r))
            if i == 1:
                ultimo2 = ultimo.copy().set_color(YELLOW)
                self.play(ultimo2.set_color(YELLOW).animate.move_to(r1))
            if i == 2:
                ultimo3 = ultimo.copy().set_color(YELLOW)
                self.play(ultimo3.set_color(YELLOW).animate.move_to(r2))
            y = seq.pop(0)
            seq.append(y)
            self.remove(p,p1,p2,a,b,igual,ultimo)

        self.end_fragment()  ################################
        seq = [1,0,2]
        produtos = []
        resul1 = 0
        for i in range(3):
            produto = f"{A[0][seq[0]] * A[1][seq[1]]* A[2][seq[2]]}"
            resul1 += A[0][seq[0]] * A[1][seq[1]]* A[2][seq[2]]
            produtos.append(produto)
            if i ==0:
                le = len(str(A[0][seq[0]] * A[1][seq[1]]* A[2][seq[2]]))
            if i == 1:
                le1 = len(str(A[0][seq[0]] * A[1][seq[1]]* A[2][seq[2]]))
            if i == 2:
                le2 = len(str(A[0][seq[0]] * A[1][seq[1]]* A[2][seq[2]]))
            y = seq.pop(0)
            seq.append(y)
        soma_str = " + ".join(produtos)
        soma1 = MathTex(rf"{soma_str} = {resul1}").scale(0.5)
        soma1.shift(2*LEFT + 1.5*DOWN )
    
        index = 0
        for i in range(3):
            if i == 0:
                self.play(ultimo1.animate.move_to(soma1[0][index:index + le]))
                index += le +1
                self.play(Create(soma1[0][index-1]))
            if i == 1:
                self.play(ultimo2.animate.move_to(soma1[0][index:index + le1]))
                index += le1 +1
                self.play(Create(soma1[0][index-1]))
            if i == 2:
                self.play(ultimo3.animate.move_to(soma1[0][index:index + le2]))
                self.play(Write(soma1[0][index + le2:index + le2+1]))
                self.play(Write(soma1[0][index + le2+1:].set_color(YELLOW)))
                resultado_final1 = soma1[0][index + le2+1:].set_color(YELLOW)
        self.end_fragment()  #################################
        Det = MathTex(rf"Det(A) = {resul} - {resul1} ").scale(0.5)
        Det1 = MathTex(rf"Det(A) = {determinante} ").scale(0.5)
        Det.shift(2*RIGHT+UP)
        Det1.next_to(Det,DOWN)
        self.remove(resultados)
        self.play(Write(Det[0][:7]))
        self.play(resultado_final.copy().animate.move_to(Det[0][7:7 + len(str(resul))]))
        self.play(Write(Det[0][7+len(str(resul)):7 +1 + len(str(resul))] ))
        self.play(resultado_final1.copy().animate.move_to(Det[0][7 + len(str(resul))+1:7 + len(str(resul)) + len(str(resul1))+1]))
        z = VGroup(Det[0][7:7 + len(str(resul))].set_color(LIGHT_PINK),Det[0][7 + len(str(resul))+1:7 + len(str(resul)) + len(str(resul1))+1].set_color(YELLOW) )
        self.play(Write(Det1[0][:7]))
        self.play(TransformFromCopy(z,Det1[0][7:]))
        self.wait()
        self.end_fragment()  #################################