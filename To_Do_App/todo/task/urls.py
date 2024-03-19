from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
	path('tasks/', views.task_list, name="task"),
	# pass item_id as primary key to remove that the todo with given id
	path('del/<str:item_id>', views.remove, name="del"),
    path('edit/<str:item_id>',views.edit,name='edit'),
    path('toggle/<str:item_id>', views.toggle_status, name='toggle_status'),
	
]
