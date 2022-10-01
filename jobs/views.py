from django.shortcuts import render, get_object_or_404
from .models import Job


def index(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/index.html', {'jobs': jobs})


def resume(request):
    return render(request, 'jobs/resume.html')


def about(request):
    return render(request, 'jobs/about.html')


def services(request):
    return render(request, 'jobs/services.html')


def portfolio(request):
    jobs = Job.objects.all()
    print(jobs)
    return render(request, 'jobs/portfolio.html', {'jobs': jobs})


def contact(request):
    return render(request, 'jobs/contact.html')


def portfolio_detail(request, job_id):
    jobs = Job.objects.all()
    job = get_object_or_404(jobs, pk=job_id)
    return render(request, 'jobs/portfolio_detail.html', {'job': job})
