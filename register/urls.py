from django.urls import include, path
from . import views

app_name = "register"
urlpatterns = [
    path('sign_up/', views.register, name='regis'),
]
