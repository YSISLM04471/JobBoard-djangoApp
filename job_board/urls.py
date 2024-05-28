from django.urls import path

from .views import index, details

urlpatterns = [
    path('', index, name="home"),
    path('jobs/<int:pk>/', details, name="job-detail")
]
