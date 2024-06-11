import pandas as pd
import json

# Carregando a planilha em um DataFrame
df = pd.read_excel('C:/Users/Dell/Downloads/pedidos.xlsx')

# Função para transformar a coluna JSON em colunas
def expandir_linha(row):
    # Transformando a coluna com o JSON em uma lista de dicionários
    dados_json = json.loads(row['pedido-itens'])

    # Criando um dicionário para armazenar os valores de cada item no JSON
    nova_linha = {}

    # Adicionando as informações de cada item no JSON ao dicionário
    for item in dados_json:
        for chave, valor in item.items():
            nova_chave = chave + '_' + str(item['linha'])
            nova_linha[nova_chave] = valor

    # Adicionando as informações das outras colunas ao dicionário
    for coluna in df.columns:
        if coluna != 'pedido-itens':
            nova_chave = coluna
            nova_linha[nova_chave] = row[coluna]

    return nova_linha

# Aplicando a função a cada linha da planilha e concatenando os resultados
df_explodido = pd.concat([pd.DataFrame(expandir_linha(row), index=[0]) for _, row in df.iterrows()], ignore_index=True)

# Selecionando apenas as colunas desejadas
colunas_selecionadas = ['quantidade_1', 'preco_cheio_1', 'preco_promocional_1', 'preco_venda_1', 'preco_custo_1', 'produto_id_1']
df_explodido = df_explodido[colunas_selecionadas]

# Removendo as linhas com valores nulos
df_explodido.dropna(inplace=True)

# Excluindo duplicatas
df_explodido.drop_duplicates(inplace=True)

# Resetando o índice do DataFrame
df_explodido.reset_index(drop=True, inplace=True)

# Salvando o novo DataFrame em um arquivo Excel
df_explodido.to_excel('C:/Users/Dell/Downloads/novo_arquivo.xlsx', index=False)
