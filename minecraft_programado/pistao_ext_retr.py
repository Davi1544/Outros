# Script para geração de extensão e retração segundo o vídeo: https://www.youtube.com/watch?v=t4iGp44WQ-U
# funções

def extensao_ope(tamanho = 0):
    res = 0
    mod = tamanho % 12
    sum = mod

    while sum <= tamanho: 
        res += sum
        sum += 12
    
    return res

def retracao_ope(tamanho = 0):
    if tamanho == 2:
        return 3
    elif tamanho > 2:
        return retracao_ope(tamanho-1) + tamanho

def extensao_fila_ope(tamanho = 0):
    res_f = ""
    res = 0
    mod = tamanho % 12
    sum = mod
    last = 0

    while sum <= tamanho: 
        res += sum

        n = 0

        while (res-(last+n)) >= 1:
            res_f += str(res-(last+n)) + " "
            n += 1

        sum += 12

        last = res
    
    return res_f

def retracao_fila_ope(tamanho = 0):

    if tamanho == 2:
        return "1 2 1 "
    elif tamanho > 2:
        res = retracao_fila_ope(tamanho-1)
        n = 0

        while tamanho-n >= 1:
            res += str(tamanho-n) + " "
            n += 1

        return res
    
# variáveis

tamanho_da_fila = 0

extensao_tamanho = 0
extensao_fila = ""
retracao_tamanho = 0
retracao_fila = ""

show = "n"

# input do tamanho

tamanho_da_fila = int(input("Tamanho da fila de pistões: "))

# extensão

extensao_tamanho = extensao_ope(tamanho_da_fila)
extensao_fila = extensao_fila_ope(tamanho_da_fila)
retracao_tamanho = retracao_ope(tamanho_da_fila)
retracao_fila = retracao_fila_ope(tamanho_da_fila)

print("Número de operações de extensão: " + str(extensao_tamanho))
print("Número de operações de retração: " + str(retracao_tamanho))
show = input("Mostrar filas(s/n)?")

if show == "s":
    print("Fila de extensão: " + str(extensao_fila))
    print("Fila de retração: " + str(retracao_fila))