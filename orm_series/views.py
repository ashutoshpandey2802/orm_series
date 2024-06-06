from django.shortcuts import render
from django.http import HttpResponse
from core.forms import Ratingform

def index(request):
    # return render(request, "index.html")
    if request.method =='POST':
        form=Ratingform(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'index.html',{'form':form}  )
        
    context={'form':Ratingform()}
    return render(request,'index.html',context)