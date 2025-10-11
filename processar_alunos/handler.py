import os      # Importa o módulo 'os' para acessar variáveis de ambiente da função Lambda
import json    # Importa o módulo 'json' para trabalhar com dados em formato JSON
import boto3   # Importa o SDK da AWS para Python (boto3), usado para interagir com serviços da AWS

# Cria um cliente para o serviço SNS (Simple Notification Service)
sns = boto3.client('sns')

# Função principal executada pela AWS Lambda
def lambda_handler(event, context):
    # Percorre cada registro recebido no evento — neste caso, vindo do SQS (fila)
    for record in event['Records']:
        # Converte o corpo da mensagem (string JSON) em um dicionário Python
        aluno = json.loads(record['body'])
        
        # Adiciona ou atualiza o campo 'status' do aluno para indicar que foi processado
        aluno['status'] = 'processado'

        # Publica os dados do aluno processado em um tópico SNS
        sns.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],  # Obtém o ARN do tópico SNS a partir das variáveis de ambiente
            Message=json.dumps(aluno)              # Converte novamente o dicionário para JSON antes de enviar
        )
    
    # Retorna uma resposta indicando sucesso
    return {'statusCode': 200, 'body': json.dumps('Alunos processados e enviados ao SNS')}
