"""tryDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView
    )
from django.urls import path, include
from users.views import register_view, profile_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('profile/', profile_view, name='profile'),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
            PasswordResetView.as_view(template_name='users/password_reset.html'),
            name='password_reset'
    ),
    path('password-reset/done/',
            PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
            name='password-reset-done'
    ),
    path('password-reset-confirm/<uidb64>/<token>/',
            PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
            name='password-reset-confirm'
    )
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
