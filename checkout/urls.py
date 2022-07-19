from django.urls import path

from checkout import views
from checkout.webhooks import webhook

urlpatterns = [
    path('', views.checkout_view, name="checkout"),
    path('cache_checkout_data/', views.cache_checkout_data, name="cache_checkout_data"),
    path('checkout_success/<order_number>/', views.checkout_success, name="checkout_success"),
    path('wh/', webhook, name='webhook'),
]