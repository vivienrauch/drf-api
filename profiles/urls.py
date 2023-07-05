from django.urls import path
from profiles import views

urlpattern = [
    path('profiles/', views.ProfileList.as_view()),
]