from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from . models import *
from datetime import date, datetime
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import  Sum
from django.http import HttpResponseRedirect
from django.conf import settings

import stripe
import uuid
stripe.api_key = settings.STRIPE_PRIVATE_KEY

YOUR_DOMAIN = 'http://127.0.0.1:8000'
 # Create your views here.


def index(request):
    print(request.user)
    banner1=Banner.objects.all()
    # banner2=Banner.objects.all().last()
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
    fee = AccademyFee.objects.all()
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
        'fee':fee,
        'is_index':True,
        "status":0
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



def club(request,id):
    teamlist=Leagueteam.objects.get(id=id)
    if ClubDetails.objects.filter(club=teamlist).exists():
        clubdetails= ClubDetails.objects.get(club=teamlist)
        matchlist1=LeagueMatches.objects.filter(team1=teamlist,completed=False)
        matchlist2=LeagueMatches.objects.filter(team2=teamlist,completed=False)
        totalmatches1=LeagueMatches.objects.filter(team1=teamlist,completed=False).count()
        totalmatches2=LeagueMatches.objects.filter(team2=teamlist,completed=False).count()
        completematch=totalmatches1+totalmatches2
        print(completematch)
        sponsors = SponsorLogo.objects.all()
        players = ClubPlayer.objects.filter(club=teamlist)
        awards =ClubAward.objects.filter(club=teamlist)
        gallery=ClubGallery.objects.filter(club=teamlist)
        jersey=ClubJersy.objects.filter(club=teamlist)
        if completematch <= 1:

            context = {
            'sponsors':sponsors,
            "clubdetails":clubdetails,
            "players":players,
            "awards":awards,
            "gallery":gallery,
            "jersey":jersey,

            
            }
            return render(request, 'single-club.html', context)
        else:
            context = {
            'sponsors':sponsors,
            "clubdetails":clubdetails,
            "matchlist1":matchlist1,
            "matchlist2":matchlist2,
            "players":players,
            "awards":awards,
            "gallery":gallery,
            "jersey":jersey,

            
        }
        return render(request, 'single-club.html', context)
        
    else:
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
        'is_club':True,
        'status':"Senior"
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
        'is_club':True,
        'status':"Under-18"
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
        'is_club':True,
        'status':"Under-15"
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
        'is_club':True,
        'status':"Under-13"
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
        'is_club':True,
        'status':"Under-12"
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
    product=Product.objects.all()
    context = {
        'sponsors':sponsors,
        "product":product
        
    }
    return render(request, 'shop.html', context)

