from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.contrib import messages

# Create your views here.
def post_list_and_review(request, slug=None):
    queryset = Post.objects.filter(status=1)
    post = None
    comments = None
    comment_count = None
    comment_form = None

    if slug:
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            # comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
            )

    if not comment_form:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    }

    if post:
        template_name = "about/index.html"
    else:
        template_name = "about/other_template.html"

    return render(
        request, 
        "about/index.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },)