from django.urls import path

from short_link.views import CreateShortLinkView, LinkView, UserLinksView

app_name = "short"


urlpatterns = [
    path("", CreateShortLinkView.as_view(), name="home"),
    path("list_links/", UserLinksView.as_view(), name="list"),
    path("<int:pk>", LinkView.as_view(), name="link"),
]
