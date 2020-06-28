from django.urls import path
from django.views.generic import TemplateView
from rest_framework_extensions.routers import ExtendedSimpleRouter
from . import views

app_name = 'core'

router = ExtendedSimpleRouter()
(
router.register(r'repos', views.RepoViewSet, basename='repos')
    .register(r'commits', views.CommitViewSet, basename='repo_commits',parents_query_lookups=['repo']),

router.register(r'commits', views.CommitViewSet, basename='commits')
)


urlpatterns = [
    path("home/", TemplateView.as_view(template_name='index.html')),
    path("commit/", TemplateView.as_view(template_name='index.html')),
    path("repo/<int:pk>/commit/", TemplateView.as_view(template_name='index.html')),
]

urlpatterns += router.urls