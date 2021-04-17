import random

def func_minimiza(qnt_obj, Volume_obj, Volume_rec): 
    
    for j in range(qnt_obj):  #verifica se os objetos cabem no recipiente.
      if Volume_obj[j]>Volume_rec:
        print('\n')
        print(f'Um dos objetos não cabem no recipiente de volume {Volume_rec}')
        return qnt_recipientes  
    
      Aux_volume_rec = Volume_rec
      qnt_recipientes = 1 
      for i in range(qnt_obj): 
        if Aux_volume_rec >= Volume_obj[i]: 
          Aux_volume_rec = Aux_volume_rec - Volume_obj[i] 
        else: 
          qnt_recipientes += 1
          Aux_volume_rec = Volume_rec - Volume_obj[i] 
    return qnt_recipientes 
Volume_dos_obj =[1,5,4,7,2,3,8,1,5,4,7,2,3,8]
qnt_entradas = len(Volume_dos_obj)
V=10

k=0
melhor_sol = 1000000

while k<10:
  k +=1
  random.shuffle(Volume_dos_obj) #Embaralha o vetor
  sol = func_minimiza(qnt_entradas, Volume_dos_obj, V)
  print(f'{Volume_dos_obj}: {sol}') #Imprime as soluções geradas
  if sol < melhor_sol:
      melhor_sol = sol

print(f'A melhor solução encontrada foi {melhor_sol}')