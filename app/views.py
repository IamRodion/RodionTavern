from typing import Any
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.db.models import OuterRef, Subquery, Case, When, IntegerField, F
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Trade, User, Item

#----------------------Login----------------------

class LoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())

        next_url = self.request.GET.get('next')
        if next_url:
            return redirect(next_url)
        else: 
            return redirect('home')

    def form_invalid(self, form):
        messages.error(self.request, 'User or Password incorrect')
        return super().form_invalid(form)

#----------------------Logout----------------------
class LogoutView(LoginRequiredMixin, LogoutView):
    def get(self, request):
        logout(request)
        return redirect('home')

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
            User.objects.filter(id=OuterRef('user_id')).values('first_name')[:1] 
        )
    )
    trades = trades.annotate(
        item_name=Subquery(
            Item.objects.filter(id=OuterRef('item_id')).values('name')[:1]
        )
    )

    return trades

#----------------------New Trade----------------------
class NewTradeView(LoginRequiredMixin, ListView):
  template_name = 'new_trade.html'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
     context = super().get_context_data(**kwargs)
     context['title'] = "New Trade"
     return context

  def get_queryset(self):
    items = Item.objects.all()
    return items


#----------------------Users----------------------
class UserView(LoginRequiredMixin, ListView):
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
            User.objects.filter(id=OuterRef('user_id')).values('first_name')[:1]
        )  
    )

    trades = trades.annotate(
        item_icon=Subquery(
            Item.objects.filter(id=OuterRef('item_id')).values('icon')[:1]
        ),
        item_level=Subquery(
            Item.objects.filter(id=OuterRef('item_id')).values('level')[:1]
        ),
        item_name=Subquery(
            Item.objects.filter(id=OuterRef('item_id')).values('name')[:1]
        ),
        # item_armour=Subquery(
        #     Item.objects.filter(id=OuterRef('item_id')).values('armour')[:1]
        # ),

        armour=Case(
            When(bonus_1="Fortified", then=F('item__armour') + F('item__level') / 10),
            When(bonus_2="Fortified", then=F('item__armour') + F('item__level') / 10),
            default=F('item__armour'),
            output_field=IntegerField(),
        ),

        item_primary_stat=Subquery(
            Item.objects.filter(id=OuterRef('item_id')).values('primary_stat')[:1]
        ),
        item_stamina=Subquery(
            Item.objects.filter(id=OuterRef('item_id')).values('stamina')[:1]
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