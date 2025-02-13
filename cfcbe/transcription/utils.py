import base64
import json
import logging
import requests

# Function to forward data to the main system
def forward_raw_data_to_main_system(raw_data):
    """
    Sends the RawData and its corresponding audio file to the main system via a POST request.

    :param raw_data: RawData instance to be forwarded
    """
    # API configuration
    api_url = "https://demo-openchs.bitz-itc.com/helpline/api/msg/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sci9de994iddqlmj8fv7r1js74",
    }

    # Sanitize text fields
    def sanitize_text(text):
        if text:
            return text.encode("utf-8", errors="replace").decode("utf-8")
        return text

    # Construct payload
    payload = {
        "unique_id": raw_data.unique_id.unique_id,
        "date": raw_data.date.isoformat(),
        "talk_time": raw_data.talk_time.isoformat(),
        "case_id": raw_data.case_id,
        "narrative": sanitize_text(raw_data.narrative),
        "plan": sanitize_text(raw_data.plan),
        "main_category": sanitize_text(raw_data.main_category),
        "sub_category": sanitize_text(raw_data.sub_category),
        "gbv": raw_data.gbv,
        "audio_base64": base64.b64encode(raw_data.unique_id.audio_data).decode("utf-8"),
    }

    logging.info(f"Payload JSON: {payload}")

    try:
        # Send POST request
        response = requests.post(api_url, json=payload, headers=headers)
        logging.info(f"API Response: {response.status_code}, {response.text}")
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred: {e} - Response: {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to forward raw data for case ID {raw_data.case_id}. Error: {e}")
