from rest_framework.response import Response
from rest_framework import status
from .chat import get_response
from .gemini import geminiConversation
from .serializers import ChatSerializer, GeminiConversationSerializer
from rest_framework.generics import GenericAPIView


class Chat(GenericAPIView):
    serializer_class = ChatSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            result = get_response(problem=serializer.data['problem'], aoc=serializer.data['aoc'])
            response = serializer.data
            response["response"] = str(result)
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GeminiConversation(GenericAPIView):
    serializer_class = GeminiConversationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            result = geminiConversation(problem=serializer.data['problem'])
            response = serializer.data
            response["response"] = str(result)
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    