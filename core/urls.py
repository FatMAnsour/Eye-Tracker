from django.urls import path
from . import views

urlpatterns = [
    path('eyeTracker/', views.ImageView.as_view()),
]
