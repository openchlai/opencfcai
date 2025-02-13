import os
from django.http import HttpResponseBadRequest, JsonResponse
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import IntegrityError, transaction
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import TriageRule, TriageAnalysis, Department, CaseHistory, ComplaintRouting, Complaint
from .serializers import (
    TriageRuleSerializer,
    TriageAnalysisSerializer,
    DepartmentSerializer,
    CaseHistorySerializer,
    ComplaintRoutingSerializer,
    ComplaintSerializer
)

# TriageRule Views
class TriageRuleListCreateView(generics.ListCreateAPIView):
    queryset = TriageRule.objects.all()
    serializer_class = TriageRuleSerializer


class TriageRuleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TriageRule.objects.all()
    serializer_class = TriageRuleSerializer


# TriageAnalysis Views
class TriageAnalysisListCreateView(generics.ListCreateAPIView):
    queryset = TriageAnalysis.objects.all()
    serializer_class = TriageAnalysisSerializer


class TriageAnalysisRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TriageAnalysis.objects.all()
    serializer_class = TriageAnalysisSerializer


# Department Views
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# CaseHistory Views
class CaseHistoryListCreateView(generics.ListCreateAPIView):
    queryset = CaseHistory.objects.all()
    serializer_class = CaseHistorySerializer


class CaseHistoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CaseHistory.objects.all()
    serializer_class = CaseHistorySerializer


# ComplaintRouting Views
class ComplaintRoutingListCreateView(generics.ListCreateAPIView):
    queryset = ComplaintRouting.objects.all()
    serializer_class = ComplaintRoutingSerializer


class ComplaintRoutingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComplaintRouting.objects.all()
    serializer_class = ComplaintRoutingSerializer


# Complaint Views
class ComplaintListCreateView(generics.ListCreateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer


class ComplaintRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer