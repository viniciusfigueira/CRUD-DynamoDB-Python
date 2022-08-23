#Drop Table DynamoDB

import boto3

def apagar_tabela_filmes():
    dynamodb = boto3.resource('dynamodb')
    tabela = dynamodb.Table('Filmes')
    tabela.delete()

apagar_tabela_filmes()