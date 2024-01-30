from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    receiver_id = request.data.get('receiver_id')
    content = request.data.get('content')

    # Handle sending message to receiver_id using Channels
    # For simplicity, you can use Django signals or other methods

    return Response({'message': 'Message sent successfully'})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_read_status(request):
    message_id = request.data.get('message_id')

    # Handle updating read status for the given message_id
    # You may want to store read status in your database

    return Response({'message': 'Read status updated successfully'})

