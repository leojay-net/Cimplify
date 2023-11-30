from django.urls import path
from .views import Chat


urlpatterns = [
    path('ai/tutor', Chat.as_view(), name="tutor-student"),
]