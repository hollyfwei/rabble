from rest_framework import serializers
from rabble.models import *

class SubrabbleSerializer(serializers.ModelSerializer):
    visibility_status = serializers.SerializerMethodField()
    community_name = serializers.CharField(source='community.community_name', read_only=True)

    class Meta:
        model = Subrabble
        fields = ['subrabble_name', 'identifier', 'community_name', 'description', 
                  'users', 'visibility_status', 'anonymous_permissions']
        extra_kwargs = {
            'url': {'lookup_field': 'identifier'}
        }

    def get_visibility_status(self, obj):
        return obj.get_visibility_display()

class PostSerializer(serializers.ModelSerializer):
    subrabble_identifier= serializers.CharField(source='subrabble.identifier', read_only=True)
    author = serializers.CharField(source='user.username', read_only=True)
    user = serializers.SlugRelatedField(slug_field='username',queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'title', 'subrabble_identifier', 'author', 'body', 'user']
        read_only_fields = ['subrabble']

    def create(self, validated_data):
        subrabble = validated_data.pop('subrabble')
        return Post.objects.create(subrabble=subrabble, **validated_data)