from datetime import date
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Post 

from django.views.generic import ListView , View , TemplateView

from .forms import CommentForm

################################## changin logic with class based views



#def getDate(post):
 #return post['date']
# Create your views here.


class startingPage(TemplateView) :
    template_name ="blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latestPosts"] = Post.objects.all().order_by("-date")[:3] #getting 3 last  posts objects ordered
        return context
    
class posts(ListView):
    model = Post
    template_name="blog/all-posts.html"
    context_object_name="all_posts"
   ########### a queryset to render data from last to first
    def get_queryset(self):
      return Post.objects.all().order_by("-date")
    
    

class postDetails(View):
    
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context={
            "post" : post,
            "postTags" : post.tag.all(),
            "form" : CommentForm()
        }
        return render('blog/post-detail.html',context)

    def post(self,request,slug):
        post = Post.objects.get(slug=slug)

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post

            comment.save()
            return HttpResponseRedirect(reverse('postDetails-page',args=[slug]))
        #else .....
        
        context={
            "post" : post,
            "postTags" : post.tag.all(),
            "form" : comment_form #saving user entered data
        }
        return render('blog/post-detail.html',context)
            
    
