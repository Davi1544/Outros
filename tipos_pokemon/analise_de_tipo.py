# utilizando o script calculadora de tipo

type_chart = [
    [1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # 1. Normal
    [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5],  # 2. Lutador
    [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1],      # 3. Voador
    [1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2],    # 4. Venenoso
    [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1],   # 5. Terra
    [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1],      # 6. Pedra
    [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5],  # 7. Inseto
    [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1],      # 8. Fantasma
    [1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 1, 0.5],        # 9. Aço
    [1, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5, 0.5, 2, 1, 1, 2, 0.5, 1, 1],      # 10. Fogo
    [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 0.5, 1, 1],  # 11. Água
    [1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1, 1],    # 12. Planta
    [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1],      # 13. Elétrico
    [1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 0, 1],      # 14. Psíquico
    [1, 1, 2, 1, 2, 1, 1, 1, 0.5, 0.5, 0.5, 2, 1, 1, 0.5, 2, 1, 1],      # 15. Gelo
    [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 0],      # 16. Dragão
    [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5],        # 17. Noturno
    [1, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 2, 2, 1]       # 18. Fada
]

peso_of = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
peso_def = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# funções

def returnTipoOfensivo(numero):

    if numero != 0:
        tipo_ofensivo = [type_chart[numero-1][i] for i in range(0,18)]
    else:
        tipo_ofensivo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    return tipo_ofensivo

def returnTipoDefensivo(numero):

    if numero != 0:
        tipo_defensivo = [type_chart[i][numero-1] for i in range(0,18)]
    else:
        tipo_defensivo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    return tipo_defensivo

def returnJuncaoTiposDef(tipo1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], tipo2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]):
    
    array_final = []
    x = 0

    while x < 18:
        to_append = tipo1[x] * tipo2[x]
        array_final.append(to_append)
        x += 1
    
    return array_final

def returnJuncaoTiposOf(tipo1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], tipo2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]):
    
    array_final = []
    x = 0

    while x < 18:

        if tipo1[x] > tipo2[x]:
            to_append = tipo1[x]
        else:
            to_append = tipo2[x]

        array_final.append(to_append)
        x += 1
    
    return array_final

def sendTipos(t1=0,t2=0, metodo=0, pior=1):

    tipo1_of = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    tipo2_of = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    tipo1_df = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    tipo2_df = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    tipo1_input = t1
    tipo2_input = t2
    resultado_ofensivo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    resultado_defensivo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    if tipo1_input == tipo2_input:
        tipo2_input = 0
        
    tipo1_of = returnTipoOfensivo(tipo1_input)
    tipo1_df = returnTipoDefensivo(tipo1_input)
    tipo2_of = returnTipoOfensivo(tipo2_input)
    tipo2_df = returnTipoDefensivo(tipo2_input)

    resultado_ofensivo = returnJuncaoTiposOf(tipo1_of, tipo2_of)
    resultado_defensivo = returnJuncaoTiposDef(tipo1_df, tipo2_df)

    i = 0
    pontuacao_ofensiva = 0
    pontuacao_defensiva = 0
    pontuacao_geral = 0

    while i < 18:
        pontuacao_defensiva += resultado_defensivo[i] * peso_def[i]
        pontuacao_ofensiva += resultado_ofensivo[i] * peso_of[i]
        i += 1

    pontuacao_geral = pontuacao_ofensiva - pontuacao_defensiva

    if metodo == 0:
        return pior*pontuacao_geral
    if metodo == 1:
        return pior*pontuacao_ofensiva
    if metodo == 2: 
        return pior*pontuacao_defensiva
    

# código
    
melhores_ = []
maior_pontuacao = 0 # setar como -100 se quiser os piores
metodo = 0 # 0 => global, 1 => ofensivamente, 2 => defensivamente
pri = 0
sec = 1
pior = 1 # setar como -1 se quiser os piores

if metodo == 2:
    maior_pontuacao = 100

while pri < 18:
    sec = 1
    while sec < 19:
        pont_ind = 0
        pont_ind = sendTipos(pri, sec, metodo, pior)

        if metodo != 2:
            if pont_ind > maior_pontuacao:
                maior_pontuacao = pont_ind
                melhores_ = []
                melhores_.append([pri,sec])
            elif pont_ind == maior_pontuacao:
                melhores_.append([pri,sec])
        else:
            if pont_ind < maior_pontuacao:
                maior_pontuacao = pont_ind
                melhores_ = []
                melhores_.append([pri,sec])
            elif pont_ind == maior_pontuacao:
                melhores_.append([pri,sec])
            
        sec += 1

    pri += 1

print(f"Maior pontuação {metodo} : {maior_pontuacao}")
print(f"Tipos com tal pontuação : {melhores_}")