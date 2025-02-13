import json
import logging
import base64
import requests
from django.conf import settings
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Complaint, Notification

API_URL = "https://demo-openchs.bitz-itc.com/helpline/api/msg/"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {settings.BEARER_TOKEN}",
}

@receiver(post_save, sender=Complaint)
def create_notification(sender, instance, created, **kwargs):
    if created:
        print(f"Signal triggered for complaint: {instance.complaint_id}, created: {created}")
        transaction.on_commit(lambda: generate_notification(instance))

def generate_notification(instance):
    instance.refresh_from_db()

    victim = instance.victim
    perpetrator = instance.perpetrator

    # Construct complaint JSON data
    complaint_data = {
        "complaint_id": str(instance.complaint_id),
        "channel": "chat",
        "timestamp": instance.timestamp.isoformat(),
        "session_id": str(instance.session_id),
        "message_id": str(instance.complaint_id),
        "from": str(instance.session_id),
        "reporter_nickname": instance.reporter_nickname,
        "case_category": instance.case_category,
        "victim": {
            "name": victim.name if victim else "",
            "age": victim.age if victim else "",
            "gender": victim.gender if victim else "",
        },
        "perpetrator": {
            "name": perpetrator.name if perpetrator else "",
            "age": perpetrator.age if perpetrator else "",
            "gender": perpetrator.gender if perpetrator else "",
        },
    }

    # Convert JSON to base64
    complaint_json = json.dumps(complaint_data)
    encoded_data = base64.b64encode(complaint_json.encode()).decode("utf-8")

    # Construct the message payload
    complaint_payload = {
        "channel": "safepal",
        "timestamp": instance.timestamp.isoformat(),
        "session_id": str(instance.session_id),
        "message_id": str(instance.complaint_id),
        "from": str(instance.session_id),
        "message": encoded_data,
        "mime": "application/json",
    }

    print(f"Sending payload: {json.dumps(complaint_payload, indent=2)}")

    # Create Notification
    message = (
        f"A new complaint has been filed by {instance.reporter_nickname or 'an anonymous reporter'} "
        f"in the category {instance.case_category}."
    )
    Notification.objects.create(complaint=instance, message=message)

    # Send to API
    try:
        response = requests.post(API_URL, headers=HEADERS, json=complaint_payload)
        print(f"API Response: {response.status_code}, {response.text}")

        if response.status_code == 201:
            response_data = response.json()
            message_id = response_data.get("messages", [[]])[0][0]  # Extract message ID
            if message_id:
                instance.message_id_ref = message_id
                instance.save(update_fields=["message_id_ref"])
                logging.info(f"message_id_ref saved: {message_id}")
            else:
                logging.error("message_id not found in API response.")
        else:
            logging.error(f"API call failed: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send complaint to API: {e}")
