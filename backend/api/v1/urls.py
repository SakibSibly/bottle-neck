from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from . import views


urlpatterns = [
    # OpenAPI schema
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # ReDoc
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # JWT
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', views.CustomTokenRefreshView.as_view(), name='token-refresh'),

    # Other API endpoints
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('users/me/', views.)

    path('blogs/', views.BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
]
