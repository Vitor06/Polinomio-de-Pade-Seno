from math import  sin,pi
from matplotlib import pyplot as plt
import numpy as np

#Constantes
MIN = -pi/4
MAX = pi/4
STEP = 0.04
K = 1/6
M = 1/120
N = 1/5040
P =1/362880
Q = 1/39916800
fig, ax= plt.subplots(2, 2)

def desenhar_ponto(ponto,color,text,i,j):
    ax[i,j].plot(ponto[0], ponto[1], marker="o", markersize=5, markeredgecolor=color, markerfacecolor=color,label=text,)#Posicao real
    ax[i,j].set_title(text)
    plt.legend()

def calacular_erro(seno_exato,seno_aproximado):
    erro_list = []
    for i in range(0,len(seno_aproximado)):
        erro_list.append(abs(seno_aproximado[i] - seno_exato[i]))
    return erro_list
#Seno Correto
def seno(x):
    return sin(x)
#Seno truncado - Serie
def seno_serie(x):
    return x - (pow(x,3)/6) + (pow(x,5)/120) - (pow(x,7)/5040) + (pow(x,9)/362880) - (pow(x,11)/39916800)
    #x - x^3/6 + x^5/120 - x^7/5040 + x^9/362880 - x^11/39916800  = 
    #x - x^3(1/6-x^2/120 +x^4/5040 - x^6/362880  +x^8/39916800) = 
    #x - x^3(1/6-x^2(1/120 + x^2/5040 - x^4/362880 + x^6/39916800))=
    # x -x^3(1/6 - x^2(1/120 +x^2(1/5040 - x^2/362880 + x^4/39916800))) = 
    # x -x^3(1/6 - x^2(1/120 +x^2(1/5040 - x^2(1/362880 - x^2/39916800))) = 
    # x(1 -x^2(1/6 - x^2(1/120 -x^2(1/5040 - x^2(1/362880 - x^2/39916800))))) = 

#Seno truncado - Serie  - Multiplicações reduzidas
def seno_serie_mult_reduzida(x):
        return x*(1 - (x**2) *(K - (x**2) *(M -(x**2) *(N - (x**2) *(P - (x**2)*Q)))))  

def seno_pade(x):
    return x - (pow(x,3)/6) - (pow(x,7)/5040) #Rever #Fazer a redução de multiplicações

def main():
    x = MIN
    seno_serie_list,seno_exato_list,seno_pade_list,x_list = [],[],[],[]

    while x<=MAX:

        x_list.append(x)
        seno_serie_list.append(seno_serie(x))#Mudar para  a reduzida
        seno_exato_list.append(seno(x))
        seno_pade_list.append(seno_pade(x))
        x+=STEP

    desenhar_ponto((x_list,seno_exato_list),"red","Seno_Exato",0,0)
    desenhar_ponto((x_list,seno_pade_list),"blue","Pade",0,1)
    desenhar_ponto((x_list,seno_serie_list),"green","Seno_Serie",1,0)
    fig.delaxes(ax[1,1])


    seno_serie_dict = dict(zip(x_list,seno_serie_list))
    seno_exato_dict = dict(zip(x_list,seno_exato_list))
    seno_pade_dict = dict(zip(x_list,seno_pade_list))

    print()
    print("Seno-Exato")
    print(seno_exato_list)
    print()
    print("Seno-Aproximado")
    print(seno_serie_list)
    print()
    print("Seno-Pade")
    print(seno_pade_list)
    print()
    print("Erro em relação a serie")
    print(calacular_erro(seno_exato_list,seno_serie_list))
    print()
    print("Erro em relação a pade")
    print(calacular_erro(seno_exato_list,seno_pade_list))
    plt.show()

    # print("Seno - exato")
    # print(seno(4))
    # print()
    # print("Seno_serie_reduzida")
    # print(seno_serie_mult_reduzida(4))
    # print()
    # print("Seno_serie")
    # print(seno_serie(4))

main()
