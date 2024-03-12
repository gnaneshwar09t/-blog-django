from django.urls import path
from others import views

urlpatterns = [

    path('other',views.technology,name="other"),
    path('create_ot_blog',views.create,name='create_ot_blog'),
    

]