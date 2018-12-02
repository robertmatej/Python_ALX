from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from maths.models import Math
from django.shortcuts import render


def calculate(operation,wart1,wart2):
    wynik = None
    if operation == 'add':
        wynik = int(wart1)+int(wart2)
    elif operation == 'sub':
        wynik = int(wart1)-int(wart2)
    elif operation == 'mult':
        wynik = int(wart1)*int(wart2)
    return wynik


# Create your views here.


#@login_required()                 # powoduje że wymagane jst logowanie dla metody calc (dodanie nowtch wart do baz)

def calc(request, operation, wart1, wart2):
    Math.objects.create(operation=operation,wart1=wart1,wart2=wart2)
    return HttpResponse(calculate(operation, wart1, wart2))


def math_list(request):
    objects = Math.objects.all()
    out = ""
    for o in objects:
        out += f'{o.operation}:{o.wart1} {o.wart2} <br>'

#    return HttpResponse(out)
    return render(request=request, template_name="math_list.html", context={"maths":objects})

def math_details(request, id):
    Math.objects.get(pk=id)

    out = f'''
    Operacja: {m.operation}<br>
    arg 1: {wart1}<br>
    arg 2: {wart2}<br>
    -------------------
    wynik: {calculate(m.operation, m.wart1, m.wart2)} <br>
    
    '''
    return HttpResponse(out)