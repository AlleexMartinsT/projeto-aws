import os
import json
import boto3

sqs = boto3.client('sqs') 

def lambda_handler(event, context):
    body = json.loads(event['body'])
    nome = body.get('nome')
    matricula = body.get('matricula')

    message = {
        'nome': nome,
        'matricula': matricula
    }

    response = sqs.send_message(
        QueueUrl=os.environ['SQS_QUEUE_URL'],
        MessageBody=json.dumps(message)
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Aluno cadastrado com sucesso!', 'sqsResponse': response})
    }