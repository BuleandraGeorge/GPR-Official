from django.urls import path

from profiles import views

urlpatterns = [
    path('', views.view_profile, name="profiles"),
]