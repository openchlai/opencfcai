import imaplib
import email
from email.header import decode_header
from datetime import datetime
from .models import Email

# Function to clean and decode email content
def clean_email_content(content):
    if isinstance(content, bytes):
        return content.decode('utf-8', errors='ignore')
    return content

def fetch_emails(username, password, mail_server="imap.gmail.com"):
    try:
        # Connect to the mail server
        mail = imaplib.IMAP4_SSL(mail_server)
        mail.login(username, password)
        mail.select("inbox")

        # Search for all emails
        status, messages = mail.search(None, "ALL")

        # Convert the byte messages to a list of email IDs
        email_ids = messages[0].split()

        for email_id in email_ids:
            # Fetch the email
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Parse the email content
                    msg = email.message_from_bytes(response_part[1])

                    # Decode email sender, recipient, and subject
                    sender = clean_email_content(msg.get("From"))
                    recipient = clean_email_content(msg.get("To"))
                    subject, encoding = decode_header(msg.get("Subject"))[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")

                    # Get the email date
                    received_date = msg.get("Date")
                    received_date = datetime.strptime(received_date, "%a, %d %b %Y %H:%M:%S %z")

                    # Get the email body
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                body = part.get_payload(decode=True)
                                body = clean_email_content(body)
                                break
                    else:
                        body = msg.get_payload(decode=True)
                        body = clean_email_content(body)

                    # Save the email to the database
                    Email.objects.create(
                        sender=sender,
                        recipient=recipient,
                        subject=subject,
                        body=body,
                        received_date=received_date
                    )
        
        # Logout from the mail server
        mail.logout()

    except Exception as e:
        print(f"Error: {e}")
