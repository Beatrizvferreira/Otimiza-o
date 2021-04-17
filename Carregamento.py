#Método Guloso

from random import random
import time

class Produto():
    def __init__(self, nome, espaco, valor, razao):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor
        self.razao = razao

if __name__ == '__main__':
    lista_produtos = []
    produtos_selecionados = []
    nomes_mostrados = []
    valores_mostrados = []
    quantidade_mostrada = []
    controle_valor = 0
    valor = 0
    espaco_ocupado = 0
    
    nome_produto = ['Geladeira Brastemp', 'PS5', 'TV 65', 'Fogão Brastemp', 'Lava louças', 'Ar condicionado',
                    'Sofá', 'Conjunto sala de jantar', 'Painel para TV', 'Purificador de água', 'Máquina de lavar roupa',
                    'Cama de solteiro', 'Cama de casal', 'Notebook Lenovo', 'Notebook Dell', 'Notebook Acer',
                    'Iphone 11', 'Galaxy S20 Ultra', 'Microondas Electrolux', 'Ferro de passar roupa',
                    'Aspirador de pó', 'Chuveiro', 'Ventilador', 'Guarda roupa', 'Cafeteira']
    
    espaco_produto = [1.155, 0.0105, 0.370, 0.516, 0.303, 0.7259, 2.898, 1.152, 1.294, 0.028, 0.518,
                      1.278, 2.158, 0.0018, 0.0019, 0.0016, 0.00091, 0.00011, 0.0865, 0.0259, 0.0054,
                      0.0107, 0.4, 3.348, 0.0341]
    
    valor_produto = [4859.10, 4999, 4099, 4859.10, 3999, 3379, 2492.49, 1488.02, 503.39, 1199,
                     1899.05, 930.90, 1551.03, 3699, 3899, 3609.05, 4463.07, 5299, 2429.1, 1481.89,
                     2165.89, 388.23, 284.90, 1367.90, 3484.19]
    controle = 0
    dez = 0
    
    for i in range(250):
        razao = valor_produto[controle] / espaco_produto[controle]
        lista_produtos.append(Produto(nome_produto[controle], espaco_produto[controle], valor_produto[controle], razao))
        dez += 1
        if dez == 10:
            controle += 1
            dez = 0

    lista_produtos.sort(key=lambda i: i.razao, reverse = True)

    ini = time.time()

    limite = 30
    
    for i in lista_produtos:
        if i.espaco < limite:
            produtos_selecionados.append(i)
            limite -= i.espaco
            espaco_ocupado += i.espaco
            valor += i.valor
        
    print('\nvalor final:', valor)
    print('espaco ocupado:', espaco_ocupado)
    
    quantidade = 0
    nome = produtos_selecionados[0].nome
    controle_valor = produtos_selecionados[0].valor
    
    for i in produtos_selecionados:
        if nome == i.nome:
            quantidade += 1
        else:
            nomes_mostrados.append(nome)
            valores_mostrados.append(controle_valor)
            quantidade_mostrada.append(quantidade)
            nome = i.nome
            quantidade = 1
            controle_valor = i.valor
    nomes_mostrados.append(nome)
    valores_mostrados.append(controle_valor)
    quantidade_mostrada.append(quantidade)
    
    fim = time.time()
    print(f'\nTempo de execução do algoritmo genético: {fim-ini} segundos\n')
    print('\nQuantidades e produtos que foram selecionados:\n')
    for i in range(len(nomes_mostrados)):
        print("%s - %s R$%s " % (quantidade_mostrada[i], 
                                             nomes_mostrados[i], 
                                             valores_mostrados[i]))