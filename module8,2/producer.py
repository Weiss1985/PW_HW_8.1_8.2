import pika
import json
from models import Contact
from faker import Faker
import connect

# Налаштування RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

faker = Faker()

def create_fake_contacts(n):
    for _ in range(n):
        contact = Contact(
            fullname=faker.name(),
            email=faker.email()
        )
        contact.save()

        channel.basic_publish(
            exchange='',
            routing_key='email_queue',
            body=json.dumps({'contact_id': str(contact.id)})
        )

create_fake_contacts(10)  # Генерування 10 фейкових контактів

connection.close()
