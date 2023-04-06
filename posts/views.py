# posts/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

def new(request):
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/new.html', context)


@login_required
def create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save()
        return redirect('posts:detail', post.pk)
    context = {
        'form': form,
    }
    return render(request, 'posts/index.html', context)

def edit(request, post_pk):
    post=Post.objects.get(pk=post_pk)
    form = PostForm(instance=post)
    context={
        'post':post,
        'form':form,
    }
    return render(request,'posts/edit.html',context)

def detail(request, post_pk):
    post=Post.objects.get(pk=post_pk)
    context={
        'post':post,
    }
    return render(request, 'posts/detail.html',context)

@login_required
def delete(request, post_pk):
    post=Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('posts:index')

@login_required
def update(request, post_pk):
    post=Post.objects.get(pk=post_pk)
    post.title=request.POST.get('title')
    post.content=request.POST.get('content')
    post.category=request.POST.get('category')
    post.save()
    return redirect('posts:detail',post.pk)
