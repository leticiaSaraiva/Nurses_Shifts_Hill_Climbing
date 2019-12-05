from estado import *

# STEEPEST-ASCENT HILL CLIMBING
def subida_de_encosta_maior_aclive(est_inicial):
    
    e_atual = None
    e_prox = est_inicial
    
    while e_prox != None:
        e_atual = e_prox
        imprime_estado(e_atual)        
        
        #guardamos o melhor vizinho encontrado até o momento
        menor_viz = None
        avaliacao_menor_viz = avaliacao(e_atual)
        
        #buscamos entre todos os vizinhos o melhor estado
        for e_viz in sucessores(e_atual):
            avaliacao_viz = avaliacao(e_viz)
            #ao encontrar um melhor estado, salvamos ele
            #porem, diferente da subida de encosta simples, continuamos a busca
            if(avaliacao_viz < avaliacao_menor_viz):
                menor_viz = e_viz
                avaliacao_menor_viz = avaliacao_viz
                
        e_prox = menor_viz
    
    return e_atual
