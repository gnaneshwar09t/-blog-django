from django.urls import path
from app1 import views


urlpatterns = [
    
    path('allblogs',views.fun1,name="page1"),
    path('',views.mainpage,name='main'),
    path('create_blog',views.fun2,name='page2'),
    path('user',views.user_posts,name='user_posts'),
    path('delete/<int:id>',views.deletestudent,name='delete'),
    path('update/<int:id>',views.updatestudent,name='update'),
]
