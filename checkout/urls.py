from django.urls import path

from checkout import views

urlpatterns = [
    path('', views.checkout_view, name="checkout"),
    path('checkout_success/<order_number>/', views.checkout_success, name="checkout_success"),
]