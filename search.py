
from models import Author, Quote
import connect


def search_quotes_by_author(author_name):
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        return [quote.quote for quote in quotes]
    return []


def search_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [quote.quote for quote in quotes]


def search_quotes_by_tags(tags):
    quotes = Quote.objects(tags__in=tags)
    return [quote.quote for quote in quotes]


while True:
    command_input = input("Enter your command: ").strip()
    if command_input.lower() == "exit":
        break
    try:
        command, value = command_input.split(":")
        if command == "name":
            quotes = search_quotes_by_author(value.strip())
        elif command == "tag":
            quotes = search_quotes_by_tag(value.strip())
        elif command == "tags":
            tags = value.split(",")
            quotes = search_quotes_by_tags(tags)
        else:
            print("Unknown command.")
            continue

        print("\n".join(quotes))
    except ValueError:
        print("Invalid command format. Please use 'command: value'.")
