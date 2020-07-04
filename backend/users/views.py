from rest_framework.response import Response
from django.contrib.auth import logout
from django.shortcuts import render 
from rest_framework import viewsets
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from users.models import SocialUser
from users.serializers import SocialUserSerializer

# Create your views here.

class SocialUserViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        try:
            user = request.user.social        
            serializer = SocialUserSerializer(user, context={'request': request})
            return Response(serializer.data)
        except:
            return Response({
                'ok': False,
            }, status=401)
    

def login(request):
    try:                   
        request.user.social
        return HttpResponseRedirect(reverse_lazy('core:home'))
    except:
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse_lazy('admin:index'))    
    return render(request, 'index.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse_lazy('users:login'))