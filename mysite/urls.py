"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import include
#import django_saml2_auth.views

urlpatterns = [
    # These are the SAML2 related URLs. You can change "^saml2_auth/" regex to
    # any path you want, like "^sso_auth/", "^sso_login/", etc. (required)
    #re_path(r'^saml2_auth/', include('django_saml2_auth.urls')),

    # The following line will replace the default user login with SAML2 (optional)
    # If you want to specific the after-login-redirect-URL, use parameter "?next=/the/path/you/want"
    # with this view.
    #re_path(r'^accounts/login/$', django_saml2_auth.views.signin),

    # The following line will replace the admin login with SAML2 (optional)
    # If you want to specific the after-login-redirect-URL, use parameter "?next=/the/path/you/want"
    # with this view.
    #re_path(r'^admin/login/$', django_saml2_auth.views.signin),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('todolist.urls'))
]
