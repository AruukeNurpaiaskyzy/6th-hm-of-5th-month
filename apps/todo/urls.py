from django.urls import path
from .views import ListCreateView, ListDetailView, DeleteAllListView

urlpatterns = [
    path('lists/', ListCreateView.as_view(), name='list-list-create'),
    path('lists/<int:pk>/', ListDetailView.as_view(), name='list-detail'),
    path('listss/delete-all/', DeleteAllListView.as_view(), name='list-all-todos'),
]
