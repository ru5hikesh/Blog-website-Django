from django.shortcuts import render
from .models import Post  # Add this line to import the Post model


def index(request):
    posts = Post.objects.all().order_by(
        "-created_at"
    )  # Assuming you want the latest posts first
    return render(request, "index.html", {"posts": posts})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, "posts.html", {"posts": posts})
