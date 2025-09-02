from django.urls import path
from teams.api.api_view import OrganizationListCreateView, OrganizationDetailView, CustomTokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('organization/', OrganizationListCreateView.as_view()),
    path('organization/<int:pk>/', OrganizationDetailView.as_view())
]

urlpatterns += [
    path('login/', CustomTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]