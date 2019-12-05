## EQUIPE ##
# Claro Henrique
# Letícia Saraiva

from estado import *

# FILA DE PRIORIDADE
#funcoes auxiliares na fila de prioridade

#retorna filho esquerdo
def l(x):
    return x*2+1
#retorna filho direito
def r(x):
    return x*2+2
#retorna nó pai
def pai(x):
    return x//2


#para uma melhor eficiência na hora de ordenar a fila, utilizaremos a fila de prioridade,
#onde as operações de inserção e remoção tem complexidade O(lg(n))
class fila_prioridade:
    def __init__(self, compare=lambda a,b:a<b):
        self.v = []
        self.comp = compare
        self.size_ = 0
        
    def size(self):
        return self.size_
    
    def empty(self):
        return self.size() == 0
    
    def descer(self,pos):
        if l(pos) < self.size() and r(pos) < self.size():
            if self.comp(self.v[l(pos)],self.v[pos]) and self.comp(self.v[l(pos)],self.v[r(pos)]): 
                self.v[pos], self.v[l(pos)] = self.v[l(pos)],self.v[pos]
                self.descer(l(pos))
            elif self.comp(self.v[r(pos)],self.v[pos]):
                self.v[pos], self.v[r(pos)] = self.v[r(pos)],self.v[pos]
                self.descer(r(pos))
        elif l(pos) < self.size() and self.comp(self.v[l(pos)],self.v[pos]):
            self.v[pos], self.v[l(pos)] = self.v[l(pos)],self.v[pos]
            self.descer(l(pos))
        elif r(pos) < self.size() and self.comp(self.v[r(pos)],self.v[pos]):
            self.v[pos], self.v[r(pos)] = self.v[r(pos)],self.v[pos]
            self.descer(r(pos))
    
    def subir(self,pos):
        if pos == 0:
            return
        else:
            if self.comp(self.v[pos],self.v[pai(pos)]):
                self.v[pos] ,self.v[pai(pos)] = self.v[pai(pos)],self.v[pos]
                self.subir(pai(pos))
    
    def pop(self):
        if self.size() > 0:
            self.v[0] = self.v[self.size()-1]
            del self.v[-1]
            self.size_ -= 1
            self.descer(0)
    
    def push(self,x):
        self.size_ += 1
        self.v.append(x)
        self.subir(self.size()-1)
        
    def top(self):
        return self.v[0]


# BEST-FIRST SEARCH
def best_first_seach(est_inicial, max_it=500):
    
    #na fila de prioridade, iremos guardar uma tupla (avaliacao(estado), estado)
    #dessa forma, evitaremos o recalculo de avaliação de um estado
    initial_node = (avaliacao(est_inicial),est_inicial)
    best_node = initial_node
    
    #utilizaremos o primeiro elemento da tupla para comparar
    comparer_function = lambda a,b: a[0] < b[0]
    
    #insere o primeiro estado na fila
    fila = fila_prioridade(comparer_function)
    fila.push(initial_node)
    
    while not fila.empty():
        e_atual = fila.top()[1]          #pegamos o estado do topo da fila (sempre o de menor avaliação)
        imprime_estado(e_atual)
        avaliacao_atual = fila.top()[0]  #pegamos a avaliação correspondente
        fila.pop()                       #remove o elemento da fila 
        
        #o no atual possui uma menor avaliação que o melhor nó encontrado até o momento
        if avaliacao_atual < best_node[0]:
            best_node = (avaliacao_atual,e_atual)
        #objetivo alcançado
        if avaliacao_atual == 0:
            break 
        
        #controle do máximo de iterações
        max_it -= 1
        if max_it == 0:
            break
        
        #busca um no melhor atraves dos vizinhos do no atual
        for e_viz in sucessores(e_atual):
            avaliacao_viz = avaliacao(e_viz)
            #insere um no melhor na fila de prioridade
            if(avaliacao_viz < avaliacao_atual):
                fila.push((avaliacao_viz,e_viz))
    
    imprime_estado(best_node[1])
    return best_node[1] #retorna o estado com menor avaliacao encontrado durante a busca         
