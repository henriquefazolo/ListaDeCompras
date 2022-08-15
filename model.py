import sqlite3


class Model:
    banco_dados = 'banco.sqlite'
    conn = sqlite3.connect(banco_dados)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS lista_compras(
        PK_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_lista TEXT NOT NULL  
        );          
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS item(
        PK_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        no_carrinho BOOLEAN,
        FK_lista INTEGER NOT NULL, 
        FOREIGN KEY (FK_lista) REFERENCES lista_compras(PK_id)
        );              
    ''')
    conn.commit()
    conn.close()

    texto_inicial = f'Super Lista de Compras\n' \
                    f'----------==========----------'

    texto_final = f'Aperte 0 (zero) para sair.\n' \


    @staticmethod
    def menu_principal():
        texto_inicial = Model.texto_inicial, 'Menu Principal'

        item = ''

        opcoes = '1 - Cadastrar Lista\n' \
                 '2 - Ver listas cadastradas\n' \

        texto_final = Model.texto_final

        return [texto_inicial, item, opcoes, texto_final]

    @staticmethod
    def menu_cadastro_lista():
        texto_inicial = Model.texto_inicial, 'Cadastrar Lista de Compras'

        item = ''

        opcoes = 'Insira um nome para esta lista de compras :'

        texto_final = Model.texto_final

        return [texto_inicial, item, opcoes, texto_final]

    @staticmethod
    def menu_cadastro_itens_lista():
        texto_inicial = Model.texto_inicial, 'Cadastrar Itens'

        item = ''

        opcoes = ['Insira o nome do item:', 'Insira a quantidade do item:']

        texto_final = Model.texto_final

        return [texto_inicial, item, opcoes, texto_final]

    @staticmethod
    def menu_ver_listas_cadastradas(item=''):
        texto_inicial = Model.texto_inicial, 'Listas Cadastradas'

        item = item

        opcoes = '\nSelecione o valor da lista para acessa-la.\n'

        texto_final = Model.texto_final

        return [texto_inicial, item, opcoes, texto_final]

    @staticmethod
    def menu_lista_acessada(texto_inicial_adcional='Itens da lista', item='Vazio\n'):
        texto_inicial = Model.texto_inicial, texto_inicial_adcional

        item = item

        opcoes = '1 - Ir ás compras com esta lista\n' \
                 '2 - Adicionar item\n' \
                 '3 - Remover item\n' \
                 '9 - Por todos itens fora do carrinho'

        texto_final = Model.texto_final

        return [texto_inicial, item, opcoes, texto_final]

    @staticmethod
    def ir_as_compras(itens_falta_pegar, itens_no_carrinho):
        texto_inicial = Model.texto_inicial, 'Fazendo Compras'

        item = ['\n---Falta Pegar---', '\n---No Carrinho---', itens_falta_pegar, itens_no_carrinho]

        opcoes = '\nDigite o número do item para mover ao carrinho.\n'

        texto_final = Model.texto_final

        return [texto_inicial, item, opcoes, texto_final]

    @staticmethod
    def compras_finalizadas():
        texto_inicial = Model.texto_inicial, 'Compra Finalizada'

        item = 'Não ha itens para comprar nesta lista.'

        opcoes = ''

        texto_final = Model.texto_final

        return [texto_inicial, item, opcoes, texto_final]

    @staticmethod
    def adicionar_item_nesta_lista():
        texto_inicial = Model.texto_inicial, 'Adicionando Item'

        item = ''

        opcoes = ''

        texto_final = Model.texto_final

        return [texto_inicial, item, opcoes, texto_final]

    @staticmethod
    def remover_item_nesta_lista():
        texto_inicial = Model.texto_inicial, 'Removendo Item'

        item = ''

        opcoes = ''

        texto_final = Model.texto_final

        return [texto_inicial, item, opcoes, texto_final]

    @staticmethod
    def salvar_cadastro_item(item, quantidade):
        try:
            conn = sqlite3.connect(Model.banco_dados)
            cursor = conn.cursor()

            ultimo_id_lista_compras = cursor.execute('''
            SELECT MAX(PK_id) FROM lista_compras
            ''').fetchone()[0]

            cursor.execute('''
            INSERT INTO item (nome, quantidade, no_carrinho, FK_lista) VALUES (?, ?, ?,?) 
            ''', (item.upper(), quantidade, False, ultimo_id_lista_compras))
            conn.commit()

            conn.close()
        except Exception as e:
            print(e)
        return item

    @staticmethod
    def salvar_cadastro_lista(lista):
        try:
            conn = sqlite3.connect(Model.banco_dados)
            cursor = conn.cursor()

            cursor.execute('''
            INSERT INTO lista_compras (nome_lista) VALUES (?) 
            ''', [lista.upper()])
            conn.commit()

            conn.close()
        except Exception as e:
            print(e)
        return lista

    @staticmethod
    def ver_listas_cadastradas():
        conn = sqlite3.connect(Model.banco_dados)
        cursor = conn.cursor()

        lista = []

        cursor.execute('''
        SELECT * from lista_compras
        ''')
        for i in cursor.fetchall():
            lista.append(f'{i[0]} - {i[1]}')

        return lista

    @staticmethod
    def ver_itens_lista_selecionada(lista):
        conn = sqlite3.connect(Model.banco_dados)
        cursor = conn.cursor()

        lista_itens = []

        cursor.execute('''
        SELECT * from item WHERE FK_lista=?
        ''', [lista])
        n = 0
        for i in cursor.fetchall():
            n += 1
            lista_itens.append(f'{n} - Item: {i[1]} - Quantidade : {i[2]}')
        conn.close()

        if len(lista_itens) > 0:
            return lista_itens
        return ['Vazio\n']

    @staticmethod
    def crud_itens_no_carrinho(lista=0, indice_item=0):
        lista = lista
        indice_item = int(indice_item) - 1

        conn = sqlite3.connect(Model.banco_dados)
        cursor = conn.cursor()
        pk_item = []
        falta_pegar = []
        cursor.execute('''
        SELECT * from item WHERE FK_lista=? AND no_carrinho=0 
        ''', [lista])
        n = 0
        for i in cursor.fetchall():
            n += 1
            pk_item.append(i[0])
            falta_pegar.append(f'{n} - Item: {i[1]} - Quantidade : {i[2]}')
        conn.close()

        conn = sqlite3.connect(Model.banco_dados)
        cursor = conn.cursor()
        no_carrinho = []
        cursor.execute('''
        SELECT * from item WHERE FK_lista=? AND no_carrinho=1 
        ''', [lista])
        n = 0
        for i in cursor.fetchall():
            n += 1
            no_carrinho.append(f'{n} - Item: {i[1]} - Quantidade : {i[2]}')
        conn.close()

        return [falta_pegar, no_carrinho,  pk_item[indice_item]]

    @staticmethod
    def atualizar_carrinho(id_remover):
        conn = sqlite3.connect(Model.banco_dados)
        cursor = conn.cursor()
        cursor.execute('''
                        UPDATE item SET no_carrinho = 1 WHERE PK_id = ?
                        ''', [id_remover])
        conn.commit()
        conn.close()

    @staticmethod
    def deletar_listas_vazias():
        pass
