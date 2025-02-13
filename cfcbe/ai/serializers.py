from rest_framework import serializers
from .models import TriageRule, TriageAnalysis, Department, CaseHistory, ComplaintRouting, Complaint

class TriageRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriageRule
        fields = '__all__'

class TriageAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriageAnalysis
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class CaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseHistory
        fields = '__all__'

class ComplaintRoutingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintRouting
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'