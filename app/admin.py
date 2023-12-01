from django.contrib import admin
from .models import Item, Trade
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# admin.site.register(User)
# admin.site.register(Item)
# admin.site.register(Trade)

admin.site.unregister(User)
@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('username', 'email')
    ordering = ('id',)
    search_fields = ('username', 'email')


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'username')
#     list_display_links = ('name', 'username')
#     ordering = ('id',)
#     search_fields = ('name', 'username')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('level', 'name', 'primary_stat_colored', 'slot')
    list_display_links = ('name',)
    list_filter = ('slot', 'primary_stat', 'level')
    list_per_page = 22 # 132 divisores = 1,2,3,4,6,11,12,22,33,44,66,132
    ordering = ('level', 'primary_stat')
    search_fields = ('name', 'primary_stat', 'slot')
    exclude = ('icon', )

    # def datos(self, obj):
    #     return obj.name.upper()
    
    # datos.short_description = "Dato"
    # datos.empty_value_display = "Vacío"
    # datos.admin_order_field = "name"


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_colored', 'user', 'primary_stat_colored', 'secondary_stat_colored', 'enchant', 'price', 'date')
    list_display_links = ('id',)
    list_filter = ('user', 'date')
    ordering = ('id', 'date', 'user')
    search_fields = ('user__first_name', 'item__name') #item, item_id, price, secondary_stat, user, user_id search_fields = ['foreignkeyfield__name']