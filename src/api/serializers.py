from rest_framework import serializers
from rabble.models import *

class SubrabbleSerializer(serializers.ModelSerializer):
    identifier_str = serializers.CharField(source='identifier', read_only=True)
    visibility_str = serializers.SerializerMethodField()
    community_str = serializers.CharField(source='community.community_name', read_only=True)
    subrabble_str = serializers.CharField(source='subrabble_name', read_only=True)
    description_str = serializers.CharField(source='description', read_only=True)
    anonymous_permissions_str = serializers.BooleanField(source='anonymous_permissions', read_only=True)
    users_str = serializers.StringRelatedField(source='users', many=True, read_only=True)

    class Meta:
        model = Subrabble
        fields = ['identifier', 'visibility', 'community', 'subrabble_name', 
                  'description', 'anonymous_permissions', 'users', 'identifier_str',
                  'visibility_str', 'community_str', 'subrabble_str', 
                  'description_str', 'anonymous_permissions_str', 'users_str']
        extra_kwargs = {
            'url': {'lookup_field': 'identifier'}
        }

    def get_visibility_str(self, obj):
        return obj.get_visibility_display()

class PostSerializer(serializers.ModelSerializer):
    subrabble_identifier_str = serializers.CharField(source='subrabble.identifier', read_only=True)
    subrabble_str = serializers.CharField(source='subrabble.subrabble_name', read_only=True)
    title_str = serializers.CharField(source='title', read_only=True)
    body_str = serializers.CharField(source='body', read_only=True)
    anonymity_str = serializers.BooleanField(source='anonymity', read_only=True)

    class Meta:
        model = Post
        fields = ['subrabble_identifier', 'subrabble', 'user', 'title', 'body', 'anonymity',
                  'identifier_str', 'subrabble_str', 'title_str', 'body_str', 
                  'anonymity_str']
