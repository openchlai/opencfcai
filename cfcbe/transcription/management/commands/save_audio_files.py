import os
import librosa
from django.core.files import File
from django.core.management.base import BaseCommand
from transcription.models import AudioFile

class Command(BaseCommand):
    help = "Save audio files to the FileField with metadata (duration & file size)."

    def add_arguments(self, parser):
        parser.add_argument("directory", type=str, help="The directory containing audio files to save.")

    def handle(self, *args, **kwargs):
        directory = kwargs["directory"]

        if not os.path.isdir(directory):
            self.stderr.write(self.style.ERROR(f"❌ Directory not found: {directory}"))
            return

        for filename in os.listdir(directory):
            if filename.endswith(".wav"):
                file_path = os.path.join(directory, filename)
                unique_id = os.path.splitext(filename)[0]  # Extract filename without extension

                try:
                    # ✅ Extract metadata
                    duration = self.get_audio_duration(file_path)
                    file_size = os.path.getsize(file_path)  # File size in bytes

                    # ✅ Check if the file already exists
                    audio_file_instance, created = AudioFile.objects.get_or_create(
                        unique_id=unique_id,
                        defaults={"duration": duration, "file_size": file_size}  # ✅ Set metadata
                    )

                    # ✅ If file exists but metadata is missing, update it
                    if not created:
                        if audio_file_instance.duration is None:
                            audio_file_instance.duration = duration
                        if audio_file_instance.file_size is None:
                            audio_file_instance.file_size = file_size

                    # ✅ Save the file to the FileField (filesystem)
                    with open(file_path, "rb") as f:
                        django_file = File(f)
                        audio_file_instance.audio_file.save(filename, django_file, save=True)

                    audio_file_instance.save()  # ✅ Ensure metadata is saved

                    if created:
                        self.stdout.write(self.style.SUCCESS(f"🎵 New audio file saved: {filename} (Duration: {duration:.2f}s, Size: {file_size} bytes)"))
                    else:
                        self.stdout.write(self.style.WARNING(f"✅ Using existing audio file: {filename} (Updated metadata if needed)"))

                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"❌ Error saving file {filename}: {e}"))

        self.stdout.write(self.style.SUCCESS("✅ All audio files processed successfully."))

    def get_audio_duration(self, file_path):
        """Extracts the duration of an audio file."""
        try:
            y, sr = librosa.load(file_path, sr=None)  # Load audio with original sampling rate
            return librosa.get_duration(y=y, sr=sr)  # Calculate duration in seconds
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"⚠️ Error extracting duration for {file_path}: {e}"))
            return None  # Return None if duration extraction fails
