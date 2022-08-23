#Insert de dados no DynamoDB

import boto3

def inserir_filme(titulo, ano, diretor, generos):
    dynamodb = boto3.resource('dynamodb')
    tabela = dynamodb.Table('Filmes')
    tabela.put_item(
        Item={
            'titulo': titulo,
            'ano': ano,
            'diretor': diretor,
            'generos': generos
        }
    )

inserir_filme('Apocalypse Now', 1979, 'Francis Ford Coppola', ['Drama', 'Guerra'])
inserir_filme('Parasita', 2019, 'Bong Joon Ho', ['Comedia', 'Drama','Suspense'])
inserir_filme('Clube da Luta', 1999, 'David Fincher', 'Drama')
inserir_filme('O Poderoso Chefao', 1972, 'Francis Ford Coppola', ['Crime', 'Drama'])
inserir_filme('Bacurau', 2019, 'Kleber Mendonça Filho', ['Western', 'Suspense', 'Terror'])