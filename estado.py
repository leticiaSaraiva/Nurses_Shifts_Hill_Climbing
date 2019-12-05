#Arquivo contendo todas as funções de um estado

## EQUIPE ##
# Claro Henrique
# Letícia Saraiva

#funcao que imprime um estado
#imprime a avaliação daquele estado
#e representação que é descrita no enunciado do trabalho

tu = 21   #turnos precisa ser divisivel por 3
en = 10   #numero de enfermeiros

def define_parametros(turnos,enferm):
    global tu
    global en
    tu = turnos
    en = enferm

def imprime_estado(e):
    print('Custo:',avaliacao(e))
    for i in range(en):
        s = '['
        for j in range(tu):
            if j == tu-1:
                s += str(e[i*tu + j]) + ']'
            elif j%3 == 2:
                s += str(e[i*tu + j]) + '|'
            else:
                s += str(e[i*tu + j]) + ''
        print(s)
    print()

#funcao que retorna a vizinhança de um estado
def sucessores (e):
    succ = []    
    for i in range(len(e)):
        e[i] = (e[i]+1)%2    #troca o bit na posição i
        succ.append(e[:])    #insere como vizinho
        e[i] = (e[i]+1)%2    #volta ao estado original
    return succ


#Restrições

#Restrição 1
#avalia se cada turno tem entre 1 e 3 enfermeiros
#retorna a quantidade de turnos que ferem a restrição
def avalia_r1(e):
    erros = 0
    for t in range(tu):
        soma = 0
        for enf in range(en):
            soma += e[enf*tu + t]   
        if soma < 1 or soma > 3:
            erros += 1
    return erros


#Restrição 2
#avalia se cada enfermeiro está alocado em 5 turnos
#para todo enfermeiro retorna a distância que falta para ele atender a restrição

def avalia_r2(e):
    erros = 0
    for enf in range(en):
        soma = 0
        #soma todos os turnos que o enfermeiro trabalha
        for t in range(tu):
            soma += e[enf*tu + t]
            
        erros += abs(5 - soma)
        #adicionaremos a distancia para o 5 turnos como penalidade
    return erros


#Restrição 3
#avalia se nenhum enfermeiro trabalha em tres turnos seguidos sem folga
#para todo enfermeiro retorna se ele atende ou não a restrição

def avalia_r3(e):
    #
    erros = 0
    for enf in range(en):
        for t in range(tu-2):
            soma = 0
            soma += e[enf*tu + t]       #turno da madrugada
            soma += e[enf*tu + (t+1)]   #turno da manha
            soma += e[enf*tu + (t+2)]   #turno da noite
            if soma == 3:
                erros += 1
    return erros


#Restrição 4
#avalia se os enfermeiros trabalham em um só tipo de turno (ex: só de manhã)
#retorna, para cada enfermeiro, a quantidade de turnos que ele trabalha -1
#exemplo: se o enfermeiro trabalha em um turno, a penalidade é 0
#se ele trabalha em três turnos a penalidade é 2

def avalia_r4(e):
    erros = 0
    for enf in range(en):
        #horários que enfermeiro 'enf' ocupa
        horario_ocupado = [0,0,0]
        
        #para cada turno, soma a quantidade de horários que o 'enf' trabalha nele
        for t in range(0,tu,3):
            horario_ocupado[0] += e[enf*tu + t]
            horario_ocupado[1] += e[enf*tu + (t+1)]
            horario_ocupado[2] += e[enf*tu + (t+2)]
        
        
        soma = 0
        #precisamos restringir o somatorio de cada turno para 1
        soma += min(horario_ocupado[0],1)
        soma += min(horario_ocupado[1],1)
        soma += min(horario_ocupado[2],1)
        
        #distancia para o enfermeiro atender somente um horário
        erros += abs(1 - soma)
    return erros


r1,r2,r3,r4 = True,True,True,True
#turnos = 21   #turnos precisa ser divisivel por 3
#enferm = 10

#Função de avaliação
def avaliacao (e):
    #pesos para cada tipo de restrição 
    #consideramos a Restrições 1 e 2 mais importantes
    p1,p2,p3,p4 = 1,1,1,1
    
    #custos calculados de acordo com o retorno das funções de avaliação de restrições
    custo1,custo2,custo3,custo4 = 0,0,0,0
    if r1:
        custo1 += avalia_r1(e)*p1
    if r2:
        custo2 += avalia_r2(e)*p2
    if r3:
        custo3 += avalia_r3(e)*p3
    if r4:
        custo4 += avalia_r4(e)*p4
    
    return custo1+custo2+custo3+custo4


