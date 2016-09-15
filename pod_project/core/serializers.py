# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from core.models import UserProfile
from pods.models import Pod, Type
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('title','description')

class PodSerializer(serializers.HyperlinkedModelSerializer):
    #type = serializers.HyperlinkedIdentityField(view_name="pods:type")
    #type = TypeSerializer()
    class Meta:
        model = Pod
        fields = ('video', 'title', 'owner', 'type')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'description', 'url', 'auth_type', 'affiliation', 'commentaire') #'image',

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
        
