escolha=int(input(''' 
Controle do estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque
Faça sua escolha: '''))
produtos=dict()
if escolha==0:
    print("Até mais!")
elif escolha==1:
    nome=input('Nome do produto: ')
    quantidade=int(input('Quantidade inicial'))
    while quantidade<0:
        print('A quantidade inicial não pode ser negativa.')
        quantidade=int(input('Quantidade inicial: '))
        