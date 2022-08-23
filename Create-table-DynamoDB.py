#Criação de tables no DynamoDB

import boto3

def criar_tabela_filmes():
    dynamodb = boto3.resource('dynamodb')
    tabela = dynamodb.create_table(
        TableName='Filmes',
        KeySchema=[
            {
                'AttributeName': 'titulo',
                'KeyType': 'HASH'  # Chave de Partição
            },
            {
                'AttributeName': 'ano',
                'KeyType': 'RANGE'  # Chave de Classificação
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'titulo',
                'AttributeType': 'S'  # String
            },
            {
                'AttributeName': 'ano',
                'AttributeType': 'N'  # Number
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return tabela

tabela_filmes = criar_tabela_filmes()
print('Status da tabela:', tabela_filmes.table_status)