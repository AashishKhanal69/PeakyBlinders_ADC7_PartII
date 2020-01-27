"""connect_project URL Configuration

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
from django.urls import path, include
from Connect.views import Login
from Connect.views import adminLogout
from Connect.views import userLogin
from Connect.views import userLogout


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('',include('Connect.urls'))
]

urlpatterns += [
    # path('accounts/',include('django.contrib.auth.urls')),
    path('', Login),
    path('logout/',adminLogout),
    path('userlog',userLogin),
    path('userlogout',userLogout)
]