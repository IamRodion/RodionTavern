from django.db import models
from django.utils.html import format_html

colors = {
    'Magic': '#FFA500',
    'Distance': '#FF69B4',
    'Melee': '#00FFFF',
    'Spirit': '#87CEEB',
    'Defense': '#FFFFFF',
    'Elite': '#FFD700'
}

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Item(models.Model):
    SLOT_CHOICES = [
        ('Helmet', 'Helmet'),
        ('Chest', 'Chest'),
        ('Gloves', 'Gloves'),
        ('Boots', 'Boots')
    ]

    PRIM_STAT_CHOICES = [
        ('Magic', 'Magic'),
        ('Distance', 'Distance'),
        ('Melee', 'Melee')
    ]
    SEC_STAT_CHOICES = [
        ("['Spirit', 'Defense', 'Magic']", 'Secondary and Magic'),
        ("['Spirit', 'Defense', 'Distance']", 'Secondary and Distance'),
        ("['Spirit', 'Defense', 'Melee']", 'Secondary and Melee')
    ]
    BONUS_CHOICES = [
        ("['HP Regen', 'Mana Regen', 'Potion Bonus', 'Leech', 'Money Find', 'Thorns', 'Omni Resist', 'Fortified', 'Empowered', 'Crit Chance']", 'Magic Bonuses'),
        ("['HP Regen', 'Mana Regen', 'Potion Bonus', 'Leech', 'Money Find', 'Thorns', 'Omni Resist', 'Fortified', 'Empowered', 'Accuracy']", 'Distance Bonuses'),
        ("['HP Regen', 'Mana Regen', 'Potion Bonus', 'Leech', 'Money Find', 'Thorns', 'Omni Resist', 'Fortified', 'Empowered', 'Block %']", 'Melee Bonuses')
    ]

    id = models.AutoField(primary_key=True)
    icon = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    slot = models.CharField(max_length=10, choices=SLOT_CHOICES)
    armour = models.PositiveSmallIntegerField()
    level = models.IntegerField()
    primary_stat = models.CharField(max_length=10, choices=PRIM_STAT_CHOICES)
    max_amount_primary_stat = models.PositiveSmallIntegerField()
    stamina = models.PositiveSmallIntegerField()
    secondary_stat = models.TextField(max_length=40, choices=SEC_STAT_CHOICES)
    max_amount_secondary_stat = models.PositiveSmallIntegerField()
    bonus = models.TextField(max_length=200, choices=BONUS_CHOICES)

    def __str__(self):
        return f"{self.name}"

    def primary_stat_colored(self):
        return format_html(f'<span style="color: {colors[self.primary_stat]};">{self.primary_stat}</span>')
        
    primary_stat_colored.short_description = "Primary"
    #class_item.admin_order_field = "name"

class Trade(models.Model):
    SEC_STAT_CHOICES = [
        ('Spirit', 'Spirit'),
        ('Defense', 'Defense'),
        ('Magic', 'Magic'),
        ('Distance', 'Distance'),
        ('Melee', 'Melee')
    ]

    BONUS_CHOICES = [
        ('HP Regen', 'HP Regen'),
        ('Mana Regen', 'Mana Regen'),
        ('Potion Bonus', 'Potion Bonus'),
        ('Leech', 'Leech'),
        ('Money Find', 'Money Find'),
        ('Thorns', 'Thorns'),
        ('Omni Resist', 'Omni Resist'),
        ('Fortified', 'Fortified'),
        ('Empowered', 'Empowered'),
        ('Crit Chance', 'Crit Chance'),
        ('Accuracy', 'Accuracy'),
        ('Block %', 'Block %')
    ]

    ENCHANT_CHOICES = [
        ('Mana', 'Mana'),
        ('Ice', 'Ice'),
        ('Nature', 'Nature'),
        ('Energy', 'Energy'),
        ('Fire', 'Fire'),
        ('Physical', 'Physical')
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount_primary_stat = models.IntegerField()
    secondary_stat = models.CharField(max_length=40, choices=SEC_STAT_CHOICES)
    amount_secondary_stat = models.IntegerField()
    bonus_1 = models.CharField(max_length=100, choices=BONUS_CHOICES)
    bonus_2 = models.CharField(max_length=100, choices=BONUS_CHOICES)
    elite = models.BooleanField()
    enchant = models.CharField(max_length=10, choices=ENCHANT_CHOICES, null=True, blank=True)
    price = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.item} ({self.user} @ {self.price})"

    # def armour_fortified(self):
    #     if 'Fortified' in (self.bonus_1, self.bonus_2):
    #         return (self.item.level//10) + self.item.armour
    #     else:
    #         return self.item.armour

    def item_colored(self):
        if self.elite:
            return format_html(f'<span style="color: #FFD700;">{self.item.name}</span>')
        else:
            return f'{self.item.name}'

    item_colored.short_description = "Item"

    def primary_stat_colored(self):
        return format_html(f'<span style="color: {colors[self.item.primary_stat]};">{self.item.primary_stat} {self.amount_primary_stat} ({self.item.max_amount_primary_stat})</span>')
    
    primary_stat_colored.short_description = "Primary"

    def secondary_stat_colored(self):
        return format_html(f'<span style="color: {colors[self.secondary_stat]};">{self.secondary_stat} {self.amount_secondary_stat} ({self.item.max_amount_secondary_stat if self.secondary_stat == self.item.primary_stat else (self.item.max_amount_secondary_stat*2)})</span>')
        
    secondary_stat_colored.short_description = "Secondary"