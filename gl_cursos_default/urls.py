from django.urls import path, include
from . import views

app_name = 'gl_cursos_default'

urlpatterns = [
    path('index/', views.index, name='index'),
]