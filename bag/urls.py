from django.urls import path

from bag import views

urlpatterns = [
    path('', views.bag_view, name="bag"),
    path('<int:wine_id>/', views.add_to_bag, name="add_to_bag"),
]