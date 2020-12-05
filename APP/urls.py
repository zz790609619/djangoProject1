from django.urls import path

from APP import views

# 路由配置
urlpatterns = [
    # path(访问路径.视图层)
    path('calOneTable', views.calOneTable, name='calOneTable'),
    path('calAllTable', views.calAllTable, name='calAllTable'),
    path('add', views.add, name='add'),
    path('init', views.init, name='init'),
    # 带参数
    path('calAllTable/<int:id>', views.calAllTablePath, name='init'),
]
