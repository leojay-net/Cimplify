from django.urls import path
from .views import Chat, GeminiConversation, GeminiChat


urlpatterns = [
    path('ai/tutor', Chat.as_view(), name="tutor-student"),
    path('Gemini/ai/conversation', GeminiConversation.as_view(), name="geminiconv"),
    path('Gemini/ai/chat', GeminiChat.as_view(), name="geminichat")
]