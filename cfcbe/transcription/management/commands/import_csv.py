import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from transcription.models import AudioFile, CaseRecord
from django.utils.timezone import make_aware

class Command(BaseCommand):
    help = 'Import data from a CSV file into the CaseRecord model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to import.')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')  # Use correct delimiter
                for row in reader:
                    try:
                        # Retrieve the AudioFile instance by unique_id
                        audio_file = AudioFile.objects.get(unique_id=row['UNIQUEID'])

                        # Check if CaseRecord exists for this audio file and update it, else create a new record
                        raw_data, created = CaseRecord.objects.update_or_create(
                            unique_id=audio_file,
                            defaults={
                                'date': make_aware(datetime.strptime(row['DATE'], '%d %b %Y %H:%M')),  # Add time zone awareness
                                'talk_time': datetime.strptime(row['TALKTIME'], '%H:%M').time(),
                                'case_id': int(row['CASEID']),
                                'narrative': row['NARRATIVE'],
                                'plan': row['PLAN'],
                                'main_category': row['MAIN CATEGORY'],
                                'sub_category': row['SUB CATEGORY'],
                                'gbv': row['GBV'].strip().lower() == 'yes',  # Convert to boolean
                            }
                        )

                        if created:
                            self.stdout.write(self.style.SUCCESS(f"Created CaseRecord for unique_id {row['UNIQUEID']}"))
                        else:
                            self.stdout.write(self.style.SUCCESS(f"Updated CaseRecord for unique_id {row['UNIQUEID']}"))

                    except AudioFile.DoesNotExist:
                        self.stderr.write(self.style.ERROR(f"AudioFile with unique_id {row['UNIQUEID']} does not exist. Skipping."))
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f"Error saving CaseRecord for unique_id {row['UNIQUEID']}: {e}"))

            self.stdout.write(self.style.SUCCESS(f"Data imported successfully from {csv_file_path}"))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {csv_file_path}"))
        except KeyError as e:
            self.stderr.write(self.style.ERROR(f"Missing column in CSV file: {e}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))