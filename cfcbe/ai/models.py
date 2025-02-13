
# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TriageRule(models.Model):
    keyword = models.CharField(max_length=255, null=True, blank=True)
    sentiment_threshold = models.FloatField(null=True, blank=True)  # e.g., range -1 to 1
    priority_level = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ])
    routing_department = models.CharField(max_length=255)  # e.g., "Abuse", "Neglect", "Education"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.keyword} - {self.priority_level}"

class TriageAnalysis(models.Model):
    complaint = models.ForeignKey('Complaint', on_delete=models.CASCADE, related_name='triage_analyses')
    sentiment_score = models.FloatField()
    detected_keywords = models.JSONField()  # Store list of detected keywords
    priority_level = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ])
    routing_department = models.CharField(max_length=255)
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for Complaint {self.complaint.id}"

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class CaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='case_histories')
    complaint = models.ForeignKey('Complaint', on_delete=models.CASCADE, related_name='case_histories')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    resolution_summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Case History for User {self.user.id}"

class ComplaintRouting(models.Model):
    complaint = models.OneToOneField('Complaint', on_delete=models.CASCADE, related_name='routing_info')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='routings')
    rationale = models.TextField()  # Why it was routed here (keywords, sentiment, etc.)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Routing for Complaint {self.complaint.id}"

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sentiment_complaints')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Complaint {self.id} by User {self.user.id}"


class SentimentAnalysis(models.Model):
    complaint = models.OneToOneField(Complaint, on_delete=models.CASCADE, related_name='sentiment_analysis')
    sentiment_score = models.FloatField()
    analyzed_at = models.DateTimeField(auto_now_add=True)
    
class CaseRouting(models.Model):
    complaint = models.OneToOneField(Complaint, on_delete=models.CASCADE, related_name='case_routing')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='case_routings')
    rationale = models.TextField()  # Why it was routed here (keywords, sentiment, etc.)
    created_at = models.DateTimeField(auto_now_add=True)
