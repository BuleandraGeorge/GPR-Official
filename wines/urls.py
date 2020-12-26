from django.urls import path

from wines import views

urlpatterns = [
    path('', views.wines_view, name="wines_view"),
]