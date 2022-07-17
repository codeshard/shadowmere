from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import proxylist.views
from proxylist import views

router = routers.DefaultRouter()
router.register(r"proxies", views.ProxyViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", proxylist.views.list_proxies),
    path("<int:proxy_id>/config", proxylist.views.json_proxy_file),
    path("<int:proxy_id>/qr", proxylist.views.qr_code),
    path("health", proxylist.views.healthcheck),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/", include(router.urls)),
    path("api/country-codes", views.country_code_list),
    path("", include("django_prometheus.urls")),
]
