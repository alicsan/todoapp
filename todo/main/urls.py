from django.urls import path
from main import views

urlpatterns=[
    path('',views.home, name="Home"),
    path('v/',views.v,name="View"),
    path('c/',views.create,name="Create"),
    path('add_todo/',views.add_todo,name="Add"),
]