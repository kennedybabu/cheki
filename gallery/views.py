from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
    return render(request, 'index.html')

def home(request):
    posts = Post.all_posts()
    return render(request, 'home.html', {"posts": posts})


def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'all_photos/search.html', {"message":message, "posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_photos/search.html', {"message":message})

def post(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except ObjectDoesNotExist:
        raise Http404()
    print(post.location)
    return render(request, 'all_photos/post.html', {"post":post})
