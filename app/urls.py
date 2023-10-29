from django.urls import path
from . import views
from .views import HomeView, TradesView, UserView, NewTradeView, LoginView, LogoutView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('trades/', TradesView.as_view(), name='trades'),
    path('user/', UserView.as_view(), name='user'),
    path('new_trade/', NewTradeView.as_view(), name='new_trade'),
    path('json_trades/', views.json_trades, name='json_trades'),
    path('json_items/', views.json_items, name='json_items'),
]