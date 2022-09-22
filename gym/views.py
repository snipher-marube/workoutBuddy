from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Tag, Category, Blog, Comment, Profile


def home(request):
    return render(request, 'gym/home.html')

def single_blog(request, slug):

    recent_posts = Blog.objects.filter(active=True).order_by('-pub_date',)
    blog = Blog.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    reply_obj = None
    try:
        reply_id = int(request.POST.get('reply_id'))
    except:
        reply_id = None

    if reply_id:
        reply_qs = Comment.objects.filter(id=reply_id)
        if reply_qs.exists() and reply_qs.count() == 1:
            reply_obj = reply_qs.first()

    if request.method == 'POST':
        Comment.objects.create(
            author=request.user.profile,
            blog=blog,
            content=request.POST['comment'],
            reply=reply_obj,


        )

        messages.success(request, "You're comment was successfuly posted!")


        return redirect('single_blog', slug=blog.slug)

    context = {
        'blog': blog,
        'contegories': categories,
        'tags': tags,
        'recent_posts': recent_posts,

    }
    return render(request, 'gym/single-blog.html', context)

def about(request):
    return render(request, 'gym/about.html')

def blog(request):
    recent_posts = Blog.objects.filter(active=True).order_by('-pub_date',)
    blogs = Blog.objects.filter(active=True)
    page = request.GET.get('page')
    paginator = Paginator(blogs, 5)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {
        'tags': tags,
        'categories': categories,
        'blogs': blogs,
        'recent_posts': recent_posts
    }
    return render(request, 'gym/blog.html', context)

def contact(request):
    return render(request, 'gym/contact.html')

def gallery(request):
    return render(request, 'gym/gallery.html')

def pricing(request):
    return render(request, 'gym/pricing.html')

def search(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    query = request.GET.get('query')
    blogs = Blog.objects.all()

    if query is not None:
        blogs = blogs.filter(Q(title__icontains=query) | Q(tag__tag__icontains=query) |
                             Q(category__category_name__icontains=query))
        page = request.GET.get('page')
        paginator = Paginator(blogs, 5)

        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

    context = {
        'blogs': blogs,
        'query': query,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'gym/search.html', context)



