"""shortlink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from links.views import BookViewSet
from main.views import *

router = SimpleRouter()
router.register(r'links', BookViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', main_page, name='home'),
                  path('register/', RegisterUser.as_view(), name='register'),
                  path('login/', AuthUser.as_view(), name='login'),
                  path('logout/', logout_user, name='logout'),
                  path('shorturl/', cut_url, name='shorturl'),
                  path('profile/', profile_page, name='profile'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls
