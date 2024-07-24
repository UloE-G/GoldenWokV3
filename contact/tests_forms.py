from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Test',
            'email': 'test@test.com',
            'number': '0872131234',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")