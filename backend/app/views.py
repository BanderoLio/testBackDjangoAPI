# Create your views here.
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer


class MessageList(generics.ListAPIView):
    # Используем ListAPIView для получения списка
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
