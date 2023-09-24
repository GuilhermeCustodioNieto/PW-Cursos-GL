from django.shortcuts import render

# Create your views here.
def menu_principal(request):
    return render(request, 'gl_cursos_default/menu_principal.html')

def inteligencia_artificial(request):
    return render(request, 'gl_cursos_default/inteligencia_artificial.html')

def curso_front(request):
    return render(request, 'gl_cursos_default/curso_front.html')

def curso_back(request):
    return render(request, 'gl_cursos_default/curso_back.html')