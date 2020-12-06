from rest_framework import serializers

from .models import Contest

import BoilerplateBackend.core.serializers

class ContestSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200)
    participants = BoilerplateBackend.core.serializers.CustomUserSerializer
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Contest
        fields = ['name', 'description', 'date_limit_participation',
                   'date_end', 'participants', 'owner' ]
    
    def create(self, validated_data):
        return Contest.objects.create(**validated_data)