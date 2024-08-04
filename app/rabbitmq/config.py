import pika


def get_rabbitmq_connection():
    connection_params = pika.ConnectionParameters(
        host='localhost',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest')
    )
    return pika.BlockingConnection(connection_params)