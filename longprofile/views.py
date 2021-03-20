from django.shortcuts import render, get_object_or_404
from longprofile.forms import *
from longprofile.models import *
from byhand.models import *
import json
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from django.urls import reverse
from longprofile.urls import url
from django.urls import resolve
import datetime as dt
from datetime import datetime
import datetime


# Create your views here.
def home(request):
    return render(request,'longprofile/home.html')
def cards(request):
    return render(request,'longprofile/cards.html')
def company_card_update(request):
    current_user = request.user
    if Company_card.objects.filter(user_id = current_user.id):
        view = Company_card.objects.get(user_id = current_user.id)
        form = Company_cardForm(instance=view)
        if request.method == "POST":
            form = Company_cardForm(request.POST, instance=view)
            if form.is_valid():
                form.save()
    else:  
        form = Company_cardForm()
        if request.method == "POST":
            form = Company_cardForm(request.POST, request.FILES)
            if form.is_valid():
                card = form.save(commit=False)
                card.user_id = current_user.id
                card.save()
    context = {
        "form":form,
    }
    return render(request,'longprofile/company_card_update.html',context)
def personal_card_update(request):
    current_user = request.user
    if Personal_card.objects.filter(user_id = current_user.id):
        view = Personal_card.objects.get(user_id = current_user.id)
        form = Personal_cardForm(instance=view)
        if request.method == "POST":
            form = Personal_cardForm(request.POST, instance=view)
            if form.is_valid():
                form.save()
    else:  
        form = Personal_cardForm()
        if request.method == "POST":
            form = Personal_cardForm(request.POST, request.FILES)
            if form.is_valid():
                card = form.save(commit=False)
                card.user_id = current_user.id
                card.save()
    context = {
        "form":form,
    }
    return render(request,'longprofile/personal_card_update.html',context)
def autosuggest(request):
    query_original = request.GET.get('term')
    queryset = CustomUser.objects.filter(first_name__icontains = query_original)
    mylist = []
    mylist += [x.first_name for x in queryset]
    return JsonResponse(mylist,safe = False)
def manualsearch(request):
    if request.method == 'GET':
        search = request.GET.get('tags')
        searching = CustomUser.objects.filter(Q(first_name__icontains = search) | Q(username__icontains=search) | Q(email__icontains=search))
        a = (len(searching))
        if a<= 0:
            return HttpResponse("We couldn't find a match for " + search)
    context = {
        'searching':searching,
    }
    return render(request,'longprofile/search.html',context)
def searchprofile_full_view(request, pk):
    request.session['othreuser'] = pk
    instance = get_object_or_404(CustomUser, pk=pk)
    is_following = Follow2.objects.filter(following_id = request.user.id, follower_id = pk)
    endorse = Endorse.objects.filter(user_id = request.user.id, liked_person_id = pk)
    if Connection.objects.filter(user_id = request.user.id, connected_person_id = pk, connection = 0):
        is_connection = "requested"
    elif Connection.objects.filter(user_id = request.user.id, connected_person_id = pk, connection = 1):
        is_connection = "connected"
    else:
        is_connection = "notConnected"
    following_count = Follow2.objects.filter(following_id = request.user.id).count()
    follower_count = Follow2.objects.filter(follower_id = request.user.id).count()
    #star rating view
    try:
        rating_view = Rating.objects.filter(rated_person = pk).aggregate(Sum('rating'))
        rating_count = Rating.objects.filter(rated_person = pk).count()
        e = (rating_view['rating__sum'])
        rating = e/rating_count
    except:
        rating = 0
    context = {
        'instance':instance,
        'connection':is_following,
        'endorse':endorse,
        'following_count':following_count,
        'rating':rating,
        'follower_count':follower_count,
        'is_connection':is_connection
    }
    return render(request,'longprofile/searchpofile_full_view.html',context)
def profile_full_view(request):
    return render(request,'longprofile/profile_full_view.html')
def countAndNotifications(request,pk):
    pk = request.session['othreuser']
    follower_count = Follow2.objects.filter(follower_id = request.user.id).count()
    if Connection.objects.filter(user_id = request.user.id, connected_person_id = pk, connection = 0):
        is_connection = "Requested"
    elif Connection.objects.filter(user_id = request.user.id, connected_person_id = pk, connection = 1):
        is_connection = "Connected"
    else:
        is_connection = "Connect+"
    pendingRequest = Connection.objects.filter(connected_person_id = request.user.id, connection = 0)
    html = ""
    for i in pendingRequest:
        print(i.pk)
        print(i.user.first_name)
        html="""
        <div>
            <p style="display: inline-block;">%s</p>
            <a type="button" class="btn btn-success" id="connections_accept" role="button" href="/longprofile/connectionAccept/%s">Accept</a>
            <a type="button" class="btn btn-danger" id="connections_remove" role="button" href="/longprofile/connectionDelete/%s">Remove</a>
        </div>
        """
        # current_url = resolve(request.path_info)
        html = html % (i.user.first_name,i.pk,i.pk)
    resp = {
        "follower_count":follower_count,
        'is_connection':is_connection,
        "data":html
        
    }
    data = json.dumps(resp)
    return HttpResponse(data,content_type = "application/json")
