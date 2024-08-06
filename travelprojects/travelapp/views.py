from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Place
from.models import photos


# Create your views here.
#def demo(request):
  # return HttpResponse("home")
from django.shortcuts import render
from .models import Place, photos

def demo(request):
    obj = Place.objects.all()
    photos_list = photos.objects.all()
    return render(request, 'index.html', {'result': obj, 'image': photos_list})

#def terminal(request):
  # return render(request,'terminal.html')
#def app(request):
  # return HttpResponse("google")
#def operator(request):
   #x=int(request.GET['num1'])
   #y=int(request.GET['num2'])
   #res=x+y
   #sub=x-y
  # multi=x*y

  # return render(request,"terminal.html",{'result':res,'subs':sub,'mult':multi})


