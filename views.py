from django.shortcuts import render,redirect
from technology.models import tech_model
from technology.forms import techmodelform
from app1.forms import samplemodelform


# Create your views here.

def technology(request):
    result = tech_model.objects.all().order_by('-id');
    dict1 = {'key1':result}
    return render(request,'technology_mainpage.html',dict1)



def create(request):
    form= samplemodelform
    dict2={'key2':form}
    if request.method=="POST":
        form2=techmodelform(request.POST)
        if form2.is_valid():
            post1 = form2.save(commit=False)
            post1.author = request.user
            post1.save()
        form=samplemodelform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
        return redirect('technology')
    return render(request,'page2.html',dict2)


    
