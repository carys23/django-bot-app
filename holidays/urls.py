from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('countries/', views.countries, name="countries"),
    path('asia/', views.asia, name="asia"),
    path('australia/', views.africa, name="australia"),
    path('antarctica/', views.africa, name="antarctica"),
    path('africa/', views.africa, name="antarctica"),
    path('europe', views.africa, name="europe"),
    path('south_america/', views.africa, name="south_america"),
]