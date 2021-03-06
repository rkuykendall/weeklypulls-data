"""weeklypulls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from weeklypulls.apps.pulls import views as pull_views
from weeklypulls.apps.pull_lists import views as pull_list_views
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    url(r'^', include(pull_list_views.router.urls)),
    url(r'^', include(pull_views.router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', authtoken_views.obtain_auth_token),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
