from django.contrib.auth.views import LoginView, LogoutView
from core import views as core_views
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from core.views import home , settings , password
urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),  # <--
    path('settings/', settings, name='settings'),
    path('settings/password/', password, name='password'),
    path('admin', admin.site.urls),

]
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
