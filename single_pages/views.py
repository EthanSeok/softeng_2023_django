from django.shortcuts import render

def landing_page(request):
    return render(
        request,
        'single_pages/landing_page.html',
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html',
    )

# Create your views here.