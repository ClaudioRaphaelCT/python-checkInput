from src.Random import Random
from src.Input import Input

numeros_aleatorios = Random.gerar_numero_aleatorio()
numeros_digitados = Input.validar_input()
existem_em_aleatorios = []
nao_existem_em_aleatorios =[]
corretos_na_posicao = []

for i in range(len(numeros_digitados)):
    if numeros_digitados[i] == numeros_aleatorios[i]:
        corretos_na_posicao.append(numeros_digitados[i])
    elif numeros_digitados[i] in numeros_aleatorios:
        existem_em_aleatorios.append(numeros_digitados[i])
    else:
        nao_existem_em_aleatorios.append(numeros_digitados[i])

print(f'Acertos na posição correta: {len(corretos_na_posicao)}')
print(f'Os números corretos na posição correta: {", ".join(map(str, corretos_na_posicao))}')

print(f'Acertos fora da posição correta: {len(existem_em_aleatorios)}')
print(f'Os números corretos fora da posição correta: {", ".join(map(str, existem_em_aleatorios))}')

print(f'Números incorretos: {len(nao_existem_em_aleatorios)}')
print(f'Os números incorretos: {", ".join(map(str, nao_existem_em_aleatorios))}')
