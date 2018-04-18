# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:44:18 2018

@author: FERNANDO
"""
produtos={}
acao=int(input('''Controle de estoque
            0 - sair
            1 - adicionar item
            2 - remover item
            3 - alterar item
            4 - imprimir estoque
            Faça sua escolha: '''))

while acao!=0:
    if acao == 1:
        produto = input('Qual o produto?')
        if produto in produtos:
                print('Produto ja está cadastrado')
        else:
            quantidade = int(input('Quantidade?'))    
            while quantidade < 0:
                print('Só é aceito numero positivo')
                quantidade = int(input('Quantidade?'))
            produtos[produto] = quantidade
        acao=int(input('''Controle de estoque
            0 - sair
            1 - adicionar item
            2 - remover item
            3 - alterar item
            4 - imprimir estoque
            Faça sua escolha: '''))
    elif acao == 2:
        produto = input('Nome do produto:')
        if produto not in produtos:
            print('Elemento não encontrado')
            acao=int(input('''Controle de estoque
            0 - sair
            1 - adicionar item
            2 - remover item
            3 - alterar item
            4 - imprimir estoque
            Faça sua escolha: '''))
        else:
            del produtos[produto]
            acao=int(input('''Controle de estoque
            0 - sair
            1 - adicionar item
            2 - remover item
            3 - alterar item
            4 - imprimir estoque
            Faça sua escolha: '''))
print(produtos)