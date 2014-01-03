from django.shortcuts import redirect
from random import choice


paises = ['Combia','Peru','Panama','Chile']
#identificar segun la ip
def de_donde_vengo(request):
    return choice(paises)

class PaisMiddleware():
    def process_request(self,request):
        pais = de_donde_vengo(request)
        print '*' *30
        print pais
        print '*' *30
#         if pais == 'Chile':
#             return redirect('http://www.mejorandola.la')
#         else:
#             print "otro pais"
#             print pais
#     