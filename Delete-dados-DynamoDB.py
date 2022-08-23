#Delete de dados no DynamoDB

import boto3

def apagar_filme(titulo, ano):
    dynamodb = boto3.resource('dynamodb')
    tabela = dynamodb.Table('Filmes')
    tabela.delete_item(
        Key={
            'titulo': titulo,
            'ano': ano,
        }
    )

apagar_filme('Bacurau', 2019)