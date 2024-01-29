import json

from models import Author, Quote
import logging
import connect

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def load_authors(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            authors_data = json.load(file)
            for author_data in authors_data:
                if not Author.objects(fullname=author_data['fullname']):
                    Author(**author_data).save()
                    logging.info(f"Author saved: {author_data['fullname']}")
    except Exception as e:
        logging.error(f"Error loading authors: {e}")


def load_quotes(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            quotes_data = json.load(file)
            for quote_data in quotes_data:
                author_name = quote_data.pop('author', None)  # Видаляємо 'author' із quote_data і зберігаємо його в author_name
                author = Author.objects(fullname=author_name).first()
                if author:
                    Quote(author=author, **quote_data).save()  # Тепер 'author' передається лише один раз
                    logging.info(f"Quote saved: {quote_data['quote']}")
    except Exception as e:
        logging.error(f"Error loading quotes: {e}")



load_authors(r'json\authors.json')
load_quotes(r'json\quotes.json')
