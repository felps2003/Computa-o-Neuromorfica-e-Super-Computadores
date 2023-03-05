import os
import numpy as np
import pandas as pd

# Define o caminho para o diretório /opt (que existe no linux), nesse caso como o meu sistema é windows, acabei por criar um diretorio chamado opt no projeto e coloquei o csv la dentro

diretorio = r"opt/"

# Lista todos os arquivos com a extensão .csv no diretório /opt
arquivos_csv = [os.path.join(diretorio, arquivo) for arquivo in os.listdir(diretorio) if arquivo.endswith(".csv")]

# Para cada arquivo CSV, carrega os dados, calcula a distância euclidiana entre todos os pontos e imprime os pontos mais próximos
for arquivo_csv in arquivos_csv:
    # Lê o arquivo CSV, especificando que o separador decimal é a vírgula
    dados = pd.read_csv(arquivo_csv, decimal=",")
    
    # Cria uma lista com todas as coordenadas do arquivo
    coordenadas = [(linha["source"], linha["destiny"]) for _, linha in dados.iterrows()]
    
    # Calcula a distância euclidiana entre todos os pontos
    distancias = []
    for i in range(len(coordenadas)):
        for j in range(i+1, len(coordenadas)):
            ponto1 = np.array([float(coordenadas[i][0]), float(coordenadas[i][1])])
            ponto2 = np.array([float(coordenadas[j][0]), float(coordenadas[j][1])])
            distancia = np.linalg.norm(ponto2 - ponto1)
            distancias.append((i, j, distancia))
    
    # Encontra os pontos com a menor distância euclidiana
    menor_distancia = min(distancias, key=lambda x: x[2])
    ponto1 = coordenadas[menor_distancia[0]]
    ponto2 = coordenadas[menor_distancia[1]]
    print(f"Os pontos mais próximos em {arquivo_csv} são {ponto1} e {ponto2}, com distância {menor_distancia[2]}")
    
    # Remove o arquivo CSV
    os.remove(arquivo_csv)



