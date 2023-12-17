from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class FeedbackForm(forms.Form):
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
