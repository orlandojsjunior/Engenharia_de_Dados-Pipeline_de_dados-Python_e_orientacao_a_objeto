# Importando a classe

from processamento_dados import Dados


# Definindo os paths dos arquivos

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


# Extract

dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f"Nomes colunas empresa A: {dados_empresaA.nome_colunas}")
print(f"Quantidade de linhas empresa A: {dados_empresaA.qtd_linhas}")


dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f"Nomes colunas empresa B: {dados_empresaB.nome_colunas}")
print(f"Quantidade de linhas empresa B: {dados_empresaB.qtd_linhas}")


# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                            'Classificação do Produto': 'Categoria do Produto',
                            'Valor em Reais (R$)': 'Preço do Produto (R$)',
                            'Quantidade em Estoque': 'Quantidade em Estoque',
                            'Nome da Loja': 'Filial',
                            'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(f"Nomes colunas Atualizado: {dados_empresaB.nome_colunas}")


dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Nomes colunas após fusão: {dados_fusao.nome_colunas}")
print(f"Quantidades de linhas após fusão: {dados_fusao.qtd_linhas}")


# Load

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Os dados foram salvos em: {path_dados_combinados}")


