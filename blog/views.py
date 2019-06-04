from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import BlogPost

from .models import Blog

# Create your views here.

def blog(request):
    blogs = Blog.objects
    return render(request, 'blog.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))


def blogpost(request):
        if request.method =='POST':
            form = BlogPost(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.pub_date=timezone.now()
                post.save()
                return redirect('blog')
        else:
            form = BlogPost()
            return render(request,'new.html',{'form':form})


