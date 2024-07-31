from django.test import TestCase
from django.urls import reverse
from .models import Contact
from .forms import CollaborateForm


class TestContactView(TestCase):

    def setUp(self):
        """Creates Contact content"""
        self.contact_content = Contact(
            title="Contact", content="Contact page.")
        self.contact_content.save()

    def test_render_contact_page_with_booking_form(self):
        """Verifies get request for contact containing a booking request"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
