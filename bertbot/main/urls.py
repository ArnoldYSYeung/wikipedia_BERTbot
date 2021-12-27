from django.urls import path

import main.views as views

urlpatterns = [
    #   default path
    path('', views.index, name='index'),
    #   history path
    path('history', views.history)
]