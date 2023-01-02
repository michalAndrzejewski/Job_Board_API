"""
Views for the job listing APIs
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import JobListing
from .serializers import JobListingSerializer


class JobListingViewSet(viewsets.ModelViewSet):
    """View for manage job listing APIs"""
    serializer_class = JobListingSerializer
    queryset = JobListing.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve job listings for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

