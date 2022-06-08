from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'is_index':True
    }
    return render(request, "index.html", context)
    

def board_management(request):
    context = {
        'is_board_management':True
    }
    return render(request , 'board-management.html', context)


def sponsors(request):
    context = {
        'is_sponsors':True
    }
    return render(request, 'sponsors.html', context)


def contact(request):
    context = {
        'is_contact':True
    }
    return render(request, 'contact.html', context)


def news(request):
    context = {
        'is_news':True
    }
    return render(request, 'blog.html', context)



def club(request):
    context = {
        'is_club':True
    }
    return render(request, 'single-club.html', context)


def team(request):
    return render(request, 'first-team.html')


def gallery(request):
    return render(request, 'gallery.html')


def shop(request):
    return render(request, 'shop.html')


def cart(request):
    return render(request, 'cart.html')