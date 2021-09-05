from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new-task'),
    path('edit/<int:id>', views.editView, name='edit-view'),
    path('delete/<int:id>', views.deleteView, name='delete-view'),
    
   
]