from math import  sin,pi
import time
from matplotlib import pyplot as plt
import numpy as np
from prettytable import PrettyTable
#Constantes
MIN = -pi/4
MAX = pi/4
STEP = 0.1
K = 1/6
M = 1/120
N = 1/5040
P =1/362880
Q = 1/39916800
fig, ax= plt.subplots(2, 2)
table = PrettyTable()
tabale_erro  =PrettyTable()
tabale_tempo  =PrettyTable()


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
    # return x - (pow(x,3)/6) - (pow(x,7)/5040)
   #x*(1 - (x**2)*K- (x**6)*N)
   return  x*(1 - (x**2)*(K +(x**4)*N))

def main():
    x = MIN
    seno_serie_list,seno_exato_list,seno_pade_list,x_list,tempo_pade_list,tempo_serie_list = [],[],[],[],[],[]

    while x<=MAX:
        start_seno_pade = time.time()
        pade = seno_pade(x)
        end_seno_pade = time.time()

        tempo_pade_list.append(end_seno_pade -start_seno_pade)

        start_seno_serie = time.time()
        serie  =seno_serie(x)
        end_seno_serie = time.time()

        tempo_serie_list.append(end_seno_serie - start_seno_serie)

        seno_ = seno(x)

        x_list.append(x)
        seno_serie_list.append(serie)#Mudar para  a reduzida
        seno_exato_list.append(seno_)
        seno_pade_list.append(pade)
        x+=STEP


    erro_seno_exato_serie = calacular_erro(seno_exato_list,seno_serie_list)
    erro_seno_exato_pade  = calacular_erro(seno_exato_list,seno_pade_list)

    tabale_erro.add_column('X',x_list)
    tabale_erro.add_column('Erro Seno Exato - Serie',erro_seno_exato_serie)
    tabale_erro.add_column('Erro Seno Exato-Pade',erro_seno_exato_pade)

    table.add_column('X',x_list)
    table.add_column('Seno -Exato',seno_exato_list)
    table.add_column('Seno - serie',seno_serie_list)
    table.add_column('Seno-Pade',seno_pade_list)

    tabale_tempo.add_column("X",x_list)
    tabale_tempo.add_column("Tepo Serie",tempo_serie_list)
    tabale_tempo.add_column("Tempo Pade",tempo_pade_list)



    print(table)
    print(tabale_erro)
    print(tabale_tempo)


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
    print()
    print(erro_seno_exato_serie)
    print()
    print("Erro em relação a pade")
    print(erro_seno_exato_pade)
    # plt.show()

    print("Seno - exato")
    print(seno(pi/4))
    print()
    print("Seno_serie_reduzida")
    print(seno_serie_mult_reduzida(pi/4))
    print()
    print("Seno_serie")
    print(seno_serie(pi/4))

main()
