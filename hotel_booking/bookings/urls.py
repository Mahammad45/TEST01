from django.urls import path
from django.contrib.auth import views as auth_views , views 
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomViewSet

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),  # Для регистрации
]

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns += router.urls
