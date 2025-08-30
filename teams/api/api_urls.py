from django.urls import path
from teams.api.api_view import OrganizationListCreateView, OrganizationDetailView

urlpatterns = [
    path('organization/', OrganizationListCreateView.as_view()),
    path('organization/<int:pk>/', OrganizationDetailView.as_view())
]