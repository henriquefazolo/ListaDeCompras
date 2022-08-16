class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def menu_principal(self):
        try:
            self.model.deletar_listas_vazias()
            opcao = self.view.menu_principal(self.model.menu_principal())
            if opcao == '1':
                self.menu_cadastro_lista()
            elif opcao == '2':
                self.menu_ver_listas_cadastradas()
            elif opcao == '0':
                exit()
            else:
                self.menu_principal()
        except Exception as e:
            print(e)

    def menu_cadastro_lista(self):
        try:
            opcao = self.view.menu_cadastro_lista(self.model.menu_cadastro_lista())
            if opcao == '0':
                self.menu_principal()
            else:
                self.menu_cadastro_itens_lista()
        except Exception as e:
            print(e)

    def menu_cadastro_itens_lista(self):
        try:

            item = self.view.menu_cadastro_itens_lista(self.model.menu_cadastro_itens_lista())
            if item[0] == '0' or item[1] == '0':
                self.menu_principal()
            else:
                self.view.valor_salvo_com_sucesso(self.model.salvar_cadastro_item(item[0], item[1]))
                self.menu_cadastro_itens_lista()
        except Exception as e:
            print(e)



    def menu_ver_listas_cadastradas(self):
        try:
            listas = self.model.ver_listas_cadastradas()
            opcao = self.view.menu_ver_listas_cadastradas(self.model.menu_ver_listas_cadastradas(item=listas))
            if opcao == '0':
                self.menu_principal()
            else:
                self.menu_lista_acessada(opcao)
        except Exception as e:
            print(e)

    def menu_lista_acessada(self, opcao):
        try:
            lista_atual = opcao
            itens = self.model.ver_itens_lista_selecionada(opcao)
            opcao = self.view.menu_lista_acessada(self.model.menu_lista_acessada(item=itens))
            if opcao == '0':
                self.menu_principal()
            elif opcao == '1':
                self.ir_as_compras(lista_atual)
            elif opcao == '2':
                self.adicionar_item_nesta_lista(lista_atual)
            elif opcao == '3':
                self.remover_item_nesta_lista(lista_atual)
        except Exception as e:
            print(e)

    def ir_as_compras(self, lista_atual):
        try:
            opcao = self.view.ir_as_compras(self.model.ir_as_compras(self.model.crud_itens_no_carrinho(lista_atual)[0],
                                                                     self.model.crud_itens_no_carrinho(lista_atual)[1]))
            if opcao == '0':
                self.menu_lista_acessada(lista_atual)
            else:
                item = self.model.crud_itens_no_carrinho(lista_atual, opcao)
                self.model.atualizar_carrinho(item[2])
                self.ir_as_compras(lista_atual)
        finally:
            self.compras_finalizadas()

    def adicionar_item_nesta_lista(self, lista_atual):
        try:
            opcao = self.view.adicionar_item_nesta_lista(self.model.adicionar_item_nesta_lista())
            if opcao == '0':
                self.menu_lista_acessada(lista_atual)
        except Exception as e:
            print(e)

    def remover_item_nesta_lista(self, lista_atual):
        try:
            opcao = self.view.remover_item_nesta_lista(self.model.remover_item_nesta_lista())
            if opcao == '0':
                self.menu_lista_acessada(lista_atual)
        except Exception as e:
            print(e)

    def compras_finalizadas(self):
        try:
            self.view.compras_finalizadas(self.model.compras_finalizadas())
            self.menu_ver_listas_cadastradas()
        except Exception as e:
            print(e)