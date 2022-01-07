from django.urls import path

from short_link.views import UserLinksView, LinkView

app_name = "short"


def index(request):
    from django.http import HttpResponse
    return HttpResponse("Hello, world. You're at the polls index.")


urlpatterns = [
    path('', index, name="home"),
    path('list_links/', UserLinksView.as_view(), name="list"),
    path('<int:pk>', LinkView.as_view(), name="link"),
]