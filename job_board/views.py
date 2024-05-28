from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import JobPosting

def index(request):
    job = JobPosting.objects.filter(is_active=True)
    print(job)
    context = {
        'jobs': job
    }
    return render (request, 'job_board/index.html', context)


def details(request, pk):
    job = get_object_or_404(JobPosting, pk=pk, is_active=True)
    context = {
        'singleJobs': job
    }
    return render (request, 'job_board/details.html', context)