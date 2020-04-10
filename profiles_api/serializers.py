from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializers  a namefield for testing our API View"""
    name = serializers.CharField(max_length=10)