import pandas as pd
import json

# Carregar a planilha em um DataFrame
df = pd.read_excel('C:/Users/Dell/Downloads/pedidos.xlsx')

# Função para transformar a coluna JSON em colunas
def expandir_linha(row):
    try:
        dados_json = json.loads(row['pedido-itens'])
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON na linha {row.name}: {e}")
        return None

    novas_linhas = []
    for item in dados_json:
        nova_linha = {}
        for chave, valor in item.items():
            nova_linha[chave] = valor

        for coluna in df.columns:
            if coluna != 'pedido-itens':
                nova_linha[coluna] = row[coluna]

        novas_linhas.append(nova_linha)

    return novas_linhas

linhas_expandidas = []
for _, row in df.iterrows():
    novas_linhas = expandir_linha(row)
    if novas_linhas is not None:
        linhas_expandidas.extend(novas_linhas)

df_explodido = pd.DataFrame(linhas_expandidas)

colunas_selecionadas = [
    'pedido-numero', 'quantidade', 'preco_cheio', 'preco_promocional', 
    'preco_venda', 'preco_custo', 'produto_id'
]

df_explodido = df_explodido[colunas_selecionadas]

df_explodido.dropna(subset=['pedido-numero'], inplace=True)

df_explodido.reset_index(drop=True, inplace=True)

df_explodido.to_excel('C:/Users/Dell/Downloads/novo_arquivo.xlsx', index=False)
