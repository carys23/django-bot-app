from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('continents/', views.continents, name="continents"),
    path('login/', views.login, name="login")
]