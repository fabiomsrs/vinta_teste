from django.conf.urls import include, url, re_path  # noqa
from django.urls import path
from django.contrib import admin
from django.shortcuts import redirect
from django.views.generic import TemplateView

import django_js_reverse.views


urlpatterns = [    
    path("", lambda request : redirect("/login/")),
    path("", include("core.urls"), name="core"),
    path("admin/", admin.site.urls, name="admin"),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),
    path("login/", TemplateView.as_view(template_name='index.html')),
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')), 
]
