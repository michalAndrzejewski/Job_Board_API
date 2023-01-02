"""
URL mappings for the job listing app
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import JobListingViewSet


router = DefaultRouter()
router.register('job_listings', JobListingViewSet)

app_name = 'job_listing'

urlpatterns = [
    path('', include(router.urls)),
]