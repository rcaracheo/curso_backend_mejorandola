# Create your views here.
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import Context
from django.template.context import RequestContext
from django.template.loader import get_template

from app.forms import EnlaceForm
from models import *


def hora_actual(request):
    ahora = datetime.now()
    t = get_template("hora.html")
    c = Context({"hora":ahora})
    html = t.render(c)
    return HttpResponse(html)
    
def home(request):
    categorias = Categoria.objects.all()
    enlaces    = Enlace.objects.order_by("-votos").all()
    
    template = "index.html"
    return render(request,template,locals())

def categoria(request,id_categoria):
    categorias = Categoria.objects.all()
    #cat        = Categoria.objects.get(pk=id_categoria)
    
    cat      = get_object_or_404(Categoria,pk =id_categoria)
    enlaces  = Enlace.objects.filter(categorias=cat)
    
    template = "index.html"
    return render(request,template,locals())

@login_required
def plus(request,id_enlace):
    enlace = Enlace.objects.get(pk=id_enlace)
    enlace.votos +=1
    enlace.save()
    return HttpResponseRedirect("/")

@login_required
def minus(request,id_enlace):
    enlace = Enlace.objects.get(pk=id_enlace)
    enlace.votos -=1
    enlace.save()
    return HttpResponseRedirect("/")

@login_required
def add(request):
    if request.method == "POST":
        form = EnlaceForm(request.POST)  
        if form.is_valid():
            enlace = form.save(commit = False)
            enlace.usuario = request.user
            enlace.save()
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = EnlaceForm()
    
    template = "form.html"
    return render_to_response(template,context_instance= RequestContext(request,locals()))
        
