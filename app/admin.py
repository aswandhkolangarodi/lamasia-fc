from django.contrib import admin
from app.models import Award, Banner, Contact, Gallery, LatestNews, Matche,LastMatchHighlight, Product, ProductCategory, SponsorLogo,TeamPlayer
# Register your models here.


admin.site.register(Banner)
admin.site.register(Matche)
admin.site.register(LastMatchHighlight)
admin.site.register(TeamPlayer)
admin.site.register(Gallery)
admin.site.register(Award)
admin.site.register(SponsorLogo)
admin.site.register(LatestNews)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Contact)
