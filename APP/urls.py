from django.urls import path

from APP import views

urlpatterns = [
    path('calOneTable', views.calOneTable, name='calOneTable'),
    path('calAllTable', views.calAllTable, name='calAllTable'),
    path('add', views.add, name='add'),
    path('init', views.init, name='init'),
    # 带参数
    path('calAllTable/<int:id>', views.calAllTablePath, name='init'),
]
