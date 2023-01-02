"""
Serializers for job listing APIs
"""
from rest_framework import serializers

from core.models import JobListing


class JobListingSerializer(serializers.ModelSerializer):
    """Job listing serializer."""

    class Meta:
        model = JobListing
        fields = [
            'id',
            'company',
            'job_title',
            'job_seniority',
            'job_description',
            'salary_max',
            'salary_min',
            'date_added',
        ]
        read_only_fields = ['id', 'date_added',]
