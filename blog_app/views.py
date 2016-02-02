from django.shortcuts import render
from blog_app.models import Blog, Comment
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from blog_app.forms import CommentForm
from django.contrib.auth import logout
from blog_app.forms import BlogForm

def index(request):
    try:
        blog_data=Blog.objects.all()[::-1]
    except Blog.DoesNotExist:
        pass
    return render(request,"blog_app/index.html",{'blog_data':blog_data})


def blog_edit(request,blog_title_slug):
    if request.method=='POST':
        new_title=request.POST.get('title', None)
        new_post=request.POST.get('post', None)
        Blog.objects.get(slug=blog_title_slug).delete()
        Blog.objects.create(
            title=new_title,
            story=new_post,
            slug=blog_title_slug,
            )
        return HttpResponseRedirect('/blog_app/')
    try:
        blog=Blog.objects.get(slug=blog_title_slug)
        story=blog.story
        story=story.replace("\n","\\")
    except Blog.DoesNotExist:
        pass
    return render(request,'blog_app/blog_edit.html',{'blog':blog,'story':story})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/blog_app/')

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
          
                login(request, user)
                return HttpResponseRedirect('/blog_app/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
    
        return render(request, 'blog_app/login.html', {})

from blog_app.forms import UserForm, UserProfileForm


def register(request):

    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'blog_app/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

import json
def read_more(request,blog_title_slug):
    context_dict={}
    if request.method=='POST':
        comment_in=request.POST.get('comment', None)
        blog=Blog.objects.get(slug=blog_title_slug)
        Comment.objects.create(
            blog_title=blog,
            comment=comment_in,
            )
        comment_objects=Comment.objects.filter(blog_title=blog)
        comment_list=[]

        for obj in comment_objects:
            comment_list.append(obj.comment)
        context=json.dumps({'json':comment_list})

        return HttpResponse(context)
    try:
		blog=Blog.objects.get(slug=blog_title_slug)
		context_dict['blog_title']=blog.title

		comments=Comment.objects.filter(blog_title=blog)
		context_dict['comments']=comments
		context_dict['blog']=blog
        
    except Blog.DoesNotExist:
        pass
    return render(request,'blog_app/read_more.html',context_dict)


def delete_post(request,id):
   Blog.objects.get(pk=id).delete()
   return redirect(index)

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = BlogForm()

    return render(request, 'blog_app/add_blog.html', {'form': form})