from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet) #No need basename because queryset define auto

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]