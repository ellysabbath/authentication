from rest_framework import serializers
from .models import Member,DeaconInfo

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'  # Include all the model fields


class DeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeaconInfo
        fields = '__all__'        