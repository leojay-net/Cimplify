from rest_framework import serializers
from django.core.validators import FileExtensionValidator



class ChatSerializer(serializers.Serializer):
    problem = serializers.CharField(max_length=300)
    aoc = serializers.CharField(max_length=300, required=False, allow_blank=True)


class ChatObjectSerializer(serializers.Serializer):
    role = serializers.CharField()
    parts = serializers.ListField()

class GeminiConversationSerializer(serializers.Serializer):
    problem = serializers.CharField(max_length=300)
    history = serializers.ListField(child=ChatObjectSerializer())



class GeminiChatSerializer(serializers.Serializer):
    problem = serializers.CharField(max_length=300)
    pdf_file = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])], write_only=True)
    