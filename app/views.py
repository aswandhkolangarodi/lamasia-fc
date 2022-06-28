from turtle import position
from unicodedata import category
from django.shortcuts import render

from app.models import Award, Banner, BoardManagement, Contact, Gallery, LastMatchHighlight, LatestNews,Matche, Product, SponsorLogo, TeamPlayer
from datetime import date, datetime
from django.db.models import Q
 # Create your views here.


def index(request):
    banner1=Banner.objects.all().first()
    banner2=Banner.objects.all().last()
    print(datetime.now())
    upComingMatch = Matche.objects.filter(match_date__gte=datetime.now(),completed =False).order_by('match_date').first()
    completedMatches= Matche.objects.filter(completed = True)
    video =LastMatchHighlight.objects.all().last()
    players = TeamPlayer.objects.all()
    gallery = Gallery.objects.all()[:6]
    awards = Award.objects.all()
    sponsors = SponsorLogo.objects.all()
    latestNews= LatestNews.objects.all().order_by('-date').first()     
    news = LatestNews.objects.all().order_by('-date')[1:6]
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
        'banner':banner1,
        'banner2':banner2,
        'is_index':True
    }
    return render(request, "index.html", context)
    


def history(request):
    sponsors = SponsorLogo.objects.all()
    context={
        'sponsors':sponsors,
        'is_history':True
    }
    return render(request, 'history.html', context)



def board_management(request):
    sponsors = SponsorLogo.objects.all()
    boardManagement = BoardManagement.objects.all() 
    context = {
        'boardManagement':boardManagement,
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
    news = LatestNews.objects.all().order_by('-date')[:15]
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


def reserve_senior(request):
    sponsors = SponsorLogo.objects.all()
    goalKeepers = TeamPlayer.objects.filter(category= 'reserve senior',position = 'GOAL KEEPER')
    defenders = TeamPlayer.objects.filter(Q(category = 'reserve senior') , Q(position = 'LEFT BACK') | Q(position='RIGHT BACK'))
    midfielder = TeamPlayer.objects.filter(Q(category = 'reserve senior') , Q(position = 'DEFENSIVE MIDFIELDER') | Q(position='ATTACKING MIDFIELDER') | Q(position='CENTER MIDFIELDER'))
    forwarder = TeamPlayer.objects.filter(Q(category = 'reserve senior') , Q(position = 'LEFT WING FORWARD') | Q(position='RIGHT WING FORWARD') | Q(position='CENTER FORWARD'))
    context = {
        'sponsors':sponsors,
        'forwarder':forwarder,
        'midfielder':midfielder,
        'defenders':defenders,
        'goalKeepers':goalKeepers,
        'is_club':True
    }

    return render(request, 'first-team.html', context)



def under_18(request):
    sponsors = SponsorLogo.objects.all()
    goalKeepers = TeamPlayer.objects.filter(category= 'under 18',position = 'GOAL KEEPER')
    defenders = TeamPlayer.objects.filter(Q(category = 'under 18') , Q(position = 'LEFT BACK') | Q(position='RIGHT BACK'))
    midfielder = TeamPlayer.objects.filter(Q(category = 'under 18') , Q(position = 'DEFENSIVE MIDFIELDER') | Q(position='ATTACKING MIDFIELDER') | Q(position='CENTER MIDFIELDER'))
    forwarder = TeamPlayer.objects.filter(Q(category = 'under 18') , Q(position = 'LEFT WING FORWARD') | Q(position='RIGHT WING FORWARD') | Q(position='CENTER FORWARD'))
    context = {
        'sponsors':sponsors,
        'forwarder':forwarder,
        'midfielder':midfielder,
        'defenders':defenders,
        'goalKeepers':goalKeepers,
        'is_club':True
    }

    return render(request, 'first-team.html', context)



def under_15(request):
    sponsors = SponsorLogo.objects.all()
    goalKeepers = TeamPlayer.objects.filter(category= 'under 15',position = 'GOAL KEEPER')
    defenders = TeamPlayer.objects.filter(Q(category = 'under 15') , Q(position = 'LEFT BACK') | Q(position='RIGHT BACK'))
    midfielder = TeamPlayer.objects.filter(Q(category = 'under 15') , Q(position = 'DEFENSIVE MIDFIELDER') | Q(position='ATTACKING MIDFIELDER') | Q(position='CENTER MIDFIELDER'))
    forwarder = TeamPlayer.objects.filter(Q(category = 'under 15') , Q(position = 'LEFT WING FORWARD') | Q(position='RIGHT WING FORWARD') | Q(position='CENTER FORWARD'))
    context = {
        'sponsors':sponsors,
        'forwarder':forwarder,
        'midfielder':midfielder,
        'defenders':defenders,
        'goalKeepers':goalKeepers,
        'is_club':True
    }

    return render(request, 'first-team.html', context)



def under_13(request):
    sponsors = SponsorLogo.objects.all()
    goalKeepers = TeamPlayer.objects.filter(category= 'under 13',position = 'GOAL KEEPER')
    defenders = TeamPlayer.objects.filter(Q(category = 'under 13') , Q(position = 'LEFT BACK') | Q(position='RIGHT BACK'))
    midfielder = TeamPlayer.objects.filter(Q(category = 'under 13') , Q(position = 'DEFENSIVE MIDFIELDER') | Q(position='ATTACKING MIDFIELDER') | Q(position='CENTER MIDFIELDER'))
    forwarder = TeamPlayer.objects.filter(Q(category = 'under 13') , Q(position = 'LEFT WING FORWARD') | Q(position='RIGHT WING FORWARD') | Q(position='CENTER FORWARD'))
    context = {
        'sponsors':sponsors,
        'forwarder':forwarder,
        'midfielder':midfielder,
        'defenders':defenders,
        'goalKeepers':goalKeepers,
        'is_club':True
    }

    return render(request, 'first-team.html', context)



def under_12(request):
    sponsors = SponsorLogo.objects.all()
    goalKeepers = TeamPlayer.objects.filter(category= 'under 12',position = 'GOAL KEEPER')
    defenders = TeamPlayer.objects.filter(Q(category = 'under 12') , Q(position = 'LEFT BACK') | Q(position='RIGHT BACK'))
    midfielder = TeamPlayer.objects.filter(Q(category = 'under 12') , Q(position = 'DEFENSIVE MIDFIELDER') | Q(position='ATTACKING MIDFIELDER') | Q(position='CENTER MIDFIELDER'))
    forwarder = TeamPlayer.objects.filter(Q(category = 'under 12') , Q(position = 'LEFT WING FORWARD') | Q(position='RIGHT WING FORWARD') | Q(position='CENTER FORWARD'))
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
        'is_club':True,
        'sponsors':sponsors,
        'player':player
    }
    return render(request, 'team-single.html',context)


def single_news(request, news_id):
    news = LatestNews.objects.get(id=news_id)
    sponsors = SponsorLogo.objects.all()
    latest_newses = LatestNews.objects.all().order_by('-date')[:6]
    context = {
        'is_news':True,
        'latest_newses':latest_newses,
        'sponsors':sponsors,
        'news':news
    }

    return render(request, 'single-news.html', context)