from django.urls import path,include
from .views import contact_us
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("feedback/", views.feedback, name="feedback"),
    path("catering/", views.catering, name="catering"),
    path('contact_us/', views.contact_us, name='contact_us'),
    # path('core/', include('core.urls')),
]
