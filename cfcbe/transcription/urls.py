from django.urls import path
from .views import case_records_with_chunk_stats, chunk_statistics, get_audio_file_chunks, get_filtered_audio_file_chunks, rejected_chunks, transcribe_audio, AudioFileListCreateView, TranscriptionListCreateView, TranscriptionRetrieveUpdateDestroyView, CaseRecordListCreateView, CaseRecordRetrieveUpdateDestroyView, transcribed_chunks, untranscribed_chunks, update_chunk_rejection_status, update_chunk_transcription

urlpatterns = [
    path("transcribe/", transcribe_audio, name="transcribe_audio"),
    
    
    # AudioFile API
    path('audio-files/', AudioFileListCreateView.as_view(), name='audio-file-list-create'),

    # Transcription API
    path('transcriptions/', TranscriptionListCreateView.as_view(), name='transcription-list-create'),
    path('transcriptions/<int:pk>/', TranscriptionRetrieveUpdateDestroyView.as_view(), name='transcription-detail'),

    # CaseRecord API
    path('case-records/', case_records_with_chunk_stats, name='case-record-list-create'),
    path('case-records/<int:pk>/', CaseRecordRetrieveUpdateDestroyView.as_view(), name='case-record-detail'),
    
    path("api/chunk-statistics/", chunk_statistics, name="chunk_statistics"),
    path("api/transcribed-chunks/", transcribed_chunks, name="transcribed_chunks"),
    path("api/untranscribed-chunks/", untranscribed_chunks, name="untranscribed_chunks"),
    path("api/rejected-chunks/", rejected_chunks, name="rejected_chunks"),
    path("api/chunks/<int:chunk_id>/update-transcription/", update_chunk_transcription, name="update_chunk_transcription"),
    path("api/chunks/<int:chunk_id>/update-rejection/", update_chunk_rejection_status, name="update_chunk_rejection_status"),
    path("api/audio-files/<int:audio_id>/chunks/", get_audio_file_chunks, name="get_audio_file_chunks"),
    path("api/audio-files/<int:audio_id>/chunks/<str:filter_type>/", get_filtered_audio_file_chunks, name="get_filtered_audio_file_chunks"),

]
