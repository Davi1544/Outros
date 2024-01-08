# Nos jogos da franquia "Pokemon", cada monstrinho tem de um a dois tipos
# Cada tipo tem suas fraquezas e vantagens (tanto ofensivamente quanto defensivamente)
# O objetivo desse script é receber os tipos de um pokemon e calcular suas fraquezas e vantagens (tanto ofensivamente quanto defensivamente)

# Para fins práticos, os tipos serão representados por números de 0 a 17 (já que existem 18 tipos)

# coluna => tipo atacado
# linha => tipo atacante

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

# variáveis

tipo1_of = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
tipo2_of = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
tipo1_df = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
tipo2_df = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
tipo1_input = 0
tipo2_input = 0
resultado_ofensivo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
resultado_defensivo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# código

tipo1_input = int(input("Qual o código do primeiro tipo? "))
tipo2_input = int(input("Qual o código do segundo tipo?(0 para típo único) "))

if tipo1_input == tipo2_input:
    tipo2_input = 0
    
tipo1_of = returnTipoOfensivo(tipo1_input)
tipo1_df = returnTipoDefensivo(tipo1_input)
tipo2_of = returnTipoOfensivo(tipo2_input)
tipo2_df = returnTipoDefensivo(tipo2_input)

resultado_ofensivo = returnJuncaoTiposOf(tipo1_of, tipo2_of)
resultado_defensivo = returnJuncaoTiposDef(tipo1_df, tipo2_df)

print(f"Defensivamente: {resultado_defensivo}")
print(f"Ofensivamente: {resultado_ofensivo}")