@login_required(login_url="/login")
def cart(request):
    sponsors = SponsorLogo.objects.all()
    custid=Customer.objects.get(id=request.user.customer.id)
    cartitems= CartIteams.objects.filter(user=custid)
    totalvalue=cartitems.aggregate(Sum('total'))
    totalAmonut = totalvalue['total__sum']
    print(totalAmonut)
  
    context = {
        'sponsors':sponsors,
        "cartitems":cartitems,
        "totalAmonut":totalAmonut,
        "status":0
        
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


def matchFixtures(request):
    match = Matche.objects.filter(match_date__gte=datetime.now(),completed =False).order_by('match_date')
    context = {
        'match':match,
        'is_match':True,
    }
    return render(request, 'match-fixtures.html',context)


def join(request):
    under18 = TeamPlayer.objects.filter(category='under 18')
    under15 = TeamPlayer.objects.filter(category='under 15')
    under13 = TeamPlayer.objects.filter(category='under 13')
    under12 = TeamPlayer.objects.filter(category='under 12')
    context = {
        'under18':under18,
        'under15':under15,
        'under13':under13,
        'under12':under12
        
    }
    return render(request, 'join.html',context)

    


def joinacademy(request):
    sponsors = SponsorLogo.objects.all()

    context = {
        'is_join':True,
        "sponsors":sponsors
    }
    return render(request, 'joinacademy.html', context)


def registration(request):
    name=request.POST['name']
    # photo=request.FILES['photo']
    photo=request.FILES.get("photo", "Photo Not Uploded")
    age=request.POST['age']
    dob=request.POST['dob']
    contactnum=request.POST['contactnum']
    guardiannum=request.POST['guardiannum']
    email=request.POST['email']
    place=request.POST['place']
    height=request.POST['height']
    weight=request.POST['weight']
    exclub=request.POST['exclub']
    education=request.POST['education']
    print(photo,'***********'*10)
    registrationss= Registration(name=name, email=email, contactnum=contactnum, guardiannum=guardiannum ,age=age ,dob=dob, place=place , height=height,weight=weight,  exclub=exclub, education=education,photo=photo, status="Not Seen")
    registrationss.save()
    
    return JsonResponse({'data':"eryset"})


def league(request):
    sponsors = SponsorLogo.objects.all()
    context = {
        'is_league':True,
        "sponsors":sponsors
    }
    return render(request, 'league.html', context)



def productsingle(request,id):
    sponsors = SponsorLogo.objects.all()
    product= Product.objects.get(id=id)
    # print(product.category.category_name)
    relatedproducts=Product.objects.filter(category__category_name=product.category.category_name)
    # print(relatedproducts)
    context = {
        'is_productsingle':True,
        "sponsors":sponsors,
        "product":product,
        "relatedproducts":relatedproducts
    }
    return render(request, 'productsingle.html', context)





def productsell(request):
    name=request.POST['name']
    place=request.POST['place']
    contactnum=request.POST['contactnum']
    pin=request.POST['pin']
    Address=request.POST['Address']
    size=request.POST['size']
    quantity=request.POST['quantity']
    totalprice=request.POST['totalprice']
    id=request.POST['id']
    proid= Product.objects.get(id=id)
    order= OrderList(product=proid, name=name, contactnum=contactnum,  place=place, pin=pin, Address=Address,size=size, quantity=quantity, totalprice=totalprice ,status="Not Seen" )
    order.save()
    
    
    
    
    return JsonResponse({'data':"eryset"})



def singleleaguedetails(request,name):
    sponsors = SponsorLogo.objects.all()
    leagueteam=Leagueteam.objects.all()
    leagues= League.objects.get(title=name)

    matchfixture=LeagueMatches.objects.filter(league=leagues,completed=False)
    completedmatch=LeagueMatches.objects.filter(league=leagues,completed=True).order_by('id')[:3]
    pointtable= LeagueMatchesPoint.objects.filter(league=leagues)
    # print(pointtable,"@"*10)
    class calculationpoints:
        def __init__(self, team,pic, match, win,lose,draw,goalscore,goalgained,goaldifference,totalpoint):
            self.team = team
            self.pic = pic
            self.match = match
            self.win = win
            self.lose = lose
            self.draw = draw
            self.goalscore = goalscore
            self.goalgained = goalgained
            self.goaldifference = goaldifference
            self.totalpoint = totalpoint

    pointlist = []
    for i in pointtable:
        team =i.team.team
        pic =i.team.teamlogo
        match=i.match
        win=i.win
        lose=i.lose
        draw=i.draw
        goalscore=i.goalscore
        goalgained=i.goalgained
        goaldifference=goalscore-goalgained
        totalpoint =(win*3)+(draw*1)+(lose*0)

        pointlist.append(calculationpoints(team, pic, match,win,lose,draw, goalscore,goalgained, goaldifference,totalpoint ))
            


    context = {
        "sponsors":sponsors,
        "name":name,
        "leagueteam":leagueteam,
        "matchfixture":matchfixture,
        "completedmatch":completedmatch,
        "pointlist":pointlist
        
    }
    return render(request, 'singleleaguedetails.html', context)

def userregistration(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        place=request.POST['place']
        username=request.POST['username']
        password=request.POST['password']
        pin=request.POST['pin']
        phone=request.POST['phone']
        city=request.POST['city']
        address=request.POST['address']
        reguser = Customer(name=name, username=username, phone=phone, email=email, password=password, place=place, city=city, address=address, pin=pin, status="Not Seen")
        reguser.save()
        User = get_user_model()
        User.objects.create_user(username=username, password=password,customer=reguser)
        return redirect('/login')


    else:
        sponsors = SponsorLogo.objects.all()
        context = {
            "sponsors":sponsors,
            
        }
        return render(request, 'userregistration.html', context)


def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser == True:
                return redirect('/')
            elif user.customer !=None:
                return redirect('/')
        else:
            msg = "* Incorrect Username or password *"
            return render(request,'login.html',{'msg':msg,})

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/login")
@csrf_exempt
def addtocart(request):
    id = request.POST["id"]
    productid=Product.objects.get(id=id)
    userid=request.user.customer
    qty=request.POST['qty']
    price=productid.price
    totalmoumt= int(price) * int(qty)

    addeditem=CartIteams(product=productid,user=userid,qty=qty,total=totalmoumt)
    addeditem.save()
    return JsonResponse({"value": "msg"})

@csrf_exempt
def deletecartitem(request):
    id = request.POST["id"]
    print(id)
    productid=Product.objects.get(id=id)
    print(productid)
    prodelect =CartIteams.objects.filter(product=productid).delete()
    print(prodelect)
    return JsonResponse({"value": "msg"})


@csrf_exempt
def savedata(request):
    # userid=request.user.customer
    # dataorder=Order(user=userid)
    # dataorder.save()
    # print(dataorder.id)
    # orderdet=Order.objects.get(id=dataorder.id)
    # cartitems=CartIteams.objects.filter(user=userid)
    # totalvalue=cartitems.aggregate(Sum('total'))
    # totalAmonut = totalvalue['total__sum']
    # print(totalAmonut)
    # orderditem=OrderList(order=orderdet,totalprice=totalAmonut)
    # orderditem.save()
    # CartIteams.objects.filter(user=userid).delete()
    return JsonResponse({"value": "msg"})


# payment

@csrf_exempt
def create_checkout_session(request):
    userid=request.user.customer
    cartitems=CartIteams.objects.filter(user=userid)
    totalvalue=cartitems.aggregate(Sum('total'))
    totalAmonut = totalvalue['total__sum']
    print(totalAmonut)
    amount = int(totalAmonut)
    pmnt_id = uuid.uuid4()
    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
      'price_data': {
        'currency': 'inr',
        'product_data': {
          'name': "Lamasia Football",
        },
        'unit_amount': amount*100,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url= f'http://127.0.0.1:8000/success',
    cancel_url=YOUR_DOMAIN + '/cancel',
    )     
    print(session.get("url"))
    return HttpResponseRedirect(session.get("url"))
    # return JsonResponse({'id': session.id})


def success(request):
    userid=request.user.customer
    dataorder=Order(user=userid)
    dataorder.save()
    print(dataorder.id)
    orderdet=Order.objects.get(id=dataorder.id)
    cartitems=CartIteams.objects.filter(user=userid)
    totalvalue=cartitems.aggregate(Sum('total'))
    totalAmonut = totalvalue['total__sum']
    print(totalAmonut)
    orderditem=OrderList(order=orderdet,totalprice=totalAmonut)
    orderditem.save()
    CartIteams.objects.filter(user=userid).delete()
    context={
        "status":1
    }
    return render(request, "index.html", context)


def cancel(request):
    context={
        "msg":"payment is not completed",
        "status":1
    }
    return render(request, 'cart.html', context)

