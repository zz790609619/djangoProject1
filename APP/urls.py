from django.urls import path

from APP import views

urlpatterns = [
    path('getDataBase', views.cal, name='getDataBase'),
    path('addDataBase', views.add, name='addDataBase'),
    path('createDataBase', views.create, name='createDataBase'),
]
