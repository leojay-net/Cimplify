from django.urls import path
from .views import Chat, GeminiConversation


urlpatterns = [
    path('ai/tutor', Chat.as_view(), name="tutor-student"),
    path('Gemini/ai/conversation', GeminiConversation.as_view(), name="geminiconv")
]