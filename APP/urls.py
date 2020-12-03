from django.urls import path

from APP import views

urlpatterns = [
    path('calOneTable', views.calOneTable, name='calOneTable'),
    path('calAllTable', views.calAllTable, name='calAllTable'),
    path('add', views.add, name='add'),
    path('init', views.init, name='init'),
]
