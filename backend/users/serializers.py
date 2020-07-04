
from rest_framework import serializers
from users.models import SocialUser
from django.middleware import csrf

class SocialUserSerializer(serializers.ModelSerializer):    
    extra_data = serializers.SerializerMethodField()
    
    def get_extra_data(self, obj):          
        extra_data = obj.extra_data
        extra_data['csrf'] = csrf.get_token(self.context.get('request'))
        return extra_data

    class Meta:
        model = SocialUser
        fields = '__all__'
    