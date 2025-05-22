from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path('dashboard/', views.menu_view, name='dashboard'),
    path('opcion1/', views.menu_view, name='opcion1'),
    path('opcion2/', views.menu_view, name='opcion2'),
    path('opcion3/', views.menu_view, name='opcion3'),
    path('opcion4/', views.menu_view, name='opcion4'),
]
