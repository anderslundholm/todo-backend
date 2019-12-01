from django.urls import path
from todos import views


urlpatterns = [
    path(
        'api/v1/todos/<int:pk>',
        views.get_delete_update_todo,
        name='get_delete_update_todo'
    ),
    path(
        'api/v1/todos/',
        views.get_post_todos,
        name='get_post_todos'
    )
]
