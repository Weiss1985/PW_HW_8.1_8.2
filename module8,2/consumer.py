import pika
import json
from models import Contact
import connect


def send_email_stub(contact):
    print(f"Sending email to {contact.fullname} at {contact.email}")
    contact.email_sent = True
    contact.save()


def callback(ch, method, properties, body):
    data = json.loads(body)
    contact_id = data['contact_id']
    contact = Contact.objects(id=contact_id).first()
    if contact:
        send_email_stub(contact)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')
channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
