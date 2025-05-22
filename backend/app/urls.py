from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('opcion1/', views.dashboard_view, name='opcion1'),
    path('opcion2/', views.dashboard_view, name='opcion2'),
    path('opcion3/', views.dashboard_view, name='opcion3'),
    path('opcion4/', views.dashboard_view, name='opcion4'),
]
