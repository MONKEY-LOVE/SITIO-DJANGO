
from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('productos/', views.productos, name='productos'),
    path('horario/', views.horario, name='horario'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('comentarios/', views.lista_comentarios, name='lista_comentarios'),
]