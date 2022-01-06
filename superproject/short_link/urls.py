from django.urls import path

from short_link import views

app_name = "short"

urlpatterns = [
    path('', views.index, name="home"),
]