from django.urls import path

from .views import index, details

urlpatterns = [
    path('', index),
    path('jobs/<int:pk>/', details, name="job-detail")
]
