from django.db import models
from django import forms

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    
class Feedback(forms.Form):
    FEEDBACK_CHOICES = [
        ('in_house', 'In-house services'),
        ('catering', 'Catering services'),
    ]

    feedback_type = forms.ChoiceField(
        choices=FEEDBACK_CHOICES,
        widget=forms.RadioSelect,
        required=True,
    )
    names = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    def __str__(self):
        return f"{self.names} - {self.email}"
    