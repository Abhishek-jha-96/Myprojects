from django.shortcuts import render
from .models import Post, Category, Author
from django.db.models import Q
# Create your views here.

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def homepage(request):
    category = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        'latest': latest,
        'category': category,
    }
    return render(request, 'homepage.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    latest = Post.objectsorder_by('-timestamp')[:3]
    context = {
        'post': post,
        'latest': latest
    }
    return render(request, 'post.html', context)

def about(request):
    return render(request, 'about_page.html')

def category_post_list(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category__in=[category])
    context = {
        "posts": posts,
        'category': category,
    }
    return render(request, 'post_list.html', context)

def allposts(request):
    posts = Post.objects.order_by('-timestamp')
    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'object_list': queryset,
    }
    return render(request, 'search_results.html', context)
