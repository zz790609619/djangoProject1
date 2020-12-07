from django.urls import path, re_path

from APP import views

# 路由配置 可以多个路由对应一个视图
urlpatterns = [
    # path(访问路径.视图层,路由名称)
    path('testGetData', views.testGetData, name='testGetData'),
    path('calOneTable', views.calOneTable, name='calOneTable'),
    path('calAllTable', views.calAllTable, name='calAllTable'),
    path('add', views.add, name='add'),
    path('init', views.init, name='init'),
    # 带参数
    # slug 获取路径的数据 数字，字母，_，
    # path 获取路径的数据 任意数据
    path('calAllTable/<int:id>', views.calAllTablePath, name='init'),

    # re_path和path 区别是匹配的是正则模式串
    # re_path(r'/repath/(\d{0,8})', views.repath, name='repath'),
]
