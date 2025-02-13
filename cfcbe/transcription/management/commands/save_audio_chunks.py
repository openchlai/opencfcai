import os
import re
<<<<<<< HEAD
<<<<<<< HEAD
import librosa
=======
>>>>>>> d44c978 (added chunks model and added endpoints)
=======
import librosa
>>>>>>> 95908c0 (saving also file_size and duration)
from django.core.files import File
from django.core.management.base import BaseCommand
from transcription.models import AudioFile, AudioFileChunk

class Command(BaseCommand):
<<<<<<< HEAD
<<<<<<< HEAD
    help = "Save audio file chunks to the FileField with metadata (duration)."
=======
    help = "Save audio file chunks to the FileField"
>>>>>>> d44c978 (added chunks model and added endpoints)
=======
    help = "Save audio file chunks to the FileField with metadata (duration)."
>>>>>>> 95908c0 (saving also file_size and duration)

    def add_arguments(self, parser):
        parser.add_argument("directory", type=str, help="The directory containing chunked audio files.")

    def handle(self, *args, **kwargs):
        directory = kwargs["directory"]

        if not os.path.isdir(directory):
<<<<<<< HEAD
<<<<<<< HEAD
            self.stderr.write(self.style.ERROR(f"❌ Directory not found: {directory}"))
=======
            self.stderr.write(self.style.ERROR(f"Directory not found: {directory}"))
>>>>>>> d44c978 (added chunks model and added endpoints)
=======
            self.stderr.write(self.style.ERROR(f"❌ Directory not found: {directory}"))
>>>>>>> 95908c0 (saving also file_size and duration)
            return

        for filename in sorted(os.listdir(directory)):  # Sort to maintain order
            if filename.endswith(".wav"):
                file_path = os.path.join(directory, filename)

                # ✅ Debug: Print filename before matching
                print(f"🔍 Checking filename: {filename}")

                # ✅ Try multiple regex formats
                match = re.match(r"^(?P<unique_id>[\d.]+)_chunk_(?P<order>\d+)\.wav$", filename)
                
                if match:
                    unique_id = match.group("unique_id")
                    chunk_order = int(match.group("order"))  # Convert chunk number to integer
                    print(f"✅ Matched! Unique ID: {unique_id}, Chunk Order: {chunk_order}")
                else:
                    print(f"❌ No match for filename: {filename}")
                    continue  # Skip this file

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 95908c0 (saving also file_size and duration)
                try:
                    # ✅ Find the parent `AudioFile`
                    parent_audio = AudioFile.objects.filter(unique_id=unique_id).first()
                    if not parent_audio:
                        self.stderr.write(self.style.ERROR(f"No matching AudioFile for {unique_id}, skipping {filename}"))
                        continue
<<<<<<< HEAD

                    # ✅ Extract metadata
                    duration = self.get_audio_duration(file_path)

                    # ✅ Check if chunk already exists
                    chunk_instance, created = AudioFileChunk.objects.get_or_create(
                        parent_audio=parent_audio,
                        order=chunk_order,
                        defaults={"chunk_file": file_path, "duration": duration}  # ✅ Ensure metadata is saved
                    )

                    # ✅ Open the file properly before saving
                    with open(file_path, "rb") as f:
                        django_file = File(f)
                        chunk_instance.chunk_file.save(filename, django_file, save=True)

                    # ✅ Update duration if missing
                    if not created and chunk_instance.duration is None:
                        chunk_instance.duration = duration
                        chunk_instance.save()

                    if created:
                        self.stdout.write(self.style.SUCCESS(f"🔹 New chunk saved: {filename} (Duration: {duration:.2f}s)"))
                    else:
                        self.stdout.write(self.style.WARNING(f"⚠️ Using existing chunk: {filename} (Updated duration if missing)"))

                except Exception as e:
                    import traceback
                    error_details = traceback.format_exc()
                    self.stderr.write(self.style.ERROR(f"❌ Error saving file {filename}: {e}\n{error_details}"))

        self.stdout.write(self.style.SUCCESS("✅ All audio chunks processed successfully."))

    def get_audio_duration(self, file_path):
        """Extracts the duration of an audio file chunk."""
        try:
            y, sr = librosa.load(file_path, sr=None)  # Load audio with original sampling rate
            return librosa.get_duration(y=y, sr=sr)  # Calculate duration in seconds
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"⚠️ Error extracting duration for {file_path}: {e}"))
            return None  # Return None if duration extraction fails
=======
            try:
                # ✅ Find the parent `AudioFile`
                parent_audio = AudioFile.objects.filter(unique_id=unique_id).first()
                if not parent_audio:
                    self.stderr.write(self.style.ERROR(f"No matching AudioFile for {unique_id}, skipping {filename}"))
                    continue
=======
>>>>>>> 95908c0 (saving also file_size and duration)

                    # ✅ Extract metadata
                    duration = self.get_audio_duration(file_path)

                    # ✅ Check if chunk already exists
                    chunk_instance, created = AudioFileChunk.objects.get_or_create(
                        parent_audio=parent_audio,
                        order=chunk_order,
                        defaults={"chunk_file": file_path, "duration": duration}  # ✅ Ensure metadata is saved
                    )

                    # ✅ Open the file properly before saving
                    with open(file_path, "rb") as f:
                        django_file = File(f)
                        chunk_instance.chunk_file.save(filename, django_file, save=True)

                    # ✅ Update duration if missing
                    if not created and chunk_instance.duration is None:
                        chunk_instance.duration = duration
                        chunk_instance.save()

                    if created:
                        self.stdout.write(self.style.SUCCESS(f"🔹 New chunk saved: {filename} (Duration: {duration:.2f}s)"))
                    else:
                        self.stdout.write(self.style.WARNING(f"⚠️ Using existing chunk: {filename} (Updated duration if missing)"))

                except Exception as e:
                    import traceback
                    error_details = traceback.format_exc()
                    self.stderr.write(self.style.ERROR(f"❌ Error saving file {filename}: {e}\n{error_details}"))

        self.stdout.write(self.style.SUCCESS("✅ All audio chunks processed successfully."))
<<<<<<< HEAD
>>>>>>> d44c978 (added chunks model and added endpoints)
=======

    def get_audio_duration(self, file_path):
        """Extracts the duration of an audio file chunk."""
        try:
            y, sr = librosa.load(file_path, sr=None)  # Load audio with original sampling rate
            return librosa.get_duration(y=y, sr=sr)  # Calculate duration in seconds
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"⚠️ Error extracting duration for {file_path}: {e}"))
            return None  # Return None if duration extraction fails
>>>>>>> 95908c0 (saving also file_size and duration)
