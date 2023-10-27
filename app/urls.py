from django.urls import path
from . import views
from .views import HomeView, TradesView, UsersView, NewTradeView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('trades/', TradesView.as_view(), name='trades'),
    path('users/', UsersView.as_view(), name='users'),
    path('new_trade/', NewTradeView.as_view(), name='new_trade'),
    path('json_trades/', views.json_trades, name='json_trades'),
    path('json_items/', views.json_items, name='json_items'),

]