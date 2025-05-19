texto = input("Digite uma palavra ou texto: ")

bigramas = [texto[posicao_inicial:posicao_inicial+2] for posicao_inicial in range(len(texto)-1)]

bigramas_unicos = []  
for bigrama in bigramas:
    if bigrama not in bigramas_unicos:
        bigramas_unicos.append(bigrama)

print(f"Bigramas encontrados: {bigramas}")
print(f"Bigramas únicos: {bigramas_unicos}")
print(f"Número de bigramas únicos: {len(bigramas_unicos)}")
