from django.urls import path
from .views import send_message, update_read_status

urlpatterns = [
    path('send-message/', send_message, name='send_message'),
    path('update-read-status/', update_read_status, name='update_read_status'),
]
