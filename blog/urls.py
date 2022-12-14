"""simple_ap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from blog import admin
from django.urls import path, include
from blog.views import index, post_list, post_detail, PostViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post_viewset', PostViewSet, 'post_model_viewset')
router.register('users', UserViewSet, 'users')

urlpatterns = router.urls


urlpatterns.append(path('', index))
urlpatterns.append(path('posts/', post_list))
urlpatterns.append(path('posts/<int:pk>', post_detail))

# urlpatterns = [
#     path('',include(router)
#     path('', index),
#     path('posts/', post_list),
#     path('posts/<int:pk>', post_detail),

# ]
