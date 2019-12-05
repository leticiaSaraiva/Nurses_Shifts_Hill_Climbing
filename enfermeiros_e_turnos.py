
## EQUIPE ##
# Claro Henrique
# Letícia Saraiva


from hill_climbing import subida_de_encosta
from steepest_ascent_hill_climbing import subida_de_encosta_maior_aclive
from best_first_seach import best_first_seach
from estado import *

turnos = 21   #turnos precisa ser divisivel por 3
enferm = 10
metodo = 0
m2s = {0:'Hill Climbing',1:'Steepest-Ascent Hill Climbing',2:'Best First Search'}
define_parametros(turnos,enferm)

from random import randint

#Função para gerar um estado aleatório
def gerar_estado_aleatorio(n_enf,n_tur):
    res = []
    for i in range(n_enf):
        for j in range(n_tur):
            res.append(randint(0,1))
    return res

#Função para ler um arquivo contendo um estado específico
def gerar_estado_arquivo():
    f = open('input.txt','r')
    global enferm
    estado_inicial = []
    enferm = -1
    for linha in f:
        enferm += 1
        for col in linha:
            if col != '\n':
                estado_inicial.append(int(col))
    define_parametros(turnos,enferm)
    return estado_inicial

#Função para resolver o problema a partir de um estado vazio
def resolver_estado_vazio():
    estado_inicial = [0]*enferm*turnos
    if metodo == 0:
        subida_de_encosta(estado_inicial)
    if metodo == 1:
        subida_de_encosta_maior_aclive(estado_inicial)
    if metodo == 2:
        best_first_seach(estado_inicial)

#Função para resolver o problema a partir de um estado gerado aleatoriamente
def resolver_estado_aleatorio():
    estado_inicial = gerar_estado_aleatorio(enferm,turnos)
    if metodo == 0:
        subida_de_encosta(estado_inicial)
    if metodo == 1:
        subida_de_encosta_maior_aclive(estado_inicial)
    if metodo == 2:
        best_first_seach(estado_inicial)

#Função para resolver o problema a partir do estado lido do arquivo
def resolver_estado_arquivo():
    estado_inicial = gerar_estado_arquivo()
    if metodo == 0:
        subida_de_encosta(estado_inicial)
    if metodo == 1:
        subida_de_encosta_maior_aclive(estado_inicial)
    if metodo == 2:
        best_first_seach(estado_inicial)

#Função para executar a Subida de Encosta pelo Maior
#Aclive n vezes, cada uma iniciando com um estado aleatório, e apresentando
#ao final o melhor estado gerado entre todas as execuções.
def resolve_n_estados_aleatorios():
    print('Digite o numero de iteracoes:')
    n = int(input())

    melhor_estado = None

    for i in range(n):
        print('\\\\\\\\\\\\-------- iteracao numero ',i+1,' -----------///////')
        estado_inicial = gerar_estado_aleatorio(enferm,turnos)
        estado_resultado = subida_de_encosta_maior_aclive(estado_inicial)

        if(melhor_estado == None or avaliacao(estado_resultado) < avaliacao(melhor_estado)):
            melhor_estado = estado_resultado

    print('O melhor resultado encontrado foi ᕦ( ͡° ͜ʖ ͡°)ᕤ')
    imprime_estado(melhor_estado)


def limpar_tela():
    print('\n'*0)
    
def pressione_enter():
    print('Precione ENTER para continuar.')
    input()
    limpar_tela()


def menu_principal():
    
    while True:
        print('Bem vindo ao programa que resolve um problema de alocacao de enfermeiros em turnos! (✿❦ ͜ʖ ❦)\n')
        #print('Selecione a opcao desejada:')
        print('[1] - resolver problema do arquivo de texto (input.txt)')
        print('[2] - resolver problema a partir de um estado vazio')
        print('[3] - resolver problema a partir de um estado aleatorio')
        print('[4] - resolver problema partindo de varios estados aleatorios')
        print('[5] - mudar os parametros da busca')
        
        print()
        print('[0] - para encerrar o programa')

        op = input()
        if(op == '1'):
            resolver_estado_arquivo()
        if(op == '2'):
            resolver_estado_vazio()
        if(op == '3'):
            resolver_estado_aleatorio()
        if(op == '4'):
            resolve_n_estados_aleatorios()
        if(op == '5'):
            menu_parametros()
        if(op == '0'):
            break

        pressione_enter()


def menu_parametros():
    while True:
        print('Bem vindo ao menu de mundanca de parametros! ( ͡~ ͜ʖ ͡°)\n')
        global metodo
        global enferm
        print('Metodo atual:', m2s[metodo])
        print('Numero de enfermeiros atual:',enferm)
        print()

        print('[1] - escolher metodo de busca')
        print('[2] - escolher numero de enfermeiros')
        print()
        print('[0] - voltar ao menu principal')
        
        op = input()
        if(op == '0'):
            break
        if(op == '1'):
            print('Escolha o metodo de busca:')
            print('[1] - Hill Climbing (Subida de Encosta)')
            print('[2] - Steepest-Ascent Hill Climbing (Subida de Encosta pelo Maior Aclive)')
            print('[3] - Best First Search (Busca pelo Melhor Primeiro)')
            metodo = int(input()) - 1
        if(op == '2'):
            print('Digite a quantidade de enfermeiros')
            enferm = int(input())
    define_parametros(turnos,enferm)


menu_principal()
