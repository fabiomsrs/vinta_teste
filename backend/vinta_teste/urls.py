from django.conf.urls import include, url, re_path  # noqa
from django.urls import path
from django.contrib import admin
from django.shortcuts import redirect
from django.views.generic import TemplateView

import django_js_reverse.views


urlpatterns = [    
    path("", lambda request : redirect("/login/")),
    path("", include("core.urls"), name="core"),
    path("", include("users.urls"), name="core"),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),        
    path('oauth/', include('social_django.urls', namespace='social')),
    path("admin/", admin.site.urls, name="admin"),
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')), 
]
