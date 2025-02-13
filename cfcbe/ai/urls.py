from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('triage-rules/', views.TriageRuleListCreateView.as_view(), name='triage-rule-list-create'),
    path('triage-rules/<int:pk>/', views.TriageRuleRetrieveUpdateDestroyView.as_view(), name='triage-rule-detail'),
    path('triage-analyses/', views.TriageAnalysisListCreateView.as_view(), name='triage-analysis-list-create'),
    path('triage-analyses/<int:pk>/', views.TriageAnalysisRetrieveUpdateDestroyView.as_view(), name='triage-analysis-detail'),
    path('departments/', views.DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', views.DepartmentRetrieveUpdateDestroyView.as_view(), name='department-detail'),
    path('case-histories/', views.CaseHistoryListCreateView.as_view(), name='case-history-list-create'),
    path('case-histories/<int:pk>/', views.CaseHistoryRetrieveUpdateDestroyView.as_view(), name='case-history-detail'),
    path('complaint-routings/', views.ComplaintRoutingListCreateView.as_view(), name='complaint-routing-list-create'),
    path('complaint-routings/<int:pk>/', views.ComplaintRoutingRetrieveUpdateDestroyView.as_view(), name='complaint-routing-detail'),
    path('complaints/', views.ComplaintListCreateView.as_view(), name='complaint-list-create'),
    path('complaints/<int:pk>/', views.ComplaintRetrieveUpdateDestroyView.as_view(), name='complaint-detail'),
]


