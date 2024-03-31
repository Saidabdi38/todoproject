from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_form, name='task_insert'),
    path('<int:id>/', views.task_form, name='task_update'),
    #path('delete/<int:id>/', views.task_delete, name='task_delete'),
    path('search/', views.searchtask, name='searchtask'),
    path('notlist/', views.not_complete, name='not_complete'),
    path('list/', views.task_list, name='task_list')
]