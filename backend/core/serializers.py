from rest_framework import serializers
from core.models import Repo, Commit

class CommitSerializer(serializers.ModelSerializer):    
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'author': instance.author,
            'date': instance.date.strftime("%d/%m/%Y %H:%M:%S"),
            'repo': {"name": instance.repo.name, "id": instance.repo.id}
        }

    class Meta:
        model = Commit
        fields = '__all__'


class RepoSerializer(serializers.ModelSerializer):
    commits = CommitSerializer(many=True, read_only=True)

    def validate(self, data):
        if Repo.objects.filter(name=data['name'], owner=data['owner'], user=data['user']).exists():
            raise serializers.ValidationError("Este repositório ja foi adicionado")    
        return data

    class Meta:
        model = Repo
        fields = '__all__'