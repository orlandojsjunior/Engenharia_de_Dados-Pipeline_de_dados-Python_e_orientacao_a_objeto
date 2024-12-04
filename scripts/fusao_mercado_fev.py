import json
import csv



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

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


dados_json = leitura_dados(path_json, 'json')
print(dados_json[0])

dados_csv = leitura_dados(path_csv, 'csv')
print(dados_csv[0])




