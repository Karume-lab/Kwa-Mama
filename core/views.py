from django.shortcuts import render, redirect
from .forms import FeedbackForm, ContactForm
from django.http import HttpResponse
from .forms import FeedbackForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for contacting us!")
    return render(request, "core/index.html")


def home(request):
    return render(request, "core/home.html")

def catering(request):
    return render(request,"core/catering.html")

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for your feedback!")

    return render(request, 'core/feedback.html')
