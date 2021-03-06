from versatileimagefield.fields import VersatileImageField,PPOIField
from django.db import models
from datetime import  date, datetime


# Create your models here.



class Banner(models.Model):
    top_heading = models.CharField(max_length=100, null=True)
    sub_heading = models.CharField(max_length=100, null=True)
    dscription = models.CharField(max_length=500, null=True)
    # banner_image = models.FileField(upload_to ='banner/', null=True)

    def __str__(self):
        return self.sub_heading

class Tournament(models.Model):
    tournament_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tournament_name

class Matche(models.Model):
    tournament_name = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)
    team1 =models.CharField(max_length=100)
    team2 =models.CharField(max_length=100)
    team1_logo = models.ImageField(upload_to="team_logos/")
    team2_logo = models.ImageField(upload_to="team_logos/")
    match_date = models.DateTimeField(null=True)
    stadium  = models.CharField(max_length=200)
    team1_goals = models.CharField(max_length=100, null=True, default="0")
    team2_goals = models.CharField(max_length=100, null=True, default="0")
    completed = models.BooleanField(default=False)

    


class LastMatchHighlight(models.Model):
    video = models.FileField(upload_to='video/')


    


class TeamPlayer(models.Model):
    GOALKEEPER = 'GOAL KEEPER'
    LEFT_BACK = 'LEFT BACK'
    RIGHT_BACK = 'RIGHT BACK'
    DEFENSIVE_MIDFIELDER = 'DEFENSIVE MIDFIELDER'
    ATTACKING_MIDFIELDER = 'ATTACKING MIDFIELDER'
    CENTER_MIDFIELDER = 'CENTER MIDFIELDER'
    LEFT_WING_FORWARD = 'LEFT WING FORWARD'
    RIGHT_WING_FORWARD = 'RIGHT WING FORWARD'
    CENTER_FORWARD = 'CENTER FORWARD'
    choices = [
        (GOALKEEPER,'Goal Keeper'),
        (LEFT_BACK,'Left Back'),
        (RIGHT_BACK,'Right Back'),
        (DEFENSIVE_MIDFIELDER,'Defensive Midfielder'),
        (ATTACKING_MIDFIELDER,'Attacking Midfielder'),
        (CENTER_MIDFIELDER,'Center Midfielder'),
        (LEFT_WING_FORWARD,'Left Wing Forward'),
        (RIGHT_WING_FORWARD,'Right Wing Forward'),
        (CENTER_FORWARD,'Center Forward')
    ]
    category_choice = [
        ('under 12','under 12'),
        ('under 13','under 13'),
        ('under 15','under 15'),
        ('under 18','under 18'),
        ('reserve senior','reserve senior')
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=category_choice)
    photo = VersatileImageField("players",upload_to='players/', null=True, ppoi_field='ppoi')
    ppoi = PPOIField('players PPOI')
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    citizenship = models.CharField(max_length=100)
    kit_number = models.IntegerField()
    position = models.CharField(choices=choices, max_length=100)
    club_debut = models.DateField(null=True)
    previous_club = models.CharField(default="", max_length=100)
    present_club = models.CharField(max_length=100 , default='Lamasia FC Kerala')

    def __str__(self):
        return self.name

class Gallery(models.Model):
    images = VersatileImageField(upload_to='gallery/', null=True)

    class Meta:
        verbose_name_plural = ('Gallery')
    

class Award(models.Model):
    tournament_name = models.CharField(max_length=500)
    trophy_image = VersatileImageField(upload_to='trophy/', null=True)
    trophy_count = models.IntegerField()


    

class SponsorLogo(models.Model):
    sponsors_logo = VersatileImageField(upload_to='sponsors log/', null=True)

   


class LatestNews(models.Model):
    heading = models.CharField(max_length=500)
    image = VersatileImageField("news_image",upload_to='news/', null=True, ppoi_field='ppoi')
    ppoi = PPOIField('news_image PPOI')
    date = models.DateTimeField(auto_now_add=True)
    news_description =models.CharField(max_length=1000, null=True, default="")

    class Meta:
        verbose_name_plural = ('Latest news')

    def __str__(self):
        return self.heading

class ProductCategory(models.Model):
    category_name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = ('Product Categories')


    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    product_image = VersatileImageField(upload_to='products/', null=True)
    price = models.IntegerField()

    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=1000)

   


class BoardManagement(models.Model):
    name = models.CharField(max_length=100)
    photo = VersatileImageField("board",upload_to='board management/', null=True, ppoi_field='ppoi')
    ppoi = PPOIField('board PPOI')
    position = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)


class AccademyFee(models.Model):
    category_choice = [
        ('under 12','under 12'),
        ('under 13','under 13'),
        ('under 15','under 15'),
        ('under 18','under 18'),
        ('reserve senior','reserve senior')
    ]
    category = models.CharField(max_length=100, choices=category_choice ,null=True)
    fee = models.IntegerField()

    def __str__(self):
        return self.category