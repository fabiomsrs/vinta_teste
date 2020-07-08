from core.models import Repo, Commit
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework_extensions.mixins import NestedViewSetMixin
from core.serializers import RepoSerializer, CommitSerializer
from core.paginations import CustomPagination
from .tasks import create_commits, create_web_hook
import json
import requests
import datetime


class RepoViewSet(NestedViewSetMixin, viewsets.ModelViewSet): 
    queryset = Repo.objects.all()
    serializer_class = RepoSerializer    
    pagination_class = CustomPagination    

    def list(self, request):
        queryset = Repo.objects.filter(user=self.request.user.social.extra_data.get("login"))
        serializer = RepoSerializer(queryset, many=True)        
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):        
        data = request.data                
        repo = {}        
        repo['name'] = data.get('name')
        repo['owner'] = data.get('owner').get('login')
        repo['date'] = data.get('created_at')  
        repo['user'] = request.user.social.extra_data.get("login")
            
        serializer = self.get_serializer(data=repo)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        create_commits(request, serializer.data)
        create_web_hook(request, serializer.data) #only in production

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(methods=['post'], detail=True, permission_classes=[AllowAny])
    def update_commits(self, request, pk=None):        
        data = request.data
        repo = self.get_object()
        print(repo)
        commits = []        
        for commit in data.get('commits'):            
            commits.append(
                Commit(author=commit.get('author').get('name'), 
                url=commit.get('url'), 
                repo=repo,
                date=data.get('head_commit').get('timestamp'))            
            )
        Commit.objects.bulk_create(commits)
        return Response({'status': 'commits successful updated'})


class CommitViewSet(NestedViewSetMixin, viewsets.ModelViewSet):    
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['repo__user',]