from versatileimagefield.fields import VersatileImageField,PPOIField
from django.db import models
from datetime import  datetime


# Create your models here.



class Banner(models.Model):
    top_heading = models.CharField(max_length=100, null=True)
    sub_heading = models.CharField(max_length=100, null=True)
    dscription = models.CharField(max_length=500, null=True)
    banner_image = models.FileField(upload_to ='banner/', null=True)

    def __str__(self):
        return self.sub_heading
    

class Matche(models.Model):
    team1 =models.CharField(max_length=100)
    team2 =models.CharField(max_length=100)
    team1_logo = models.ImageField(upload_to="team_logos/")
    team2_logo = models.ImageField(upload_to="team_logos/")
    match_date = models.DateTimeField(null=True, default=datetime.today())
    # time = models.TimeField(null=True)
    stadium  = models.CharField(max_length=200)
    team1_goals = models.CharField(max_length=100, null=True, default="0")
    team2_goals = models.CharField(max_length=100, null=True, default="0")
    completed = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.team1 


class LastMatchHighlight(models.Model):
    video = models.FileField(upload_to='video/')


    


class TeamPlayer(models.Model):
    GOALKEEPER = 'GOAL KEEPER'
    DEFENDER = 'DEFENDER'
    MIDFIELDER = 'MIDFIELDER'
    FORWARDER = 'FORWARDER'
    choices = [
        (GOALKEEPER,'Goal Keeper'),
        (DEFENDER,'Defender'),
        (MIDFIELDER,'Midfielder'),
        (FORWARDER,'Forwarder')
    ]
    name = models.CharField(max_length=100)
    photo = VersatileImageField("players",upload_to='players/', null=True, ppoi_field='ppoi')
    ppoi = PPOIField('players PPOI')
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    citizenship = models.CharField(max_length=100)
    kit_number = models.IntegerField()
    position = models.CharField(choices=choices, max_length=100)


    def __str__(self):
        return self.name

class Gallery(models.Model):
    images = VersatileImageField(upload_to='gallery/', null=True)
    date = models.DateTimeField(null=True, default=datetime.now())


    def __str__(self):
        return self.images

class Award(models.Model):
    tournament_name = models.CharField(max_length=500)
    trophy_image = VersatileImageField(upload_to='trophy/', null=True)
    trophy_count = models.IntegerField()


    def __str__(self):
        return self.tournament_name

class SponsorLogo(models.Model):
    sponsors_logo = VersatileImageField(upload_to='sponsors log/', null=True)

    def __str__(self):
        return self.sponsors_logo


class LatestNews(models.Model):
    heading = models.CharField(max_length=500)
    image = VersatileImageField("news_image",upload_to='news/', null=True, ppoi_field='ppoi')
    ppoi = PPOIField('news_image PPOI')
    date = models.DateTimeField(default=datetime.now())
    news_description =models.CharField(max_length=1000, null=True, default="")


    def __str__(self):
        return self.heading

class ProductCategory(models.Model):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    product_image = VersatileImageField(upload_to='products/', null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.product_image


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name