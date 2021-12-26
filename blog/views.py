from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
from blog.models import Post, Comment, Carinfo


class UploadView(ListView):
    model = Post
    template_name = 'about.html'

def index(request):
    if request.method == 'POST':
        year = request.POST['year']
        make = request.POST['make']
        model = request.POST['model']
        price = request.POST['price']
        info = request.POST['info']
        print(year,make,model,price,info)
        obj = Carinfo()
        obj.year = year
        obj.make = make
        obj.model = model
        obj.price = price
        obj.info = info 
        obj.save()
    context = {


    }
    return render(request,'about.html',context)




def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog_detail.html", context)
