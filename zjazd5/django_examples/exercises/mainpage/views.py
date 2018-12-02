# Create your views here.

from django.http import HttpResponse


def main_page(request):
    return HttpResponse(content="Main Page !!!")

def hello_world(request):
    return HttpResponse(content="Hello World")

def hello_personalized(request, name,lastname):
    return HttpResponse(content=f"Hello {name } {lastname}")

def product(request):
    return HttpResponse(content="Strona z produktami")

# def calc(request, dzialanie, wart1, wart2):
#     wynik = None
#     if dzialanie == 'add':
#         wynik = int(wart1)+int(wart2)
#     elif dzialanie =='sub':
#         wynik = int(wart1)-int(wart2)
#     elif dzialanie =='mult':
#         wynik = int(wart1)*int(wart2)
#
#
#     return HttpResponse(content=f"Wynik {calc} wynosi: {wynik} ")