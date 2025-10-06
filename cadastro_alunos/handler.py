import os          # Para acessar variáveis de ambiente (como a URL da fila SQS)
import json        # Para converter dados entre Python e JSON
import boto3       # SDK da AWS para Python, usado para acessar serviços como SQS

# Cria um cliente SQS para enviar mensagens à fila
sqs = boto3.client('sqs') 

def lambda_handler(event, context):
    # Converte o corpo (body) da requisição JSON em um dicionário Python
    body = json.loads(event['body'])

    # Extrai os dados enviados pelo cliente (via POST)
    nome = body.get('nome')
    matricula = body.get('matricula')

    # Cria a mensagem que será enviada para a fila SQS
    message = {
        'nome': nome,
        'matricula': matricula
    }

    # Envia a mensagem para a fila SQS configurada nas variáveis de ambiente da Lambda
    response = sqs.send_message(
        QueueUrl=os.environ['SQS_QUEUE_URL'],  # URL da fila SQS (definida no template SAM)
        MessageBody=json.dumps(message)        # Converte a mensagem em JSON para envio
    )

    # Retorna uma resposta HTTP com status 200 e uma mensagem de sucesso
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Aluno cadastrado com sucesso!',  # Mensagem de confirmação
            'sqsResponse': response                      # Retorna dados da resposta da SQS (opcional)
        })
    }
