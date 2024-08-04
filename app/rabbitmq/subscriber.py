import pika, sys

from .config import get_rabbitmq_connection


def consume_messages():    
    try:
        connection = get_rabbitmq_connection()
        channel = connection.channel()

        channel.exchange_declare(exchange='via', exchange_type='topic', durable=True)
        channel.queue_declare(queue='cola', durable=True)
        channel.queue_bind(exchange='via', queue='cola', routing_key='test')

        print(' [***] Waiting for logs from Report.')
        sys.stdout.flush()

        def callback(ch, method, properties, body):
            ch.basic_ack(delivery_tag=method.delivery_tag)
            print(f" [xXX] {body.decode()}")
            sys.stdout.flush()

        channel.basic_consume(queue='cola', on_message_callback=callback)
        channel.start_consuming()
        
    except pika.exceptions.AMQPConnectionError as e:
        print("RabbitMQ connection error")
        sys.stdout.flush()
    else:
        print("Consuming")
        sys.stdout.flush()