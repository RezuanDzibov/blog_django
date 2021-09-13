"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user_account import views as user_account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', user_account_views.LoginView.as_view(), name='signin'),
    path('accounts/register/', user_account_views.RegisterCreateView.as_view(), name='signup'),
    path('accounts/',  include('django.contrib.auth.urls')),
    path('accounts/', include('user_account.urls', namespace='user_account')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/user_account/', include('user_account.api.urls')),
    path('api/blog/', include('blog.api.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)