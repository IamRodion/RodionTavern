from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import HomeView, TradesView, UserView, NewTradeView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('accounts/login/', LoginView.as_view(), {'template_name':'login.html'}, name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('trades/', TradesView.as_view(), name='trades'),
    path('user/', login_required(UserView.as_view()), name='user'),
    path('new_trade/', login_required(NewTradeView.as_view()), name='new_trade'),
    path('json_trades/', views.json_trades, name='json_trades'),
    path('json_items/', views.json_items, name='json_items'),

]