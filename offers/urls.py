from django.urls import path

from offers import views

urlpatterns = [
    path('', views.offers_view, name="offers"),
    path('<int:offer_id>/', views.offer_details, name="offer_details"),
]