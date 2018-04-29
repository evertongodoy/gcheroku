"""gestao_clientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from clientes import urls as clientes_urls

from django.conf import settings
from django.conf.urls.static import static

# Secao 4, video 23
from django.contrib.auth import views as auth_views

# Secao 4, video 24
from home import urls as home_urls

urlpatterns = [
	path('', include(home_urls)),
	path('clientes/', include(clientes_urls)),
	# Login aponta para a URL login do django
	path('login/', auth_views.login, name='login'),
	# Logout aponta para a URL logout do django
	# path('logout/', auth_views.logout, name='logout'), COMENTADA NA SECAO 4, VIDEO 24. 06:30
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
