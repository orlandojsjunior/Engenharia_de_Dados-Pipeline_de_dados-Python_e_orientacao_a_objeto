import json
import csv


# Funções
def leitura_jason(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json


def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv


def leitura_dados(path, tipo_arquivo):
    dados = []
    if tipo_arquivo == 'json':
        dados = leitura_jason(path)
    elif tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    return dados


def get_columns(dados):
    return list(dados[0].keys())


def rename_columns(dados, key_mapping):
    new_dados_csv = []
    
    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
    return new_dados_csv


# Definindo os paths dos arquivos
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


# Iniciando a leitura
dados_json = leitura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
print(f"Nome colunas dados JSON: {nome_colunas_json}")

dados_csv = leitura_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
print(f"Nome colunas dados CSV: {nome_colunas_csv}")


key_mapping = {'Nome do Item': 'Nome do Produto',
                            'Classificação do Produto': 'Categoria do Produto',
                            'Valor em Reais (R$)': 'Preço do Produto (R$)',
                            'Quantidade em Estoque': 'Quantidade em Estoque',
                            'Nome da Loja': 'Filial',
                            'Data da Venda': 'Data da Venda'}
key_mapping


# Transformação dos dados

dados_csv = rename_columns(dados_csv, key_mapping)

nome_colunas_csv = get_columns(dados_csv)

print(f"Nome colunas Renomadas: {nome_colunas_csv}")