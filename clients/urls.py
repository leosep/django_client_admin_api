# urls.py
from django.urls import path
from .views import ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView

urlpatterns = [
    path('api/clients/', ClientListView.as_view(), name='client-list'),
    path('api/clients/create/', ClientCreateView.as_view(), name='client-create'),
    path('api/clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('api/clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('api/clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
]
