from django.urls import path
from technology import views

urlpatterns = [

    path('technology',views.technology,name="technology"),
    path('create_tech_blog',views.create,name='create_tech_blog'),
    

]