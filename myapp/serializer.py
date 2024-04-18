from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        
class SnippetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "__all__"  

class SnippetDetailsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Snippet
        fields = "__all__"  
