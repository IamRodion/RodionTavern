from django.urls import path
from .views import HomeView, TradesView, UsersView

# urlpatterns=[
#     path('', views.home, name='home'),
#     path('trades/', views.trades, name='trades'),
#     path('users/', views.users, name='users')
# ]

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('trades/', TradesView.as_view(), name='trades'),
    path('users/', UsersView.as_view(), name='users')
]