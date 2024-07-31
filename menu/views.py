from django.shortcuts import render
# from .models import Menu

# Create your views here.


def my_menu(request):
    """
    Renders the Menu page
    """
    return render(
        request,
        "menu/menu.html",
    )
