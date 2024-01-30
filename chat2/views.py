from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages


@login_required
def course_chat_room(request, group_id):
    user = request.user
    group_name = Group.objects.get(id=group_id)
    print(group_name.id)
    if user.groups.filter(name=group_name).exists():
        messages.success(request, "User Account Found")
    else:
        messages.success(request, "User Account not Found")
    
    return render(request, 'chat2/room.html', {'group_name': group_name})
