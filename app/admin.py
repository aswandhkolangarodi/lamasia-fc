from django.contrib import admin
from app.models import Award, Banner, Contact, Gallery, LatestNews, Matche,LastMatchHighlight, Product, ProductCategory, SponsorLogo,TeamPlayer
# Register your models here.


admin.site.register(Banner)
class Matches(admin.ModelAdmin):
    model = Matche
    list_display = ['team1','team2']
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

admin.site.register(Award)
class Sponsores(admin.ModelAdmin):
    model = SponsorLogo
    list_display = ['sponsors_logo']
admin.site.register(SponsorLogo,Sponsores)

admin.site.register(LatestNews)
admin.site.register(ProductCategory)

class Products(admin.ModelAdmin):
    model = Product
    list_display = ['product_image']
admin.site.register(Product,Products)

admin.site.register(Contact)
