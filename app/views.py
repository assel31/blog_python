from django.shortcuts import render, get_object_or_404
from app.models import Post, Category, Comment

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post(request, id):
    post = get_object_or_404(Post, id = id)
    comments = post.comments.all()
    return render(request, 'post.html', {'post': post, 'comments': comments})
