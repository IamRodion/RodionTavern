from django.http.response import JsonResponse
from typing import Any
#from django.shortcuts import render
from django.db.models import OuterRef, Subquery
from django.views.generic import ListView
from .models import Trade, User, Item


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

#----------------------New Trade----------------------
class NewTradeView(ListView):
  template_name = 'new_trade.html'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
     context = super().get_context_data(**kwargs)
     context['title'] = "New Trade"
     return context

  def get_queryset(self):
    items = Item.objects.all()
    return items


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

#----------------------Trades for Datatable----------------------
def json_trades(_request):
    trades = Trade.objects.values()

    trades = trades.annotate(
        username=Subquery(
            User.objects.filter(id=OuterRef('user_id')).values('username')[:1]
        )  
    )

    trades = trades.annotate(
        item_icon=Subquery(
            Item.objects.filter(id=OuterRef('item_id')).values('icon')[:1]
        ),
        item_name=Subquery(
            Item.objects.filter(id=OuterRef('item_id')).values('name')[:1]
        ),
        item_primary_stat=Subquery(
            Item.objects.filter(id=OuterRef('item_id')).values('primary_stat')[:1]
        )
    )
    trades = list(trades)

    # trades = list(Trade.objects.values())
    data = {'trades': trades}
    return JsonResponse(data)


#----------------------Items for Datatable----------------------
def json_items(_request):
    trades = Item.objects.values()

    trades = list(trades)

    # trades = list(Trade.objects.values())
    data = {'items': trades}
    return JsonResponse(data)