from django.urls import path

from bag import views

urlpatterns = [
    path('', views.bag_view, name="bag"),
]