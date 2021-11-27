from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

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
