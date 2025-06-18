from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('opcion1/', views.dashboard_view, name='opcion1'),
    path('opcion2/', views.dashboard_view, name='opcion2'),
    path('opcion3/', views.dashboard_view, name='opcion3'),
    path('opcion4/', views.dashboard_view, name='opcion4'),
    path('otp/', views.otp_view, name='otp'),
    path('agregarservidor/', views.agregarServidor, name='agregarservidor'),
    path('levantarServicio/', views.levantar_servicio, name='levantarServicio'),
    path('administrar_servicios/', views.administrar_servicios, name='administrar_servicios'),
    path('monitor/', views.monitor_servicios_view, name='monitor_servicios'),
    path('api/estado_servicios/', views.estado_servicios_api, name='estado_servicios_api'),
    path('editar-servidores/', views.editar_servidores, name='editar_servidores'),
]
