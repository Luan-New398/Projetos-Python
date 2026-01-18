import os
restaurantes = [
                {'nome':'El Cagado', 'categoria':'Open bar', 'ativo':True},
                {'nome':'Tio Sapo', 'categoria':'Pizzaria', 'ativo':False},
                {'nome':'Sabo', 'categoria':'Shopping', 'ativo':True},
                {'nome':'Sequilhos', 'categoria':'Ortifruti', 'ativo':False}
]

def volte_menu():
    input('\nEnter para voltar ao menu\n')
    main()

def subtitulo(txt):
    os.system('cls')
    linha = '*' * (len(txt) + 4)
    print(linha)
    print(txt)
    print(linha)

def liste_restaurente():
    '''
    Lista do dicionário 'restaurantes'
     '''
    subtitulo('Restaurantes cadastrados')
    print(f'{'Nome'.ljust(18)} | {'Categoria'.ljust(15)} | Status')
    for restaurente in restaurantes:
        r_nome = restaurente['nome']
        r_categoria = restaurente['categoria']
        r_ativo = 'Ativado' if restaurente['ativo'] else 'Dasetivado'
        print(f'-> {r_nome.ljust(15)} | {r_categoria.ljust(15)} | {r_ativo}')
    volte_menu()

def irregular():
    print('Opção irregular, escolha novante entre as opções conhecidas:')
    volte_menu()

def cadastre_restaurente():
    ''' 
    Aqui cadastra um novo restaurente 
    
    Inputs:
    - Nome restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista, com status 'desabilitado' por padrão
    '''
    subtitulo('Cadastre o restaurante')
    nome_restaurante = input('Digite o nome do restaurente:\n')
    categoria = input('Digite a cetegoria do restaurente:\n')
    r_dados = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(r_dados)
    print(f'Restaurente {nome_restaurante} cadastrado')
    volte_menu()

def ativacao():
    '''
    Altera o status do restaurante entre 'ativado' e 'desativado'

    Inputs:
    ' Nome restaurante

    Outputs:
    Altera o status do restaurante, caso haja um restaurante com o nome procurado
    '''
    subtitulo('Ative e/ou desative restaurante')
    nome_restaurente = input('Digite o nome do restaurante:\n')
    r_procura = False
    for restaurante in restaurantes:
        if nome_restaurente == restaurante['nome']:
            r_procura = True
            restaurante['ativo'] = not restaurante['ativo']
            msg = f'O restaurante {nome_restaurente} foi ativado' if restaurante['ativo'] else f'O restaurante {nome_restaurente} foi desativado'
            print(msg)
    if not r_procura:
        print('Não encontrado')
    volte_menu()

def mostra_nome():
    os.system('cls')
    print('''
    █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ █▀▀ █▄░█ ▀█▀ █▀▀ █▀   █▀ ▄▀█ █▄▄ █▀█ █▀█ █▀█ █▀ █▀█ █▀ █
    █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ ██▄ █░▀█ ░█░ ██▄ ▄█   ▄█ █▀█ █▄█ █▄█ █▀▄ █▄█ ▄█ █▄█ ▄█ ▄
      ''')

def mostra_opcoes():
    print('1. Cadastro de restaurante')
    print('2 Listar restaurente')
    print('3 Ativar restaurente')
    print('4 Sair\n')

def escolhe_opcao():
    try:
        escolhido = int(input('Escolhe a opção:\n'))
        print(f'Foi escolhido {escolhido}\n')
        if escolhido == 1:
            cadastre_restaurente()
        elif escolhido == 2:
            liste_restaurente()
        elif escolhido == 3:
            ativacao()
        elif escolhido == 4:
            encerrar()
        else:
            irregular()
    except:
        irregular()

def encerrar():
    os.system('cls')
    print('Encerrado\n')

def main():
    mostra_nome()
    mostra_opcoes()
    escolhe_opcao()

if __name__ == '__main__':
    main()