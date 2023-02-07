from datetime import date
from django.shortcuts import render , get_object_or_404

from blog.models import Post 


def getDate(post):
    return post['date']
# Create your views here.


def startingPage(request) :
    #sorted_posts = sorted(all_posts,key=getDate)
    latestPosts = Post.objects.all().order_by("-date")[:3] #getting 3 last  posts objects ordered
    return render(request,"blog/index.html",{
        "posts" : latestPosts
    })

def posts(request):
    allPosts = Post.objects.all().order_by("-date")
    return render(request,"blog/all-posts.html",{
        "all_posts" : allPosts
    })

def postDetails(request,slug):
    identified_post = get_object_or_404(Post , slug=slug)
    return render(request,"blog/post-Detail.html",{
        "post" : identified_post,
        "postTags" : identified_post.tag.all()
    })
