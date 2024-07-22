from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages

# Create your views here.
def post_list_and_review(request):
    queryset = Post.objects.filter(status=1)
    post = None
    comments = Comment.objects.all()
    comment_count = None
    comment_form = None

    # if slug:
    #     post = get_object_or_404(queryset, slug=slug)
    #     comments = post.comments.all().order_by("-created_on")
    #     comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            print("Valid form")
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post_id = request.POST.get('post')  # Set the post_id directly
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
            )

    
    comment_form = CommentForm()
    print("About to render template")

    context = {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    }

    # if post:
    #     template_name = "about/index.html"
    # else:
    #     template_name = "about/other_template.html"

    return render(request, "about/index.html", context)

def comment_edit(request, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        # post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            # comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('about'))

def comment_delete(request, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    # post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('about'))