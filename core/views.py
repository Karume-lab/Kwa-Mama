from django.shortcuts import render, redirect
from . import forms
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for contacting us!")
    else:
        form = forms.ContactForm()
    return render(request, "core/index.html", {"form": form})


def home(request):
    return render(request, "core/home.html")


def feedback(request):
    return render(request, "core/feedback.html")


def catering(request):
    return render(request, "core/catering.html")
