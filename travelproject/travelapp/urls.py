from .import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('about/',views.about,name='about'),
    # path('new/',views.new,name="new"),
    # path('add/',views.addition,name='addition')

]