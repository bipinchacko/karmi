import json


from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from social.models import Post

from social.forms import PostForm

from byhand.models import Follow

from social.models import Like

from social.models import Comment


def PostView(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            a = form.cleaned_data['caption']
            b = form.cleaned_data['image']
            post.user_id = request.user.id
            post.save()
            return HttpResponse('sucess')






        # Cmnt = request.POST.get('caption')
        # img = request.POST.get('image')
        # post = Post()
        # post.caption = Cmnt
        # post.image = img
        # post.save()
        # print(Cmnt,img)
    return render(request,'post.html',{'form':form})

def index(request):
    print(request.user.id)

    fol = Follow.objects.filter(follower_id = request.user.id)

    group_ids = []
    for i in fol:
        group_ids.append(i.following_id)


    print(group_ids)
    post_items = Post.objects.filter(user_id__in=group_ids).all()



    liked = Like.objects.filter(user_id=request.user.id).exists()

    if request.method == "POST":
        id = request.POST.get('id')
        comment = request.POST.get('comment')
        commentv = Comment()
        commentv.comment = comment
        commentv.post_id = id
        commentv.user_id = request.user.id
        commentv.save()
        post = Post.objects.get(id = id)
        print(post)
        current_comments = post.comments
        post.comments = current_comments + 1
        post.save()








    # pos = Post.objects.filter(user_id = request.user.id)
    context = {
        'liked':liked,
        'post_items': post_items,


    }

    return render(request,'index.html',context)

def like(request,id):


    # if liked:
    #     dislike = Like.objects.filter(post_id = id)
    #     dislike.delete()
    #     liked = False
    #     return HttpResponse('true')
    # else:


    like=Like()
    like.user_id = request.user.id
    like.post_id = id
    like.save()

    post = Post.objects.get(id=id)
    current_like = post.likes
    post.likes = current_like +1
    post.save()
    return redirect('index')

def dislike(request,id):
     dislike = Like.objects.filter(post_id = id)
     dislike.delete()

     post = Post.objects.get(id=id)
     current_like = post.likes
     post.likes = current_like - 1
     post.save()
     return redirect('index')

def likecount(request,id):
    likescount = Like.objects.filter(post_id = id).count()
    return render(request,'index.html',{'likescount':likescount})

# def comment(request):
#
#         return HttpResponse('sucess')
#
#     return render(request,'index.html')

def post_detail(request,id):
    post = Post.objects.get(id=id)
    comment = Comment.objects.filter(post_id = id)

    context = {
        'post':post,
        'comment':comment,
    }
    return render(request,'post-details.html',context)

def profile(request):
    print(request.user.id)

    return render(request,'profile/profile.html')










    # def __str__(self):
    #     return 'Comment by {} on {}'.format(self.name, self.post)


