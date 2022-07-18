from django.urls import path

from checkout import views

urlpatterns = [
    path('', views.checkout_view, name="checkout"),
    path("create-payment-intent", views.create_payment, name="create_payment")
    path('checkout_success/<order_number>/', views.checkout_success, name="checkout_success"),
]