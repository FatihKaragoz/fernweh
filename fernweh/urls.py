"""fernweh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from fernweh import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.homeview, name="home"),
    url(r'^browse/', views.browseview, name="browse"),
    url(r'^aboutus/', views.aboutview, name="about"),
    url(r'^contact/', views.contactview, name="contact"),
    url(r'^login/', views.loginview, name="login"),
    url(r'^signup/', views.signupview, name="signup"),
    # url(r'^loginfunc/', views.loginfunc, name="loginfunc"),
    url(r'^signupfunc/', views.signupfunc, name="signupfunc"),
    url(r'^logout/', views.logoutfunc, name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
