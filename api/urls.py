from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('categories/<str:pk>', views.categoriesDetails.as_view(), name='categoriesDetail'),
    path('latestMusic/', views.latestMusic.as_view(), name='latestMusic'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/register/', views.registerUser.as_view(), name='register'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('categories/', views.categoriesList.as_view(), name='categories'),
    path('doc/',SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
