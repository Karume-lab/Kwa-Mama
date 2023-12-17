from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for contacting us!")
    return render(request, "core/index.html")


def home(request):
    return render(request, "core/home.html")


def feedback(request):
    return render(request, "core/feedback.html")

def catering(request):
    return render(request,"core/catering.html")
