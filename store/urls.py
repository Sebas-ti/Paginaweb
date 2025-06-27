
from django.urls import path
from store import views

urlpatterns = [
    path('', views.index),
    path('about/',views.about),
    path('hello/<str:username>', views.hello),
    path('products/',views.products),
    path('proyects/',views.proyects)
]
