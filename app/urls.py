from django.urls import path

from . import views


urlpatterns = [
    path('',views.index, name="index"),
    path('history',views.history,name='about'),
    path('board-management', views.board_management, name='board-management'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    path('club', views.club, name='club'),
    path('sponsors', views.sponsors, name='sponsors'),
    path('team/reserve-senior', views.reserve_senior, name='team/reserve-senior'),
    path('team/under-18', views.under_18, name='team/under-18'),
    path('team/under-15', views.under_15, name='team/under-15'),
    path('team/under-13', views.under_13, name='team/under-13'),
    path('team/under-12', views.under_12, name='team/under-12'),
    path('gallery', views.gallery, name='gallery'),
    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('player_profile/<str:player_id>',views.player_profile,name='player_profile'),
    path('news/<str:news_id>', views.single_news, name='single_news'),
    path('match-fixtures', views.matchFixtures, name='match-fixtures'),
    path('join-now', views.join, name='join-now'),
    path('joinacademy', views.joinacademy, name='joinacademy'),
    path('registration', views.registration, name='registration'),
    

]
