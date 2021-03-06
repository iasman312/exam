from django.urls import path
from .views import (index_view,
                    feedback_create_view,
                    feedback_update_view,
                    feedback_delete_view
)

urlpatterns = [
    path('', index_view, name='feedback-list'),
    path('add/', feedback_create_view, name='feedback-add'),
    path('<int:pk>/update', feedback_update_view, name='feedback-update'),
    path('<int:pk>/delete', feedback_delete_view, name='feedback-delete')
]