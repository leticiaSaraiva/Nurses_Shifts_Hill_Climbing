## EQUIPE ##
# Claro Henrique
# Letícia Saraiva

from estado import *

#HILL CLIMBING
def subida_de_encosta(est_inicial):
    e_prox  = est_inicial
    e_atual = None
    
    while e_prox != None:
        e_atual = e_prox
        imprime_estado(e_atual) #imprime o estado visitado

        avaliacao_atual = avaliacao(e_atual)
        e_prox = None
        
        #busca um estado melhor na vizinhança
        for e_viz in sucessores(e_atual):
            avaliacao_viz = avaliacao(e_viz)
            #encerra assim que encontrar um estado vizinho melhor 
            if(avaliacao_viz < avaliacao_atual):
                e_prox = e_viz
                break
    
    return e_atual

