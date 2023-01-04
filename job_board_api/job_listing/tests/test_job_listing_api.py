"""
Tests for job listings APIs.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import JobListing
from job_listing.views import JobListingViewSet

from job_listing.serializers import JobListingSerializer


JOB_LISTING_URL = reverse('job_listing:job_listing-list')


def create_job_listing(user, **params):
    """Create and return a sample job listing."""
    defaults = {
        'company': 'Test company',
        'job_title': 'Test job listing',
        'job_seniority': 'Senior',
        'job_description': 'This is a test job listing',
        'salary_max': 4000,
        'salary_min': 5000,
    }
    defaults.update(params)

    job_listing = JobListing.objects.create(user=user, **defaults)
    return job_listing


class PublicJobListingApiTests(TestCase):
    """Test unauthenticated API requests."""
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API"""
        res = self.client.get(JOB_LISTING_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateJobListingApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'password123',
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_job_listings(self):
        """Test retrieving a list of job listings"""
        create_job_listing(user=self.user)

        res = self.client.get(JOB_LISTING_URL)

        job_listings = JobListing.objects.all().order_by('-id')
        serializer = JobListingSerializer(job_listings, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_creating_job_listing_user(self):
        """Test creating job listing with user"""
        job_listing_test_data = {
            'user': self.user,
            'company': 'Test Company',
            'job_title': 'Test job listing',
            'job_seniority': 'Senior',
            'job_description': 'This is a test job listing',
            'salary_max': 4000,
            'salary_min': 5000,
        }
        res = self.client.post(JOB_LISTING_URL, data=job_listing_test_data)

        job_listing = JobListing.objects.all()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(job_listing[0].user, self.user)
