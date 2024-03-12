from django.shortcuts import render,redirect
from app1.models import model2
from app1.forms import samplemodelform
from django.contrib.auth.decorators import login_required
from education.models import edu_model
from entertainment.models import ent_model
from education.forms import edumodelform
from technology.models import tech_model
from others.models import ot_model
from entertainment.forms import entmodelform
from technology.forms import techmodelform
from others.forms import otmodelform
from django.http import HttpResponseServerError
from app1.forms import usermodelform
from django.core.mail import send_mail
from django.conf import settings
from app1.models import userclass
from django.contrib.auth.models import User

# Create your views here.
def registerpage(request):
    user_form = usermodelform

    if request.method == 'POST':
        user_form = usermodelform(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            # Save the email in the userclass model
            userclass_form = userclass(email=user.email)
            userclass_form.save()

            return redirect('main')

    dic = {'user_form': user_form}
    return render(request, 'registration/register.html', dic)



@login_required
def mainpage(request):
    education_topics = edu_model.objects.order_by('-id')
    entertainment_topics=ent_model.objects.order_by('-id');
    technology_topics=tech_model.objects.order_by('-id');
    ot_topics=ot_model.objects.order_by('-id');
    dictionary={'key':education_topics,'key1':entertainment_topics,'key2':technology_topics,'key3':ot_topics}
    return render(request,'index.html',dictionary)

@login_required
def fun2(request):
    form= samplemodelform
    dict2={'key2':form}
    if request.method=="POST":
        form=samplemodelform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if post.category in ["education","EDUCATION","Education"]:
                form2=edumodelform(request.POST)
                if form2.is_valid():
                    post1 = form2.save(commit=False)
                    post1.author = request.user
                    post1.save()
            elif post.category in ["entertainment","ENTERTAINMENT","ENTERTAINMENT"]:
                form2=entmodelform(request.POST)
                if form2.is_valid():
                    post1 = form2.save(commit=False)
                    post1.author = request.user
                    post1.save()
            elif post.category in ["technology","TECHNOLOGY","Technology"]:
                form2=techmodelform(request.POST)
                if form2.is_valid():
                    post1 = form2.save(commit=False)
                    post1.author = request.user
                    post1.save()
            else :
                form2=otmodelform(request.POST)
                if form2.is_valid():
                    post1 = form2.save(commit=False)
                    post1.author = request.user
                    post1.save()
            post.save()
        return redirect('page1') #------> the redirect function takes the name of the url page as the argument
    return render(request,'page2.html',dict2)

@login_required
def fun1(request):
    result = model2.objects.all().order_by('-id');
    dict1 = {'key1':result}
    return render(request,'page1.html',dict1)

@login_required
def user_posts(request):
    user_posts=model2.objects.filter(author=request.user)
    return render(request,'page3.html',{'user_posts':user_posts})



def delete_from_edu_model(topic):
    try:
        edu_entry = edu_model.objects.get(topic=topic)
        edu_entry.delete()
    except edu_model.DoesNotExist:
        # Log or handle the exception as needed
        pass

def delete_from_ent_model(topic):
    try:
        ent_entry = ent_model.objects.get(topic=topic)
        ent_entry.delete()
    except ent_model.DoesNotExist:
        # Log or handle the exception as needed
        pass

def delete_from_tech_model(topic):
    try:
        tech_entry = tech_model.objects.get(topic=topic)
        tech_entry.delete()
    except tech_model.DoesNotExist:
        # Log or handle the exception as needed
        pass

def delete_from_ot_model(topic):
    try:
        ot_entry = ot_model.objects.get(topic=topic)
        ot_entry.delete()
    except ot_model.DoesNotExist:
        # Log or handle the exception as needed
        pass

@login_required
def deletestudent(request, id):
    s = model2.objects.get(id=id)

    try:
        # Delete from edu_model
        delete_from_edu_model(s.topic)

        # Delete from ent_model
        delete_from_ent_model(s.topic)

        # Delete from tech_model
        delete_from_tech_model(s.topic)

        # Delete from ot_model
        delete_from_ot_model(s.topic)

        # Delete from model2
        s.delete()

        return redirect(user_posts)

    except Exception as e:
        # Log or print the error for debugging
        print(e)
        return HttpResponseServerError("Internal Server Error")



@login_required
def updatestudent(request, id):
    post = model2.objects.get(id=id)
    form = samplemodelform(instance=post)
    dic = {'form': form, 'post_id': id}  # Passing post_id to identify the post
    if request.method == "POST":
        form = samplemodelform(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return user_posts(request)
    return render(request, 'update_post.html', dic)

def forgot_password(request):
        if request.method=="POST":
            mail = request.POST['email']

            # store_mail = userclass.objects.get(email=mail)   
            # store_mail.save()

            check_mail = userclass.objects.get(email=mail)
            print(check_mail.email)
            subject = 'password chnage for blog website'
            message = "<a>http://127.0.0.1:8000/password_reset/</a>"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [check_mail.email]
            send_mail( subject, message, email_from, recipient_list )
            
    # except:
    #     msg="NO email found"
    #     return render(request,'forgot_password.html',{'msg':msg})
        return render (request,"forgot_password.html")

def password_reset(request):
    if request.method=="POST":
        password=request.POST['password']
        confirm_password=request.POST['confirm-password']
        if password==confirm_password:
            check_email = userclass.objects.all().first()
            email = User.objects.get(email=check_email.email)
            email.set_password(password)
            email.save()
            
    return render(request,'password_reset.html')