def home2(request):
    
    return render(request,'longprofile/home2.html')
@csrf_exempt
def starRating(request):
    current_user = request.user
    othreuser = request.session['othreuser']
    if Rating.objects.filter(user_id = current_user.id, rated_person = othreuser):
        view = Rating.objects.get(user_id = current_user.id, rated_person = othreuser)
        if request.method == "POST":
            view.user_id = current_user.id
            view.rated_person = othreuser
            r = request.POST['rating']
            view.rating = float(r)
            view.save()
    else:
        if request.method == "POST":
            data = Rating()
            data.user_id = current_user.id
            data.rated_person = othreuser
            r = request.POST['rating']
            data.rating = float(r)
            data.save()
    return HttpResponse("rating is not working.we are working to fix it")
def follow(request, pk):
    main_user = request.user.id
    othreuser = pk
    #check if already following
    if Follow2.objects.filter(following_id = main_user, follower_id = othreuser):
        unfollow = Follow2.objects.get(following_id = main_user, follower_id = othreuser)
        unfollow.delete()
        is_following = False
        following_count = Follow2.objects.filter(following_id = main_user).count()
    else:
        foll2 = Follow2()
        foll2.follower_id=othreuser
        foll2.following_id = main_user
        foll2.save()
        is_following = True
        following_count = Follow2.objects.filter(following_id = main_user).count()
    resp = {
        "following":is_following,
        "following_count":following_count
    }
    response = json.dumps(resp)
    return HttpResponse(response,content_type="application/json")
def endorse(request,pk):
    main_user = request.user.id
    othreuser = pk
    if Endorse.objects.filter(user_id = main_user, liked_person_id = othreuser):
        unendorse = Endorse.objects.get(user_id = main_user, liked_person_id = othreuser)
        unendorse.delete()
        is_endorsing = False
    else:
        endorse = Endorse()
        endorse.user_id = main_user
        endorse.liked_person_id = othreuser
        endorse.save()
        is_endorsing = True
    resp = {
        "endorsing":is_endorsing,
    }
    response = json.dumps(resp)
    return HttpResponse(response,content_type="application/json")
def connection(request,pk):
    main_user = request.user.id
    othreuser = pk
    if Connection.objects.filter(user_id = main_user, connected_person_id = othreuser):
        disconnect = Connection.objects.get(user_id = main_user, connected_person_id = othreuser)
        disconnect.delete()
        is_connection = "notConnected"
    elif Connection.objects.filter(user_id = main_user, connected_person_id = othreuser, connection = 0):
        is_connection = "requested"
    elif Connection.objects.filter(user_id = main_user, connected_person_id = othreuser, connection = 1):
        is_connection = "connected"
    else:
        conn = Connection()
        conn.user_id = main_user
        conn.connected_person_id = othreuser
        conn.save()
        is_connection = "requested"
    resp = {
        "isconnection":is_connection,
    }
    response = json.dumps(resp)
    return HttpResponse(response,content_type="application/json")
def connectionList(request,pk):
    instance = get_object_or_404(CustomUser, pk=pk)
    pendingRequest = Connection.objects.filter(connected_person_id = request.user.id, connection = 0)
    myConnections = Connection.objects.filter(Q(user_id = pk) | Q(connected_person_id = pk, connection = 1))
    context = {
        'instance':instance,
        'pendingRequest':pendingRequest,
        'myConnections':myConnections
    }
    return render(request,"longprofile/connectionlist.html",context)
def connectionDelete(request,pk):
    othreuser = request.session['othreuser']
    d = Connection.objects.get(pk=pk)
    d.delete()
    return HttpResponseRedirect(reverse("connectionList",kwargs={'pk':othreuser}))
def connectionAccept(request,pk):
    othreuser = request.session['othreuser']
    view=Connection.objects.get(pk=pk)
    view.connection = 1
    view.save()
    return HttpResponseRedirect(reverse("connectionList",kwargs={'pk':othreuser}))
