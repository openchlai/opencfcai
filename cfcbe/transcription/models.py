import re
from django.db import models
from django.contrib.auth.models import User


class AudioFile(models.Model):
    unique_id = models.CharField(max_length=50, unique=True)
    audio_file = models.FileField(upload_to="")
    file_size = models.PositiveIntegerField(null=True)
    duration = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.unique_id


class AudioFileChunkManager(models.Manager):
    """Custom manager for AudioFileChunk to provide useful queries."""

    def with_transcriptions(self):
        """Get all chunks that have a true transcription."""
        return self.filter(true_transcription__isnull=False).exclude(true_transcription="").filter(is_rejected=False)

    def without_transcriptions(self):
        """Get all chunks that do not have a true transcription."""
        return self.filter(models.Q(true_transcription__isnull=True) | models.Q(true_transcription="")).filter(is_rejected=False)


    def rejected_chunks(self):
        """Get all chunks that have been rejected."""
        return self.filter(is_rejected=True)

    def total_chunks(self):
        """Get the total number of chunks."""
        return self.count()

    def total_transcribed_chunks(self):
        """Get the total number of transcribed chunks."""
        return self.with_transcriptions().count()

    def total_untranscribed_chunks(self):
        """Get the total number of untranscribed chunks."""
        return self.without_transcriptions().count()

    def total_rejected_chunks(self):
        """Get the total number of rejected chunks."""
        return self.rejected_chunks().count()

from django.db import models

class AudioFileChunk(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("not_sure", "Not Sure"),
    ]

    LOCALE_CHOICES = [
        ("en", "English"),
        ("sw", "Swahili"),
        ("both", "Both"),
    ]

    parent_audio = models.ForeignKey("AudioFile", on_delete=models.CASCADE, related_name="chunks")
    chunk_file = models.FileField(upload_to="audio_chunks/")
    order = models.PositiveIntegerField()  # Order of the chunk in the original file
    duration = models.FloatField(null=True)
    true_transcription = models.TextField(blank=True, null=True)  # ✅ Holds ground-truth transcriptions
    is_rejected = models.BooleanField(default=False)  # ✅ Tracks whether chunk is rejected
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="not_sure")  # ✅ Gender field
    locale = models.CharField(max_length=5, choices=LOCALE_CHOICES, default="both")  # ✅ Locale field
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AudioFileChunkManager()  # ✅ Attach the custom manager

    class Meta:
        unique_together = ('parent_audio', 'order')  # Prevent duplicate chunk orders


    def save(self, *args, **kwargs):
        """
        ✅ Extracts order number from chunk filename before saving.
        ✅ Ensures `chunk_file.name` exists before validation.
        ✅ Prevents accidental overwrites.
        """
        if not self.chunk_file or not self.chunk_file.name:
            raise ValueError("Chunk file must be set before saving.")

        match = re.search(r"_chunk_(\d{4})", self.chunk_file.name)  # Extract chunk number
        if match:
            self.order = int(match.group(1))  # Convert extracted chunk number to integer
        else:
            raise ValueError(f"Invalid chunk filename format: {self.chunk_file.name}. Expected format: unique_id_chunk_XXXX.wav")

        super().save(*args, **kwargs)


    def __str__(self):
        return f"Chunk {self.order} of {self.parent_audio.unique_id}"


class CaseRecord(models.Model):
    unique_id = models.OneToOneField(AudioFile, on_delete=models.CASCADE)
    date = models.DateTimeField()
    talk_time = models.TimeField()
    case_id = models.CharField(max_length=20)
    narrative = models.TextField()
    plan = models.TextField()
    main_category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    gbv = models.BooleanField()

    def __str__(self):
        return f"Case {self.case_id} - {self.main_category}"


class ModelVersion(models.Model):
    version = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.version


class ModelTranscription(models.Model):
    # Supports either full audio file or a chunk
    audio_id = models.ForeignKey(AudioFile, null=True, blank=True, on_delete=models.DO_NOTHING)
    audio_chunk_id = models.ForeignKey(AudioFileChunk, null=True, blank=True, on_delete=models.DO_NOTHING)

    model_version_id = models.ForeignKey(ModelVersion, on_delete=models.DO_NOTHING)
    predicted_text = models.TextField()
    wer = models.FloatField(null=True, blank=True)

    status = models.CharField(
        max_length=50,
        choices=[('in-progress', 'In Progress'), ('completed', 'Completed')],
        default='in-progress'
    )

    started_at = models.DateTimeField(null=True, blank=True)  # Timestamp when transcription starts
    finished_at = models.DateTimeField(null=True, blank=True)  # Timestamp when transcription finishes

    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)  # Who is transcribing
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.audio_chunk_id:
            return f"Transcription for Chunk {self.audio_chunk_id.order} of {self.audio_chunk_id.parent_audio.unique_id}"
        else:
            return f"Transcription for {self.audio_id.unique_id} - {self.model_version_id.version}"


