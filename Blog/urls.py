
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token#alternative token gen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_blog.urls')),
    path('auth/',obtain_auth_token),#for token gen
]
