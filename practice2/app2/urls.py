from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]

# from django.urls import path
# from .views import index

# urlpatterns = [
#     path('', index, name='index'),
# ]