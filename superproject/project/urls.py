from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from short_link.views import UserSignupView, UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserSignupView.as_view(), name="signup"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('short/', include('short_link.urls')),
]
