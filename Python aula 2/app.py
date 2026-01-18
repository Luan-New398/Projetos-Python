import os
from Modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('praça','gourmet')
restaurante_praca.recebe_av('Lu',2)
restaurante_praca.recebe_av('NaN',5)
restaurante_praca.recebe_av('NaN',98)
restaurante_praca.recebe_av('Ga',4)
restaurante_mexico = Restaurante('max-food','Mexicano')
restaurante_mexico.recebe_av('Padre',1)
restaurante_mexico.alt_estado()
restaurante_pinguco = Restaurante('bar do Pinguço','open bar')
restaurante_praca.liste_c()

def titulo():
    os.system('cls')
    print( '''
██████╗░███████╗███╗░░░███╗  ██╗░░░██╗██╗███╗░░██╗██████╗░░█████╗░██╗
██╔══██╗██╔════╝████╗░████║  ██║░░░██║██║████╗░██║██╔══██╗██╔══██╗██║
██████╦╝█████╗░░██╔████╔██║  ╚██╗░██╔╝██║██╔██╗██║██║░░██║██║░░██║██║
██╔══██╗██╔══╝░░██║╚██╔╝██║  ░╚████╔╝░██║██║╚████║██║░░██║██║░░██║╚═╝
██████╦╝███████╗██║░╚═╝░██║  ░░╚██╔╝░░██║██║░╚███║██████╔╝╚█████╔╝██╗
╚═════╝░╚══════╝╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝\n''')

def subtitulo(txt):
    os.system('cls')
    linha = '*' * (len(txt) + 4)
    print(linha)
    print(txt)
    print(linha)

def volte_menu():
    input('\nEnter para voltar ao menu\n')
    main()

def irregular():
    print('Opção irregular, escolha novante entre as opções conhecidas:')
    volte_menu()

def encerrar():
    os.system('cls')
    print('Encerrado\n')

def opcoes():
    print('1 Listar restaurantes')
    print('2 Listar avaliações')
    print('3 Ativar/Desativar restaurante')
    print('4 Adicionar restaurante')
    print('5 Adicionar avaliação')
    print('6 Sair')
    selecionar()

def selecionar():
        try:
            escolhido = int(input('Escolhe a opção:\n'))
            print(f'Foi escolhido {escolhido}\n')
            if escolhido == 1:
                Restaurante.liste_r()
                volte_menu()
            elif escolhido == 2:
                liste_avaliacao()
                volte_menu()
            elif escolhido == 3:
                ativacao()
            elif escolhido == 4:
                cadastre_restaurente()
            elif escolhido == 5:
                adicione_avaliacao()
            elif escolhido == 6:
                encerrar()
            else:
                irregular()
        except:
            irregular()

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
    #r_dados = {nome_restaurante, categoria}
    restaurante = Restaurante(nome_restaurante,categoria)
    print(f'Restaurente {nome_restaurante} cadastrado')
    volte_menu()

def liste_avaliacao():
    subtitulo('Lista de Avaliações')
    nome_restaurante = input('Digite o nome do restaurante:\n').title() # Adicionei .title() para bater com o init
    r_procura = False
    
    for restaurante in Restaurante.restaurantes:
        if nome_restaurante == restaurante._nome: # Agora os nomes vão bater
            r_procura = True
            restaurante.liste_c() # CHAMADA CORRETA: O objeto chama o método
            
    if not r_procura:
        print('O restaurante informado não foi encontrado.')
    volte_menu()

def ativacao():
    subtitulo('Ative e/ou desative restaurante')
    nome_restaurente = input('Digite o nome do restaurante:\n').title()
    r_procura = False
    for restaurante in Restaurante.restaurantes:
        if nome_restaurente == restaurante._nome:
            r_procura = True
            restaurante.alt_estado()
            msg = f'O restaurante {nome_restaurente} foi ativado' if restaurante._ativo else f'O restaurante {nome_restaurente} foi desativado'
            print(msg)
    if not r_procura:
        print('Não encontrado')
    volte_menu()

def adicione_avaliacao():
    subtitulo('Avalie um restaurante')
    nome_restaurente = input('Digite o nome do restaurante:\n').title()
    nome_cliente = input('Digite seu nome:\n')
    nota = int(input('Dê uma nota de 1 a 5:\n'))
    r_procura = False
    for restaurante in Restaurante.restaurantes:
        if nome_restaurente == restaurante._nome:
            r_procura = True
            restaurante.recebe_av(nome_cliente,nota)
            msg = f'O restaurante {nome_restaurente} foi avaliado'
            print(msg)
    if not r_procura:
        print('Não encontrado')
    volte_menu()

def main():
    titulo()
    opcoes()
    pass

if __name__ == '__main__':
    main()