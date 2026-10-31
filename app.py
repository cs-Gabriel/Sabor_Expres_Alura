import os

restaurantes = [{'nome': 'Praça' , 'categoria':'Japonesa', 'ativo':False},
                {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]


def exibir_nome_do_programa():
    ''' Exibe o nome do programa '''

    print('''🅢 🅐 🅑 🅞 🅡  🅔 🅧 🅟 🅡 🅔 🜁
''')

def exibir_opcoes():
    ''' Exibe as opções do programa '''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    ''' Função para voltar ao menu principal '''

    input('\nPrecione qualquer tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    ''' Função para finalizar o app '''

    exibir_subtitulo('Finalizando o app')

def opcao_invalida():
    ''' Função para tratar opção invalida '''

    print('Opção invalida!\n')
    voltar_ao_menu_principal()


def cadastrar_restaurante():
    '''
    Função para cadastrar um novo restaurante.

    Inputs: Nome do restaurante e categoria do restaurante
    Outputs: Nenhum
    '''
    exibir_subtitulo('Cadasto de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Função para listar os restaurantes.

    Inputs: Nenhum
    Outputs: Nenhum
    '''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(24)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(22)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''
    Função para alterar o estado de um restaurante.

    Inputs: Nenhum
    Outputs: Nenhum
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')

    voltar_ao_menu_principal()



def escolher_opcao():
    ''' Função para escolher a opção do menu principal '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''' Função principal do programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()