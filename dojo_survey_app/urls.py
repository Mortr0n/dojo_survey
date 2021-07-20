from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('session_items', views.session_items),
    path('results', views.results),
]