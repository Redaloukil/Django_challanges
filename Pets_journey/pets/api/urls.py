from django.urls import path 
from .views import DogsView , CatsView

urlpatterns = [
    path('dogs/',  DogsView.as_view()),
    path('cats/' , CatsView.as_view()),
]
