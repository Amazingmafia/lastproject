from .import views
from django.urls import path
urlpatterns = [
    path('',views.demo,name='demo'),
    #path('terminal/',views.terminal,name='terminal')
    #path('add/',views.operator,name='addition'),

]
