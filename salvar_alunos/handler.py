import json

def lambda_handler(event, context):
    for record in event['Records']:
        aluno = json.loads(record['Sns']['Message'])
        print(f"Salvando aluno: {aluno['nome']} - Matrícula: {aluno['matricula']}")

    return {'statusCode': 200, 'body': json.dumps('Alunos salvos com sucesso')}