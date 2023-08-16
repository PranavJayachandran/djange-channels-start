from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("chat/", include("appname.url")),
    path("admin/", admin.site.urls),
]