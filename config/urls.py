from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # API endpoint - Catalog
    path('api/', include('catalog.urls')),

    # API Endpoint - Authnetication
    path('api/auth/', include('user_auth.urls')),

    # JWT Built-in views (login and token refresh)
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger Documentation (Auto-generated)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