#event
def event(request):
    current_user = request.user
    form = CreateEventForm()
    if request.method == "POST":
        form = CreateEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user_id = current_user.id
            event.save()
            return HttpResponseRedirect(reverse("event"))
    my_event = CreateEvent.objects.filter(user_id = current_user.id)
    context = {
        "form":form,
        "my_event":my_event,
    }
    return render(request,'longprofile/event.html',context)
def eventOtheruser(request,pk):
    current_user = request.user
    my_event = CreateEvent.objects.filter(user_id = pk)
    saved_event = [i for i in my_event if SavedEvent.objects.filter(savedperson_id = current_user.id,event_id = i)]
    savedEventView = SavedEvent.objects.filter(savedperson_id = current_user.id)
    context = {
        "my_event":my_event,
        "saved_event":saved_event,
        "savedEventView":savedEventView
    }
    return render(request,'longprofile/eventOtheruser.html',context)
def eventSave(request,pk):
    main_user = request.user
    events = int(pk)
    if SavedEvent.objects.filter(event_id = events,savedperson_id = main_user.id):
        unsave = SavedEvent.objects.get(event_id = events,savedperson_id = main_user.id)
        unsave.delete()
        is_save = False
    else:
        saving = SavedEvent()
        saving.event_id = pk
        saving.savedperson_id = main_user.id
        saving.save()
        is_save = True
    resp = {
        "is_save":is_save,
        "save_id":pk
    }
    response = json.dumps(resp)
    return HttpResponse(response,content_type="application/json")
#enquiry
def createEnquiry(request,pk):
    current_user = request.user
    other_user = int(pk)
    form = CreateEnquiryForm()
    if current_user.id != other_user:
        if request.method == "POST":
            form = CreateEnquiryForm(request.POST)
            if form.is_valid():
                enquiry = form.save(commit=False)
                enquiry.user_id = current_user.id
                enquiry.enquired_person_id = other_user
                enquiry.save()
                return HttpResponseRedirect(reverse("createEnquiry",kwargs={'pk':other_user}))
    context = {
        "form":form,
    }
    return render(request,'longprofile/enquiry.html',context)
def myenquiry(request):
    current_user = request.user
    enquiries = CreateEnquiry.objects.filter(enquired_person_id = current_user.id)
    myenquies = CreateEnquiry.objects.filter(user_id = current_user.id)
    savedenquiries = [i for i in enquiries if SavedEnquiry.objects.filter(savedperson_id = current_user.id,enquiry_id = i)]
    savedEnquiryView = SavedEnquiry.objects.filter(savedperson_id = current_user.id)
    context = {
        "enquiries":enquiries,
        "myenquies":myenquies,
        "savedenquiries":savedenquiries,
        "savedEnquiryView":savedEnquiryView
    }
    return render(request,'longprofile/myenquiry.html',context)
def enquirySave(request,pk):
    main_user = request.user
    enquiry = int(pk)
    if SavedEnquiry.objects.filter(enquiry_id = enquiry,savedperson_id = main_user.id):
        unsave = SavedEnquiry.objects.get(enquiry_id = enquiry,savedperson_id = main_user.id)
        unsave.delete()
        is_save = False
    else:
        saving = SavedEnquiry()
        saving.enquiry_id = pk
        saving.savedperson_id = main_user.id
        saving.save()
        is_save = True
    resp = {
        "is_save":is_save,
        "save_id":pk
    }
    response = json.dumps(resp)
    return HttpResponse(response,content_type="application/json")
#appoinment
def createAppoinment(request,pk):
    current_user = request.user
    other_user = int(pk)
    form = CreateAppoinmentForm()
    if current_user.id != other_user:
        if request.method == "POST":
            appoinment = CreateAppoinment2()
            appoinment.name = request.POST['name']
            appoinment.purpose = request.POST['purpose']
            appoinment.description = request.POST['description']
            a =request.POST['date']
            b = request.POST['time']
            bb = b.replace(":","")
            new_date = datetime.datetime.strptime(a, '%Y-%m-%d')
            mytime = dt.datetime.strptime(bb,'%H%M').time()
            c = dt.datetime.combine(new_date, mytime)
            appoinment.dateandtime = c
            appoinment.user_id = current_user.id
            appoinment.enquired_person_id = other_user
            appoinment.save()
            return HttpResponseRedirect(reverse("createAppoinment",kwargs={'pk':other_user}))
    context = {
        "form":form,
    }
    return render(request,'longprofile/appoinment.html',context)
def myappoinment(request):
    date = datetime.datetime.now()
    # current_time = date.strftime("%X")
    # current_date = date.strftime("%Y-%m-%d")
    pending = CreateAppoinment2.objects.filter(dateandtime__gte = date)
    print(pending)
    return render(request,'longprofile/myappoinment.html')