from django.urls import path
from entertainment import views

urlpatterns = [

    path('entertainment',views.entertainment,name="entertainment"),
    path('create_ent_blog',views.create,name='create_ent_blog'),
    

]