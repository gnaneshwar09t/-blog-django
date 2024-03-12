from django.shortcuts import render,redirect
from education.models import edu_model
from education.forms import edumodelform
from app1.forms import samplemodelform


# Create your views here.

def education(request):
    result = edu_model.objects.all().order_by('-id');
    dict1 = {'key1':result}
    return render(request,'education_mainpage.html',dict1)

def create(request):
    form= samplemodelform
    dict2={'key2':form}
    if request.method=="POST":
        form2=edumodelform(request.POST)
        if form2.is_valid():
            post1 = form2.save(commit=False)
            post1.author = request.user
            post1.save()
        form=samplemodelform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

        return redirect('education')
    return render(request,'page2.html',dict2)





