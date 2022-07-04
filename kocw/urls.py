from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.kocw),
    path('edwith/', include('edwith.urls'), name='edwith'),
    path('kmooc/', include('kmooc.urls'), name='kmooc'),
    path('kocw/', include('kocw.urls'), name='kocw'),
]