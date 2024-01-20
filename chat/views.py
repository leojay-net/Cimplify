from rest_framework.response import Response
from rest_framework import status
from .chat import get_response
from .langchain_gemini import geminiChat
from .gemini import geminiConversation
from .serializers import ChatSerializer, GeminiConversationSerializer, GeminiChatSerializer
from rest_framework.generics import GenericAPIView
from pypdf import PdfReader
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser
import requests
from io import BytesIO

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
            print(type(serializer.data['history']))
            result = geminiConversation(problem=serializer.data['problem'], history=serializer.data['history'])
            response = serializer.data
            response["response"] = result
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GeminiChat(GenericAPIView):
    serializer_class = GeminiChatSerializer
    #parser_classes = (MultiPartParser, FileUploadParser, FormParser)

    def read_pdf(self, url):
        response = requests.get(url)
        bytes_stream = BytesIO(response.content)
        pdf_loader = PdfReader(bytes_stream)
        context = "\n\n".join(str(p.extract_text()) for p in pdf_loader.pages)
        return context
        # pdf = request.FILES.get("pdf_file")
        # pdf_loader = PdfReader(pdf)
        # # pages = pdf_loader.load_and_split()
        # context = "\n\n".join(str(p.extract_text()) for p in pdf_loader.pages)
        # return context

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            context = self.read_pdf(url=str(serializer.data['pdf_url']))
            result = geminiChat(problem=serializer.data['problem'], context=context)
            response = serializer.data
            response["response"] = result
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
