# posts/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    category_dct = Post.category_dct.items()
    category_names = Post.category_dct.values()
    if request.method == "GET":
        category = request.GET.get("category")
        if category == None:
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(category=category)
    context = {
    'posts': posts,
    'category_names': category_names,
    'category_dct': category_dct,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)

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
    category_dct = Post.category_dct.items()
    category_names = Post.category_dct.values()
    context={
        'post':post,
        'category_names': category_names,
        'category_dct': category_dct,
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
