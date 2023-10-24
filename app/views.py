#from django.http.response import JsonResponse
from typing import Any
#from django.shortcuts import render
from django.db.models import OuterRef, Subquery
from django.views.generic import ListView
from .models import Trade, User, Item

# Create your views here.
# def home(request):
#     return render(request, 'home.html')

# def trades(request):
#     trades = Trade.objects.all()

#     trades = trades.annotate(
#         username=Subquery(
#             User.objects.filter(id=OuterRef('user_id')).values('username')[:1] 
#         )
#     )

#     trades = trades.annotate(
#         item_name=Subquery(
#             Item.objects.filter(id=OuterRef('item_id')).values('name')[:1]
#         )  
#     )

#     context = {
#         'trades': trades
#     }

#     return render(request, 'trades.html', context)

# def users(request):
#     return render(request, 'users.html')


#----------------------Home----------------------
class HomeView(ListView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
     context = super().get_context_data(**kwargs)
     context['title'] = "Home"
     return context

  def get_queryset(self):
    return None
  

#----------------------Trades----------------------
class TradesView(ListView):
  template_name = 'trades.html'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
     context = super().get_context_data(**kwargs)
     context['title'] = "Trades"
     return context

  def get_queryset(self):
    trades = Trade.objects.all()
    trades = trades.annotate(
        username=Subquery(
            User.objects.filter(id=OuterRef('user_id')).values('username')[:1] 
        )
    )
    trades = trades.annotate(
        item_name=Subquery(
            Item.objects.filter(id=OuterRef('item_id')).values('name')[:1]
        )
    )

    return trades


#----------------------Users----------------------
class UsersView(ListView):
  template_name = 'users.html'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
     context = super().get_context_data(**kwargs)
     context['title'] = "Users"
     return context

  def get_queryset(self):
    return None
    #return User.objects.all()