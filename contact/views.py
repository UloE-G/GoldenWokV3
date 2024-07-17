from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import CollaborateForm

def contact_me(request):
    """
    Renders the Contact page
    """
    print("Rendering template")

    if request.method == "POST":
        print("Recived post request")
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            print("Valid request")
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, 
            "Booking request received! our team typically responds within 12 Hours.")

    contact = Contact.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "contact/contact.html",
        {"contact": contact,
        "collaborate_form": collaborate_form},
    )