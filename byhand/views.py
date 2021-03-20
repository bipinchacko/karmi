from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from byhand.models import CustomUser

from byhand.models import UserExtend
from django.views.decorators.csrf import csrf_exempt

from byhand.models import Follow


def register(request):
    Email = request.POST.get('email')
    Username = request.POST.get('phone')
    Password = request.POST.get('password1')
    #password = make_password(Password)
    if request.method == "POST":
        user = CustomUser()
        user.email = Email
        user.username = Username
        user.set_password(Password)
        user.is_active = True
        user.save()
        login(request,user)
        return redirect('register_as')
    return render(request,'registration/registration-byhand.html')

@csrf_exempt
def check_email_exist(request):
    email = request.POST.get('email')
    user_obj = CustomUser.objects.filter(email = email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_phone_exist(request):
    phone = request.POST.get('phone')
    user_obj = CustomUser.objects.filter(username = phone).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def dashboard(request):
    return render(request,'dashboard.html')
def loginpage(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')


        # user = authenticate(request, email=username, password=password)
        try:
            user = CustomUser.objects.get(username = username)

            if user.check_password(password):

                print('username')
                login(request,user)
                print(user)
                return redirect('dashboard')


        except CustomUser.DoesNotExist:
            messages.info(request, 'Username OR Password is incorrect')
            try:
                user = CustomUser.objects.get(email=username)
                if user.check_password(password):
                    login(request,user)
                    return redirect('dashboard')


            except:

                messages.info(request, 'Username OR Password is incorrect')
                # return redirect('dashboard')







        # if user is not None:
        #
        #
        #     login(request, user)
        #     return redirect('dashboard')
        # else:
        #     messages.info(request, 'None user')



    return render(request,'registration/byhand-login.html')



def register_as(request):
    return render(request,'registration/registration-as.html')
def register_company(request):
    view = CustomUser.objects.get(id=request.user.id)
    if request.method == "POST":
        Company = request.POST.get('cname')
        Createdby = request.POST.get('createdby')
        Position = request.POST.get('position')
        Email = request.POST.get('email')
        Mobile = request.POST.get('phone')
        view.email= Email
        view.username = Mobile
        view.save()
        userextend = UserExtend()
        userextend.company_name = Company
        userextend.created_by = Createdby
        userextend.position = Position
        userextend.user_id = request.user.id
        userextend.save()
        return HttpResponse('sucess')


    context = {
        'view': view
    }
    return render(request,'registration/registration-company.html',context)
def register_freelancer(request):
    view = CustomUser.objects.get(id= request.user.id)


    if request.method == "POST":

        First_Name = request.POST.get('first_name')
        Last_Name = request.POST.get('last_name')
        Email = request.POST.get('email')
        Mobile = request.POST.get('phone')
        Profession = request.POST.get('profession')
        view.first_name = First_Name
        view.last_name = Last_Name
        view.email = Email
        view.username = Mobile
        view.save()
        userextend = UserExtend()
        userextend.profession = Profession
        userextend.user_id = request.user.id
        userextend.save()
        return HttpResponse('sucess')


    context = {
        'view': view
    }
    return render(request,'registration/registration-freelancer.html',context)

def register_professional(request):
    view = CustomUser.objects.get(id=request.user.id)
    if request.method == "POST":

        First_Name = request.POST.get('first_name')
        Last_Name = request.POST.get('last_name')
        Email = request.POST.get('email')
        Mobile = request.POST.get('phone')
        Profession = request.POST.get('profession')
        view.first_name = First_Name
        view.last_name = Last_Name
        view.email = Email
        view.username = Mobile
        view.save()
        userextend = UserExtend()
        userextend.profession = Profession
        userextend.user_id = request.user.id
        userextend.save()

        return HttpResponse('sucess')

    context = {
        'view': view
    }


    return render(request,'registration/registration-professional.html',context)
def register_public(request):
    view = CustomUser.objects.get(id=request.user.id)
    if request.method == "POST":
        First_Name = request.POST.get('first_name')
        Last_Name = request.POST.get('last_name')
        Email = request.POST.get('email')
        Mobile = request.POST.get('phone')



        view.first_name = First_Name
        view.last_name = Last_Name
        view.email = Email
        view.username = Mobile
        view.save()

    context = {
        'view': view
    }

    return render(request,'registration/registration-public.html',context)
def register_student(request):
    view = CustomUser.objects.get(id=request.user.id)
    if request.method == "POST":
        First_Name = request.POST.get('first_name')
        Last_Name = request.POST.get('last_name')
        Email = request.POST.get('email')
        Mobile = request.POST.get('phone')
        Degree = request.POST.get('degree')
        Specilization = request.POST.get('specialization')
        Startyear = request.POST.get('start_year')
        Endyear = request.POST.get('end_year')
        school = request.POST.get('school')
        view.first_name = First_Name
        view.last_name = Last_Name
        view.email = Email
        view.username = Mobile
        view.save()
        userextend = UserExtend()
        userextend.degree = Degree

        userextend.start_year = Startyear
        userextend.end_year = Endyear
        userextend.institution_name = school
        userextend.specilisation = Specilization

        userextend.user_id = request.user.id


        userextend.save()
        return HttpResponse('sucess')

    context = {
        'view': view
    }
    return render(request,'registration/registration-student.html',context)



###################################
def userslist(request):
    users = CustomUser.objects.all()

    context = {
        'users':users
    }
    return render(request,'userslist.html',context)
def userview(request,id):

    user = CustomUser.objects.get(id = id)
    followerscount = Follow.objects.filter(following_id = id)
    followers = followerscount.count()
    print(followers)
    followingcount = Follow.objects.filter(follower_id = id)
    following = followingcount.count()
    print(following)
    followstatus = Follow.objects.filter(follower_id = request.user.id,following_id = id).exists()

    print(id)
    print(request.user.id)
    print(followstatus)
    context = {
        'user': user,
        'followstatus': followstatus,
        'followers': followers,
        'following':following,
    }
    return render(request,'userview.html',context)

def follow(request,id):


    foll = Follow()
    foll.follower_id=request.user.id
    foll.following_id = id

    foll.save()

    return HttpResponse("true")



def unfollow(request,id):
    ufollow = Follow.objects.filter(follower_id = request.user.id,following_id = id)
    ufollow.delete()
    return HttpResponse("true")








