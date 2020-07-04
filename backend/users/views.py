from rest_framework.response import Response
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
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('core:home'))
    return render(request, 'index.html')