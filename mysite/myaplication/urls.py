from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('001', views.index1, name='index1'),
    path('002', views.index2, name='index2'),
    path('003', views.index3, name='index3'),
    path('004', views.index4, name='index4'),
    path('005', views.index5, name='index5'),
    path('006', views.django1, name='django1'),

]