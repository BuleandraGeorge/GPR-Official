from django.urls import path

from . import views

urlpatterns = [
    path('listing/', views.requirements, name="requirements"),
    path('declined/', views.access_denied, name="access_denied"),
]