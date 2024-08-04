import pika

from .config import get_rabbitmq_connection


def publish_message(message):    
    try:
        connection = get_rabbitmq_connection()
        channel = connection.channel()
        channel.confirm_delivery()

        channel.queue_declare(queue='cola', durable=True)
        channel.exchange_declare(exchange='via', exchange_type='topic', durable=True)

        channel.basic_publish(exchange='via', routing_key='test', body=message, properties=pika.BasicProperties(delivery_mode=2))

        connection.close()
        
    except pika.exceptions.AMQPConnectionError as e:
        return("RabbitMQ connection error")
    except pika.exceptions.UnroutableError:
        return("Messaje could not be confirmed.")
    else:
        return(f"Sent {message}")