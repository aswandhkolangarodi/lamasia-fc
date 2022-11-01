from django.contrib import admin
from app.models import *
# Register your models here.


admin.site.register(Banner)

admin.site.register(Tournament)

class Matches(admin.ModelAdmin):
    model = Matche
    list_display = ['team1','team2']
    search_fields=('team1','team2',)
admin.site.register(Matche,Matches)

class video(admin.ModelAdmin):
    model = LastMatchHighlight
    list_display = ['video']
admin.site.register(LastMatchHighlight,video)

admin.site.register(TeamPlayer)

class Galleries(admin.ModelAdmin):
    model = Gallery
    list_display = ['images']
admin.site.register(Gallery,Galleries)


class AwardAdmin(admin.ModelAdmin):
    model = Award
    list_display = ['tournament_name','trophy_count',]
    search_fields=('tournament_name',)
admin.site.register(Award,AwardAdmin)


class Sponsores(admin.ModelAdmin):
    model = SponsorLogo
    list_display = ['sponsors_logo']
admin.site.register(SponsorLogo,Sponsores)

admin.site.register(LatestNews)
admin.site.register(ProductCategory)

class Products(admin.ModelAdmin):
    model = Product
    list_display = ['category']
admin.site.register(Product,Products)

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['name','email','phone_number',]
    search_fields=('name','email','phone_number')
admin.site.register(Contact,ContactAdmin)


class BoardManagementAdmin(admin.ModelAdmin):
    model = BoardManagement
    list_display = ['name','position','citizenship','date_of_birth',]
    search_fields=('name','position')
admin.site.register(BoardManagement,BoardManagementAdmin)


admin.site.register(AccademyFee)



class Registrations(admin.ModelAdmin):
    model = Registration
    list_display = ['name','contactnum','guardiannum']
    search_fields=('name','contactnum','guardiannum')
admin.site.register(Registration,Registrations)




class Customers(admin.ModelAdmin):
    model = Customer
    list_display = ['name','phone','place']
    search_fields=('name','phone','place')
admin.site.register(Customer,Customers)




admin.site.register(User)

class Leagues(admin.ModelAdmin):
    model = League
    list_display = ['title']
admin.site.register(League,Leagues)

class Leagueteams(admin.ModelAdmin):
    model = Leagueteam
    list_display = ['team']
admin.site.register(Leagueteam,Leagueteams)



class LeagueMatchess(admin.ModelAdmin):
    model = LeagueMatches
    list_display = ['team1','team2','league']
    search_fields=('team1','team2','league')
admin.site.register(LeagueMatches,LeagueMatchess)




class LeagueMatchesPoints(admin.ModelAdmin):
    model = LeagueMatchesPoint
    list_display = ['league','team','match','win','lose','draw']
    search_fields=('team','league')
admin.site.register(LeagueMatchesPoint,LeagueMatchesPoints)



class ClubDetailss(admin.ModelAdmin):
    model = ClubDetails
    list_display = ['club','president']
    search_fields=('club','president')
admin.site.register(ClubDetails,ClubDetailss)

class ClubPlayers(admin.ModelAdmin):
    model = ClubPlayer
    list_display = ['name','club','kit_number']
    search_fields=('name','club','kit_number')
admin.site.register(ClubPlayer,ClubPlayers)



class ClubAwards(admin.ModelAdmin):
    model = ClubAward
    list_display = ['awardname','club']
    search_fields=('awardname','club')
admin.site.register(ClubAward,ClubAwards)




class ClubGallerys(admin.ModelAdmin):
    model = ClubGallery
    list_display = ['club','photo']
    search_fields=('photo','club')
admin.site.register(ClubGallery,ClubGallerys)


class ClubJersys(admin.ModelAdmin):
    model = ClubJersy
    list_display = ['club','title']
    search_fields=('club','title')
admin.site.register(ClubJersy,ClubJersys)



admin.site.register(CartIteams)

admin.site.register(Order)

class OrderLists(admin.ModelAdmin):
    model = OrderList
    list_display = ['order']
admin.site.register(OrderList,OrderLists)