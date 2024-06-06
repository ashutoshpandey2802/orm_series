from django.shortcuts import render
from .forms import Ratingform
# Create your views here.


def index(request):
    if request.method =='POST':
        form=Ratingform(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'index.html',{'form':form}  )
        
    context={'form':Ratingform()}
    return render(request,'index.html',context)