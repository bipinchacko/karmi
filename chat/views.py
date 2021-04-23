from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from .models import *
from django.db.models import Q
import json
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.http import HttpResponse


# Create your views here.
@login_required
def chatroom(request,pk:int):
    current_user = request.user.id
    other_user = get_object_or_404(CustomUser, pk=pk)
    messages = Message.objects.filter(
        Q(receiver=request.user, sender=other_user)
    )
    messages.update(seen=True)
    messages = messages | Message.objects.filter(Q(receiver=other_user, sender=request.user) )
    connecteduser = CustomUser.objects.all()
    context = {
        "other_user": other_user,
        "messages": messages,
        "current_user":current_user,
        "connecteduser":connecteduser
    }
    return render(request, "chat/onetoonechat.html",context)
@login_required
def ajax_load_messages(request,pk):
    message_list = []
    other_user = get_object_or_404(CustomUser, pk=pk)
    messages = Message.objects.filter(seen=False).filter(Q(receiver=request.user, sender=other_user))
    for message in messages:
        if message.files == '':
            message_list = [{
                "sender": message.sender.id,
                "message": message.message,
                "sent": message.sender == request.user,
                "file": ''
                
            } ]
        else:
            message_list = [{
                "sender": message.sender.id,
                "message": message.message,
                "sent": message.sender == request.user,
                "file":message.files.url
            } ]
        print(message_list)
        messages.update(seen=True)
    if request.method == "POST":
        a = request.POST.get('message')
        b = request.FILES.get('upload')
        if a == '' and b == None:
            print("null")
        else:
            m = Message.objects.create(receiver=other_user, sender=request.user, message=a, files=b)
            if m.files == None:
                message_list.append({
                    "sender": request.user.id,
                    "message": m.message,
                    "sent": True,
                    "file":''
                })
            else:
                message_list.append({
                    "sender": request.user.id,
                    "message": m.message,
                    "sent": True,
                    "file":m.files.url
                })
    return JsonResponse(message_list, safe=False)
def messageDelete(request):
    a = request.POST.get('id')
    d = Message.objects.get(pk=a)
    d.delete()
    return HttpResponse('')
# @login_required
# def switchUser(request):
#     print("hloooo")
#     current_user = request.user
#     connecteduser = CustomUser.objects.all()
#     last_seen = cache.get('seen_%s' % connecteduser)
#     print(last_seen)
#     return HttpResponse('')
# Group chat.
def createGroup(request):
    if request.method == "POST":
        group = Group()
        group.name = request.POST.get('groupname')
        group.icon = request.FILES.get('groupicon')
        group.save()
        groupmembers = GroupMembers()
        c = request.POST.get('members')
        arr = c.split(',')
        for i in arr:
            groupmembers.group = group
            d = int(i)
            groupmembers.member = d
            groupmembers.admin = "member"
            groupmembers.save()
        groupmembers.group = group
        groupmembers.member = request.user.id
        groupmembers.admin = "Admin"
        groupmembers.save()
    return HttpResponse('')
@login_required
def groupchatroom(request,pk:int):
    current_user = request.user.id
    other_user = get_object_or_404(CustomUser, pk=pk)
    messages = Message.objects.filter(
        Q(receiver=request.user, sender=other_user)
    )
    messages.update(seen=True)
    messages = messages | Message.objects.filter(Q(receiver=other_user, sender=request.user) )
    connecteduser = CustomUser.objects.all()
    context = {
        "other_user": other_user,
        "messages": messages,
        "current_user":current_user,
        "connecteduser":connecteduser
    }
    return render(request, "chat/groupchat.html",context)
def groupchatroom_base(request):
    connecteduser = CustomUser.objects.all()
    context = {
        "connecteduser":connecteduser
    }
    return render(request, "chat/groupchatbase.html",context)    
@login_required
def ajax_load_messages_group(request,pk):
    message_list = []
    other_user = get_object_or_404(CustomUser, pk=pk)
    messages = Message.objects.filter(seen=False).filter(Q(receiver=request.user, sender=other_user))
    for message in messages:
        if message.files == '':
            message_list = [{
                "sender": message.sender.id,
                "message": message.message,
                "sent": message.sender == request.user,
                "file": ''
                
            } ]
        else:
            message_list = [{
                "sender": message.sender.id,
                "message": message.message,
                "sent": message.sender == request.user,
                "file":message.files.url
            } ]
        print(message_list)
        messages.update(seen=True)
    if request.method == "POST":
        a = request.POST.get('message')
        b = request.FILES.get('upload')
        if a == '' and b == None:
            print("null")
        else:
            m = Message.objects.create(receiver=other_user, sender=request.user, message=a, files=b)
            if m.files == None:
                message_list.append({
                    "sender": request.user.id,
                    "message": m.message,
                    "sent": True,
                    "file":''
                })
            else:
                message_list.append({
                    "sender": request.user.id,
                    "message": m.message,
                    "sent": True,
                    "file":m.files.url
                })
    return JsonResponse(message_list, safe=False)
def messageDelete_group(request):
    a = request.POST.get('id')
    d = Message.objects.get(pk=a)
    d.delete()
    return HttpResponse('')