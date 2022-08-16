import os
from colorama import init
from colorama import Fore, Style

init()


class View:
    def __init__(self):
        self.__controller = None

    cor_texto_inicial = Fore.CYAN + Style.BRIGHT
    cor_item = Fore.RESET + Style.RESET_ALL
    cor_opcoes = Fore.CYAN
    cor_texto_final = Fore.LIGHTRED_EX + Style.NORMAL
    cor_input = Fore.RESET + Style.RESET_ALL

    @staticmethod
    def menu_principal(retorno, cor_texto_inicial=cor_texto_inicial, cor_item=cor_item, cor_opcoes=cor_opcoes,
                       cor_texto_final=cor_texto_final, cor_input=cor_input):
        View.limpar_tela()
        print(cor_texto_inicial + retorno[0][0])
        print(retorno[0][1])
        print(cor_item + retorno[1])
        print(cor_opcoes + retorno[2])
        print(cor_texto_final + retorno[3])
        return str(input(cor_input))

    @staticmethod
    def menu_cadastro_lista(retorno, cor_texto_inicial=cor_texto_inicial, cor_item=cor_item, cor_opcoes=cor_opcoes,
                            cor_texto_final=cor_texto_final, cor_input=cor_input):
        View.limpar_tela()
        print(cor_texto_inicial + retorno[0][0])
        print(retorno[0][1])
        print(cor_item + retorno[1])
        print(cor_opcoes + retorno[2])
        print(cor_texto_final + retorno[3])
        return str(input(cor_input))

    @staticmethod
    def menu_cadastro_itens_lista(retorno, cor_texto_inicial=cor_texto_inicial, cor_item=cor_item,
                                  cor_opcoes=cor_opcoes, cor_texto_final=cor_texto_final, cor_input=cor_input):
        View.limpar_tela()
        print(cor_texto_inicial + retorno[0][0])
        print(retorno[0][1])
        print(cor_texto_final + retorno[3])
        print(cor_item + retorno[1])
        print(cor_opcoes + retorno[2][0])
        item = str(input(cor_input))
        if item == '0':
            return item
        print(cor_opcoes + retorno[2][1])
        quantidade = str(input(cor_input))
        print(cor_texto_final + retorno[3])
        return item, quantidade

    @staticmethod
    def menu_ver_listas_cadastradas(retorno, cor_texto_inicial=cor_texto_inicial, cor_item=cor_item,
                                    cor_opcoes=cor_opcoes, cor_texto_final=cor_texto_final, cor_input=cor_input):
        View.limpar_tela()
        print(cor_texto_inicial + retorno[0][0])
        print(retorno[0][1])
        print()
        for i in retorno[1]:
            print(cor_item + i)
        print(cor_opcoes + retorno[2])
        print(cor_texto_final + retorno[3])
        return str(input(cor_input))

    @staticmethod
    def menu_lista_acessada(retorno, cor_texto_inicial=cor_texto_inicial, cor_item=cor_item, cor_opcoes=cor_opcoes,
                            cor_texto_final=cor_texto_final, cor_input=cor_input):
        View.limpar_tela()
        print(cor_texto_inicial + retorno[0][0])
        print(retorno[0][1])
        print()
        for i in retorno[1]:
            print(cor_item + i)
        print('\n')
        print(cor_opcoes + retorno[2])
        print(cor_texto_final + retorno[3])
        return str(input(cor_input))

    @staticmethod
    def ir_as_compras(retorno, cor_texto_inicial=cor_texto_inicial, cor_item=cor_item, cor_opcoes=cor_opcoes,
                      cor_texto_final=cor_texto_final, cor_input=cor_input):
        View.limpar_tela()
        print(cor_texto_inicial + retorno[0][0])
        print(retorno[0][1])
        print(cor_item + retorno[1][0])

        for i in retorno[1][2]:
            print(i)

        print(cor_item + retorno[1][1])
        for i in retorno[1][3]:
            print(i)

        print(cor_opcoes + retorno[2])
        print(cor_texto_final + retorno[3])
        return str(input(cor_input))

    @staticmethod
    def adicionar_item_nesta_lista(retorno, cor_texto_inicial=cor_texto_inicial, cor_item=cor_item,
                                   cor_opcoes=cor_opcoes, cor_texto_final=cor_texto_final, cor_input=cor_input):
        View.limpar_tela()
        print(cor_texto_inicial + retorno[0][0])
        print(retorno[0][1])
        print(cor_item + retorno[1])
        print(cor_opcoes + retorno[2])
        print(cor_texto_final + retorno[3])
        return str(input(cor_input))

    @staticmethod
    def remover_item_nesta_lista(retorno, cor_texto_inicial=cor_texto_inicial, cor_item=cor_item, cor_opcoes=cor_opcoes,
                                 cor_texto_final=cor_texto_final, cor_input=cor_input):
        View.limpar_tela()
        print(cor_texto_inicial + retorno[0][0])
        print(retorno[0][1])
        print(cor_item + retorno[1])
        print(cor_opcoes + retorno[2])
        print(cor_texto_final + retorno[3])
        return str(input(cor_input))

    @staticmethod
    def compras_finalizadas(retorno, cor_texto_inicial=cor_texto_inicial, cor_item=cor_item, cor_opcoes=cor_opcoes,
                            cor_texto_final=cor_texto_final, cor_input=cor_input):
        View.limpar_tela()
        print(cor_texto_inicial + retorno[0][0])
        print(retorno[0][1])
        print(cor_item + retorno[1])
        print(cor_opcoes + retorno[2])
        print(cor_texto_final + retorno[3])
        return str(input(cor_input))

    @staticmethod
    def limpar_tela():
        return os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def valor_salvo_com_sucesso(valor, cor_item=cor_item):
        return print(cor_item + f'{valor}: Salvo com sucesso!')
