from django.contrib import admin
from django.urls import path, include

from short_link.views import UserSignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserSignupView.as_view(), name="signup"),
    path('short/', include('short_link.urls')),
]
