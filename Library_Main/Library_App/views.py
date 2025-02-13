from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *

# Create your views here.
def home(request):
    return render(request,"home.html",context={"current_tab":"HOME"})

def readers_tab(request):
    if request.method == "GET":
        readers = reader.objects.all()
        return render(request,"readers.html",context={"current_tab":"readers","readers":readers})
    else :
        query = request.POST["query"]
        readers = reader.objects.raw("select * from Library_App_reader where reader_name like '%"+query+"%'")
        return render(request,"readers.html",context={"current_tab":"readers","readers":readers,"query":query})

def save_reader(request):
    reader_item =  reader(
    reference_id = request.POST["reader_ref_id"],
    reader_name = request.POST["reader_name"],
    reader_contact = request.POST["reader_contact"],
    reader_address = request.POST["address"],
    active=True
    )
    reader_item.save()
    return redirect('/readers')

# def readers_tab(request):
#     readers = reader.object.all()
#     return render(request,"readers.html",context={"current_tab":"readers","readers":readers})
