# fetch_emails.py
from django.core.management.base import BaseCommand
from  utils import fetch_emails  # Adjust import path

class Command(BaseCommand):
    help = "Fetch emails from the mailbox and store them in the database."

    def handle(self, *args, **kwargs):
        username = input("Enter your email address: ")
        password = input("Enter your password: ")
        fetch_emails(username, password)
        self.stdout.write(self.style.SUCCESS("Emails fetched and stored successfully."))
