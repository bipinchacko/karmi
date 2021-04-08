from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from .models import *
from django.db.models import Q
import json
from django.shortcuts import get_object_or_404


# Create your views here.
@login_required
def chatroom(request,pk:int):
    # othrer_user = get_object_or_404(CustomUser, pk=pk)
    # messages = Message.objects.filter(
    #     Q(receiver=request.user, sender=othrer_user)
    # )
    # messages.update(seen=True)
    # messages = messages | Message.objects.filter(Q(receiver=othrer_user, sender=request.user))
    # return render(request,"chat/chatroom.html",{"othrer_user":othrer_user,"messages":messages})
    other_user = get_object_or_404(CustomUser, pk=pk)
    messages = Message.objects.filter(
        Q(receiver=request.user, sender=other_user)
    )
    messages.update(seen=True)
    messages = messages | Message.objects.filter(Q(receiver=other_user, sender=request.user) )
    return render(request, "chat/chatroom.html", {"other_user": other_user, "messages": messages})
@login_required
def ajax_load_messages(request,pk):
    # othrer_user = get_object_or_404(CustomUser, pk=pk)
    # messages = Message.objects.filter(seen=False).filter(
    #     Q(receiver=request.user, sender=othrer_user)
    # )
    # messages.update(seen=True)
    # message_list = [{
    #     "sender":message.sender.first_name,
    #     "message":message.message,
    #     "sent":message.sender == request.user
    # } for message in messages]
    # messages.update(seen=True)
    # if request.method == "POST":
    #     message = json.loads(request.body)
    #     m = Message.objects.create(receiver=othrer_user, sender=request.user, message=message)
    #     message_list.append({
    #         "sender":request.user.first_name,
    #         "message":m.message,
    #         "sent":True
    #     })
    # return JsonResponse(message_list, safe=False)
    other_user = get_object_or_404(CustomUser, pk=pk)
    messages = Message.objects.filter(seen=False).filter(
        Q(receiver=request.user, sender=other_user)
    )
    message_list = [{
        "sender": message.sender.first_name,
        "message": message.message,
        "sent": message.sender == request.user
    } for message in messages]
    messages.update(seen=True)
    
    if request.method == "POST":
        message = json.loads(request.body)
        m = Message.objects.create(receiver=other_user, sender=request.user, message=message)
        message_list.append({
            "sender": request.user.first_name,
            "message": m.message,
            "sent": True,
        })
    print(message_list)
    return JsonResponse(message_list, safe=False)