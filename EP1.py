import json
acao=int(input(''' 
Controle do estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque
Faça sua escolha: '''))
estoque=dict()
while acao!=0:
    if acao==1:
        produto=input('Nome do produto: ')
        if produto not in estoque:
            quantidade=int(input('Quantidade inicial: '))
            while quantidade<0:
                print('A quantidade inicial não pode ser negativa.')
                quantidade=int(input('Quantidade inicial: '))
            estoque[produto]={'quantidade':quantidade}
        else:
            print('Produto já cadastrado.')
    elif acao==2:
        produto=input('Nome do produto: ')
        if produto not in estoque:
            print('Elemento não encontrado.')
        else:
            del estoque[produto]
    elif acao==3:
        produto=input('Nome do produto: ')
        if produto not in estoque:
            print('Elemento não encontrado.')
        else:
            quantidade=int(input('Quantidade: '))
            estoque[produto]['quantidade']+=quantidade
    elif acao==4:
        for produto in estoque:
            print('{0} : {1}'.format(produto, estoque[produto]['quantidade']))
    acao=int(input(''' 
Controle do estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque
Faça sua escolha: '''))
dicionario=json.dumps(estoque, sort_keys=True, indent=4)
print("Até mais!")