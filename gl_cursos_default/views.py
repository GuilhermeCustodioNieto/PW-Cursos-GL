from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'gl_cursos_default/index.html')