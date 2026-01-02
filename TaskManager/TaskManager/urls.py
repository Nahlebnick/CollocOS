from django.contrib import admin
from django.urls import path
from main.views import TaskAPIView, RegisterAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tasks/', TaskAPIView.as_view(),  name='tasks'),
    path('api/v1/tasks/<int:pk>/', TaskAPIView.as_view(),  name='tasks/<int:pk>'),
    path('api/v1/token/', TokenObtainPairView.as_view()),
    path('api/v1/token/refresh/', TokenRefreshView.as_view()),
    path('api/v1/register/', RegisterAPIView.as_view()),
]
