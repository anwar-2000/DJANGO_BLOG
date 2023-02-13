from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = "__all__"
        labels={
            "username " : "Your Username :",
            "text" : "Your Thoughts :"
        }
        error_messages = {"username" : {
            "required" : "you should add your username",
        },
        "text" : {
            "required" : "you should add your thoughts",
        }}
