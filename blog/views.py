from datetime import date
from django.shortcuts import render , get_object_or_404

from blog.models import Post 

from django.views.generic import ListView , DetailView , TemplateView

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
    
    

class postDetails(DetailView):
    template_name ="blog/post-detail.html"
    model = Post
    slug_field ="slug"
    slug_url_kwarg ="slug"

    def get_queryset(self):
        return Post.objects.all()
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        post = self.get_object()
        context['postTags'] = post.tag.all() #with related name of tag field
        form = CommentForm()
        context['form'] =form
        return context
    
    
