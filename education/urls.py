from django.urls import path
from education import views

urlpatterns = [

    path('education',views.education,name="education"),
    path('create_edu_blog',views.create,name='create_edu_blog'),
    
    

]