from django.conf import settings
from django.contrib import admin
from django.urls import path ,include
from .views import home
from .api.views import ApiStart
from users.views import (
    login,
    logout,
    register,
    dashbord
)

urlpatterns = [
    path('' , home , name="home"),
    path('' , dashbord , name="dashbord"),
    # ## Auth
    path('login/' , login , name="login"),
    path('logout/' , logout , name="logout"),
    path('signup/' , register, name="signup"),
    
    
    ## Admin
    path('admin/', admin.site.urls),
    
    # Custom urls
    path('users/',include('users.urls')),
    path('owners/',include('owners.urls')),
    path('pets/',include('pets.urls')),
    
    # Api
    path('api/',ApiStart.as_view() , name="api"),
    path('api/',include('users.api.urls')),
    path('api/',include('pets.api.urls')),
    
]


