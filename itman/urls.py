"""itman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from djangosaml2 import views as djangosaml2_views

# LOGOUT_VIEW = import_string(settings.LOGOUT_VIEW)

if getattr(settings, 'ENABLE_SAML2_LOGIN', False):
    actual_logout = djangosaml2_views.logout
else:
    actual_logout = LogoutView.as_view()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("calllogger.urls")),
    (r'^saml2/', include('djangosaml2.urls')),
    path(r'admin/logout', actual_logout, name='custom_logout'),
    # path('calllogger/', include("calllogger.urls")) `${}`
]
