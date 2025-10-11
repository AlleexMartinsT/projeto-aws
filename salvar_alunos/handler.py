import json  

# Função principal da AWS Lambda
def lambda_handler(event, context):
    # Percorre cada registro recebido no evento (event)
    for record in event['Records']:
        # Extrai e converte a mensagem JSON enviada pelo SNS para um dicionário Python
        aluno = json.loads(record['Sns']['Message'])
        
        # Exibe no log os dados do aluno (nome e matrícula)
        print(f"Salvando aluno: {aluno['nome']} - Matrícula: {aluno['matricula']}")

    # Retorna uma resposta padrão de sucesso
    return {'statusCode': 200, 'body': json.dumps('Alunos salvos com sucesso')}
