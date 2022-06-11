from django.urls import path

from . import views


urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about,name='about'),
    path('board-management', views.board_management, name='board-management'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    path('club', views.club, name='club'),
    path('sponsors', views.sponsors, name='sponsors'),
    path('team', views.team, name='team'),
    path('gallery', views.gallery, name='gallery'),
    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('player_profile/<str:player_id>',views.player_profile,name='player_profile')

]
