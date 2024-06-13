import pandas as pd
import json

# lendo os dados da planilha
df = pd.read_excel('C:/Users/Dell/Downloads/pedidos.xlsx')

# convertendo a coluna JSON em objetos Python
df['pedido-itens'] = df['pedido-itens'].apply(json.loads)

# criando lista para armazenar as linhas duplicadas e transformadas
rows = []

# iterando sobre cada linha do DataFrame
for idx, row in df.iterrows():

    # iterando sobre cada objeto no JSON da coluna
    for json_obj in row['pedido-itens']:

        # criando um dicionário para armazenar os valores
        data_dict = {}

        # adicionando as chaves e valores do JSON ao dicionário
        for key, value in json_obj.items():
            data_dict[key] = value

        # adicionando os valores das colunas restantes ao dicionário
        for column in df.columns:
            if column != 'pedido-itens':
                data_dict[column] = row[column]

        # adicionando o dicionário resultante à lista de linhas
        rows.append(data_dict)

# criando um novo DataFrame a partir da lista de linhas
new_df = pd.DataFrame(rows)

# exportando o novo DataFrame para um arquivo Excel
new_df.to_excel('C:/Users/Dell/Downloads/pedidos-expandidos.xlsx', index=False)

print("concluido")
