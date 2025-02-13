from rest_framework import serializers
from .models import AudioFile, AudioFileChunk, CaseRecord, ModelVersion, ModelTranscription

class AudioFileChunkSerializer(serializers.ModelSerializer):
    """Serializer for AudioFileChunk including gender and locale fields."""
    
    gender = serializers.ChoiceField(choices=AudioFileChunk.GENDER_CHOICES, default="not_sure")
    locale = serializers.ChoiceField(choices=AudioFileChunk.LOCALE_CHOICES, default="both")

    class Meta:
        model = AudioFileChunk
        fields = [
            "id",
            "parent_audio",
            "chunk_file",
            "order",
            "duration",
            "true_transcription",
            "is_rejected",
            "gender",  # ✅ New field
            "locale",  # ✅ New field
            "created_at",
        ]

class AudioFileChunkUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating AudioFileChunk attributes, including gender and locale."""
    
    class Meta:
        model = AudioFileChunk
        fields = ["true_transcription", "is_rejected", "gender", "locale"]  # ✅ Added new fields

class AudioFileSerializer(serializers.ModelSerializer):
    """Serializer for AudioFile, including chunk statistics."""

    total_chunks = serializers.IntegerField(source="chunks.count", read_only=True)
    transcribed_chunks = serializers.IntegerField(source="chunks.with_transcriptions.count", read_only=True)
    untranscribed_chunks = serializers.IntegerField(source="chunks.without_transcriptions.count", read_only=True)

    class Meta:
        model = AudioFile
        fields = [
            "id",
            "unique_id",
            "audio_file",

            "duration",
            "file_size",

            "duration",
            "file_size",
            "total_chunks",  # ✅ Total chunks
            "transcribed_chunks",  # ✅ Transcribed chunks
            "untranscribed_chunks",  # ✅ Untranscribed chunks
        ]

class ModelVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelVersion
        fields = ['version']

class ModelTranscriptionSerializer(serializers.ModelSerializer):
    audio_id = AudioFileSerializer()  # Nested serializer to include AudioFile data
    model_version_id = ModelVersionSerializer()  # Nested serializer to include ModelVersion data

    class Meta:
        model = ModelTranscription
        fields = ['audio_id', 'model_version_id', 'predicted_text', 'wer', 'created_at', 'updated_at']

class CaseRecordSerializer(serializers.ModelSerializer):
    unique_id = AudioFileSerializer()  # Nested serializer to include AudioFile data
    audio_file = AudioFileSerializer(read_only=True)
    transcriptions = ModelTranscriptionSerializer(read_only=True, many=True)

    class Meta:
        model = CaseRecord
        fields = ['unique_id', 'date', 'talk_time', 'case_id', 'audio_file', 'narrative', 'transcriptions','plan', 'main_category', 'sub_category', 'gbv']


class CaseRecordSerializer(serializers.ModelSerializer):
    """Serializer for Case Records, including their associated Audio Files and Chunks."""
    
    audio_file = AudioFileSerializer(read_only=True, source="unique_id")  # ✅ Get related audio file

    class Meta:
        model = CaseRecord
        fields = [
            "id",
            "case_id",
            "date",
            "talk_time",
            "narrative",
            "plan",
            "main_category",
            "sub_category",
            "gbv",
            "audio_file",  # ✅ Includes related Audio File and Chunks
        ]
