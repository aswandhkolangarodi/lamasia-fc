from turtle import position
from django.shortcuts import render

from app.models import Award, Banner, Contact, Gallery, LastMatchHighlight, LatestNews,Matche, Product, SponsorLogo, TeamPlayer
from datetime import date
 # Create your views here.


def index(request):
    banner=Banner.objects.all()
    upComingMatch = Matche.objects.filter(match_date__gte=date.today(),status =False).order_by('match_date').first()
    completedMatches= Matche.objects.filter(status= True)
    video =LastMatchHighlight.objects.all().last()
    players = TeamPlayer.objects.all()
    gallery = Gallery.objects.all()
    awards = Award.objects.all()
    sponsors = SponsorLogo.objects.all()
    latestNews= LatestNews.objects.filter(date__lte=date.today()).last()     
    news = LatestNews.objects.filter(date__lte=date.today())
    products = Product.objects.all()
    players_count = TeamPlayer.objects.all().count()
    award_count = Award.objects.all().count()
    context = {
        'award_count':award_count,
        'players_count':players_count,
        'products':products,
        'news':news,
        'latestNews':latestNews,
        'sponsors':sponsors,
        'awards':awards,
        'gallery':gallery,
        'players':players,
        'video':video,
        'completedMatches':completedMatches,
        'upComingMatch':upComingMatch,
        'banner':banner,
        'is_index':True
    }
    return render(request, "index.html", context)
    


def about(request):
    context={
        'is_history':True
    }
    return render(request, 'about.html', context)



def board_management(request):
    sponsors = SponsorLogo.objects.all()
    context = {
        'sponsors':sponsors,
        'is_board_management':True
    }
    return render(request , 'board-management.html', context)


def sponsors(request):
    sponsors = SponsorLogo.objects.all()
    context = {
        'sponsors':sponsors,
        'is_sponsors':True
    }
    return render(request, 'sponsors.html', context)


def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone_number=phone, subject=subject, message=message)
        contact.save()
    sponsors = SponsorLogo.objects.all()
    context = {
        'sponsors':sponsors,
        'is_contact':True
    }
    return render(request, 'contact.html', context)


def news(request):
    sponsors = SponsorLogo.objects.all()
    news = LatestNews.objects.all()
    context = {
        'sponsors':sponsors,
        'news':news,
        'is_news':True
    }
    return render(request, 'blog.html', context)



def club(request):
    sponsors = SponsorLogo.objects.all()
    context = {
        'sponsors':sponsors,
        
    }
    return render(request, 'single-club.html', context)


def team(request):
    sponsors = SponsorLogo.objects.all()
    goalKeepers = TeamPlayer.objects.filter(position = 'GOAL KEEPER')
    defenders = TeamPlayer.objects.filter(position = 'DEFENDER')
    midfielder = TeamPlayer.objects.filter(position = 'MIDFIELDER')
    forwarder = TeamPlayer.objects.filter(position = 'FORWARDER')
    context = {
        'sponsors':sponsors,
        'forwarder':forwarder,
        'midfielder':midfielder,
        'defenders':defenders,
        'goalKeepers':goalKeepers,
        'is_club':True
    }
    return render(request, 'first-team.html', context)


def gallery(request):
    sponsors = SponsorLogo.objects.all()
    gallery = Gallery.objects.all()
    context = {
        'sponsors':sponsors,
        'gallery':gallery,
        'is_gallery':True
    }
    return render(request, 'gallery.html', context)


def shop(request):
    sponsors = SponsorLogo.objects.all()
    context = {
        'sponsors':sponsors,
        
    }
    return render(request, 'shop.html', context)


def cart(request):
    sponsors = SponsorLogo.objects.all()
    context = {
        'sponsors':sponsors,
        
    }
    return render(request, 'cart.html', context)



def player_profile(request, player_id):
    sponsors = SponsorLogo.objects.all()
    player = TeamPlayer.objects.get(id=player_id)
    context = {
        'sponsors':sponsors,
        'player':player
    }
    return render(request, 'team-single.html',context)