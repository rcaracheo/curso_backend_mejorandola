'''
Created on 26-12-2013

@author: mercenario
'''

from random import choice
from django.core.urlresolvers import reverse

frases = ["olo","mono loco","vanino esta en la cama"]

def ejemplo(request):
    return {'frase':choice(frases)}


def menu(request):
    menu= {"menu":[
           {"name":"Home","url":reverse("home")},
           {"name":"Add" ,"url":reverse("add")},
           {"name":"Acerca de" ,"url":reverse("about")}
           ]}
    for item in menu["menu"]:
        if request.path == item["url"]:
            item["active"] = True
    return menu