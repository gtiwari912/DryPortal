from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='home page'),
    path('login', views.index, name='home page'),
    path('form', views.form),
    path('upload', views.upload),
    path('signup', views.signup)
]
