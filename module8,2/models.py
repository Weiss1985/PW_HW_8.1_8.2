from mongoengine import Document, StringField, BooleanField
import connect

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    email_sent = BooleanField(default=False)

