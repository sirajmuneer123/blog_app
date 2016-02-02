from django import forms
from blog_app.models import Blog, Comment,UserProfile
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Title")
    x={'rows':15, 'cols':100,'placeholder':"Type blog..........."}
    story=forms.CharField(widget=forms.Textarea(attrs=x),help_text="Story")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    
    class Meta:
        
        model = Blog
        fields = ('title','story')

class CommentForm(forms.ModelForm):
    comment=forms.CharField(max_length=128,help_text='Comment ')
    class Meta:
        model = Comment
        fields=('comment',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
		model = UserProfile
		fields = ('picture',)