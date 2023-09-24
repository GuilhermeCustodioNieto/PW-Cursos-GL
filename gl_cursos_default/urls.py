from django.urls import path, include
from . import views

app_name = 'gl_cursos_default'

urlpatterns = [
    path('menu_principal/', views.menu_principal, name='menu_principal'),
    path('inteligencia_artificial/', views.inteligencia_artificial, name='inteligencia_artificial'),
    path('curso_front/', views.curso_front, name='curso_front'),
    path('curso_back/', views.curso_back, name='curso_back'),
]