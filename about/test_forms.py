from django.test import TestCase
from .forms import CommentForm
from .models import Post
from django.contrib.auth.models import User


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        # Creating a user for the author
        author = User.objects.create(username='Test', password='test456')

        # Creating a post with the author's id
        post = Post.objects.create(title='Test Post',
                                   slug='test-post',
                                   author_id=author.id,
                                   content='Test Content')

        comment_form = CommentForm(
            {'post': post.id, 'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        # Creating a user for the author
        author = User.objects.create(username='Test', password='test456')

        # Creating a post with the author's id
        post = Post.objects.create(title='Test Post',
                                   slug='test-post',
                                   author_id=author.id,
                                   content='Test Content')

        comment_form = CommentForm({'post': post.id, 'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
