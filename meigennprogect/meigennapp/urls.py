from django.urls import path
from .views import Listfunc, Detailfunc, Createfunc, Deletefunc, Updatefunc

urlpatterns = [
    path('list/', Listfunc.as_view(), name='list'),
    path('detail/<int:pk>', Detailfunc.as_view(), name='detail'),
    path('create/', Createfunc.as_view(), name='create'),
    path('delete/<int:pk>', Deletefunc.as_view(), name='delete'),
    path('update/<int:pk>', Updatefunc.as_view(), name='update'),
]