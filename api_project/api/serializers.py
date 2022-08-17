from rest_framework import serializers

class PlateNumberSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=200, required=True)
