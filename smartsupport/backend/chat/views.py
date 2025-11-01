from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from services.openai_client import OpenAIClient
from django.conf import settings


class ChatView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def post(self, request):
    """Send a user message, save it, ask OpenAI, save AI reply."""
        user = request.user
        text = request.data.get('text')
        conversation_id = request.data.get('conversation_id')


        if not text:
            return Response({'detail': 'Message text is required.'}, status=status.HTTP_400_BAD_REQUEST)


        # get or create conversation
        if conversation_id:
            conv = get_object_or_404(Conversation, id=conversation_id, user=user)
        else:
            conv = Conversation.objects.create(user=user)


        # save user message
        user_msg = Message.objects.create(conversation=conv, sender='user', text=text, is_ai=False)


        # call OpenAI
        client = OpenAIClient(model=getattr(settings, 'OPENAI_MODEL', 'gpt-3.5-turbo'))
        try:
            prompt = f"You are a helpful support assistant. A user asks: {text}"
            ai_text = client.ask(prompt)
        except Exception as e:
        # if OpenAI fails, escalate
            conv.status = 'escalated'
            conv.save()
            return Response({'detail': 'AI unavailable, escalated to agent.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


        # save AI response
        ai_msg = Message.objects.create(conversation=conv, sender='ai', text=ai_text, is_ai=True)


        serializer = ConversationSerializer(conv, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ConversationListView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request):
        convs = Conversation.objects.filter(user=request.user).order_by('-created_at')
        serializer = ConversationSerializer(convs, many=True)
        return Response(serializer.data)