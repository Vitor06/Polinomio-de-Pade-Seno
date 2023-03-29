from math import  sin,pi
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import csv

#Constantes
MIN = -pi/4
MAX = pi/4
STEP = 0.1

K = -0.1666666666666666#-1/6
M = 0.0083333333333333 #1/120
N =  -0.0001984126984126984 #-1/5040
P = 2.755731922398589e-6 # 1/362880
Q = -2.505210838544172e-8 #-1/39916800

D = -0.1460606060606061
E = 0.0032744107744108
F =-0.0005335097000176
G = 0.0206060606060606
H =0.00015993265993265

#gráfico
# fig, ax= plt.subplots(2,2 )
# ax[0,0].set_xlim([MIN,MAX])
# ax[0,1].set_xlim([MIN,MAX])

# ax[0,0].set_yscale('symlog')
# ax[0,1].set_yscale('symlog')

#tabelas
table = PrettyTable()
tabale_erro  =PrettyTable()
tabale_tempo  =PrettyTable()

def desenhar_ponto(ponto,color,text):
    plt.plot(ponto[0], ponto[1], markerfacecolor=color,label=text,)#Posicao real
    # plt.set_title(text)
    plt.legend()


def calacular_erro(seno_exato,seno_aproximado):
    erro_list = []
    for i in range(0,len(seno_aproximado)):
        erro_list.append(abs(seno_aproximado[i] - seno_exato[i]))
    return erro_list
#Seno Correto
def seno(x):
    return sin(x)

#Seno truncado - Serie  - Multiplicações reduzidas
def seno_horner(x):
        return x*(1 + (x**2) *(K + (x**2) *(M +(x**2) *(N + (x**2) *(P + (x**2)*Q)))))

def seno_pade(x):

   return  (x*(1+(x**2)*(D+(x**2)*(E+F*(x**2)) )))/(1+(x**2)*(G +H*(x**2)))
def main():
    x = MIN
    seno_serie_list,seno_exato_list,seno_pade_list,x_list,tempo_pade_list,tempo_serie_list = [],[],[],[],[],[]

    while x<=MAX:
        start_seno_pade = time.time_ns()
        pade = seno_pade(x)
        end_seno_pade = time.time_ns()

        tempo_pade_list.append(end_seno_pade -start_seno_pade)

        start_seno_serie = time.time_ns()
        serie  =seno_horner(x)
        end_seno_serie = time.time_ns()

        tempo_serie_list.append(end_seno_serie - start_seno_serie)

        seno_ = seno(x)

        x_list.append(x)
        seno_serie_list.append(serie)
        seno_exato_list.append(seno_)
        seno_pade_list.append(pade)
        x+=STEP

    #Calculando para MAX = pi/4
    start_seno_pade = time.time_ns()
    pade = seno_pade(MAX)
    end_seno_pade = time.time_ns()

    tempo_pade_list.append(end_seno_pade -start_seno_pade)

    start_seno_serie = time.time_ns()
    serie  =seno_horner(MAX)
    end_seno_serie = time.time_ns()

    tempo_serie_list.append(end_seno_serie - start_seno_serie)

    seno_ = seno(MAX)

    x_list.append(x)
    seno_serie_list.append(serie)
    seno_exato_list.append(seno_)
    seno_pade_list.append(pade)



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

    # plt.set_ylim([min(erro_seno_exato_serie),max(erro_seno_exato_serie)])
    # plt.set_ylim([min(erro_seno_exato_pade),max(erro_seno_exato_pade)])

    plt.plot(x_list,erro_seno_exato_pade,label = "Exato-Pade")
    plt.plot(x_list,erro_seno_exato_serie,label = "Exato-Serie")

    plt.xlabel('Argumento')
    plt.ylabel('Erro')
    plt.legend()

    plt.show()
    # fig.delaxes(ax[1,1])
    # fig.delaxes(ax[1,0])

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
    print()
    print("Seno - exato")
    print(seno(pi/4))
    print()
    print("Seno_serie_reduzida")
    print(seno_horner(pi/4))
    print()
    print("Seno_Pade")
    print(seno_pade(pi/4))
    print()
    print("Erro Maximo - Pade")
    print(max(erro_seno_exato_pade))
    print()
    print("Erro Maximo - Serie")
    print(max(erro_seno_exato_serie))

main()
