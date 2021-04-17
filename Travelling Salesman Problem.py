import time

valores = [] #Matriz que armazenará os dados 
soma = 0 #Caminho percorrido
caminho =[] #Salvará as cidades visitadas

with open("C:\Users\Beatriz\Desktop\GitHub\Otimização\26 cidades.txt",'r') as f:
    for line in f.readlines():
      vet = line.split('  ')
      results=[]
      valores.append(results)
      for i in range(len(vet)):
        vet[i]=int(float(vet[i]))
        results.append(vet[i])

tamanho = len(valores) #Tamanho do vetor de cada linha da matriz

"""
for l in range(tamanho): #Caso queira imprimir as matrizes a cada visita em uma nova cidade 
   print(valores[l])
"""

substitui = [] #Matrizes que serão preenchidas com -1 (marcador de que a cidade já foi visitada);
for i in range(tamanho):
    substitui.append(-1)
 
linha_controle = 0 #Salvará a linha da cidade em que teremos que ir, pois está possuirá a menor distância;
c = 0 #Cidade origem, ou seja, neste caso estamos iniciando na cidade 0 (coluna 0);
saltos = 0 #Quantidade de cidades que precisaremos visitar, partindo da cidade origem, temos n-1 cidades inicialmente.

ini1=time.time() #Inicialização do primeiro contador de tempo
while saltos < tamanho-1:
    menor = 100000 
    for l in range(tamanho):
        if menor > int(valores[l][c]) and int(valores[l][c]) > 0: #Verificando qual é a menor distância na coluna (a cidade cuja a distância seja a menor possível) 
            menor = valores[l][c] #salva a distância do percurso
            linha_controle = l #salva a linha, ou seja, a próxima cidade que será visitada
    caminho.append(c) #Adiciona a cidade visita
    valores[c] = substitui.copy() #Marca que a cidade já foi visitada
    c = linha_controle #A próxima cidade que será visitada será a nova coluna c
    saltos += 1 #atualiza o salto
    #print('A menor distância é:', menor)
    soma += menor #Armazenamos a distância percorrida
fim1=time.time() #Finalização do primeiro contador de tempo
tot1=fim1-ini1 #Atribuição do tempo total 1


ini2=time.time() #Inicialização do segundo contador de tempo
ultimo=100000
for l in range(tamanho):
  """
  Retornaremos a cidade origem, neste momento,n-1 linhas estarão preenchidas com o marcador -1,
  então terá apenas uma posição em que o valor será maior que 0, ou seja, exatamente 
  o valor que precisaremos para encontrar a distância.
  Como sabemos que a cidade origem está na coluna 0, então basta percorre-lá até encontrar a distância.  
  """
  if ultimo > int(valores[l][0]) and int(valores[l][0]) > 0:
    ultimo=int(valores[l][0])
    c=l

caminho.append(c)
#print('Distância para origem:',ultimo)
soma +=ultimo #Armazeno a distância da cidade em que o caixeiro enconra-se até a cidade origem
fim2=time.time() #Finalização do segundo contador de tempo
tot2=fim2-ini2 #Atribuição do tempo total 2
print(caminho)
print('Resultado final:', soma)
print(f'Tempo de execução: {tot1+tot2} segundos')