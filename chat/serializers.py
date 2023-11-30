from rest_framework import serializers



class ChatSerializer(serializers.Serializer):
    problem = serializers.CharField(max_length=300)
    aoc = serializers.CharField(max_length=300)
    