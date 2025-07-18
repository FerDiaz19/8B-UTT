from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('crear/', views.todo_create, name="todo_create"),
    path('editar/<int:pk>/', views.todo_update, name="todo_update"),
    path('eliminar/<int:pk>/', views.todo_delete, name="todo_delete"),

    path('usuarios/nuevo/', views.user_create, name='user_create'),
    path('usuarios/', views.user_list, name='user_list'),
    path('usuarios/editar/<int:pk>/', views.user_update, name='user_update'),
    path('usuarios/eliminar/<int:pk>/', views.user_delete, name='user_delete'),

    path('solo_ids/', views.todos_ids, name="todos_ids"),
    path('ids_titles/', views.todos_ids_titles, name="todos_ids_titles"),
    path('resueltos/', views.todos_resueltos, name="todos_resueltos"),
    path('no_resueltos/', views.todos_no_resueltos, name="todos_no_resueltos"),
    path('ids_user/', views.todos_ids_user, name="todos_ids_user"),
    path('resueltos_user/', views.todos_resueltos_user, name="todos_resueltos_user"),
    path('no_resueltos_user/', views.todos_no_resueltos_user, name="todos_no_resueltos_user"),
    path('editar/<int:pk>/', views.todo_update, name="todo_update"),
    path('eliminar/<int:pk>/', views.todo_delete, name="todo_delete"),
]
