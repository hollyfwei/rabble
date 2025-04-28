from rest_framework import serializers
from rabble.models import *

class SubrabbleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subrabble
        fields = ['identifier, visibility', 'community', 'subrabble_name', 'description', 'anonymous_permissions', 'users']