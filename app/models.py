from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Item(models.Model):
    PRIM_STAT_CHOICES = [
        ('Magic', 'Magic'),
        ('Distance', 'Distance'),
        ('Melee', 'Melee')
    ]
    SEC_STAT_CHOICES = [
        ("['Spirit', 'Defense', 'Magic']", 'Secondary and Magic'),
        ("['Spirit', 'Defense', 'Distance']", 'Secondary and Distance'),
        ("['Spirit', 'Defense', 'Mele']", 'Secondary and Mele')
    ]
    BONUS_CHOICES = [
        ("['HP Regen', 'Mana Regen', 'Potion Bonus', 'Leech', 'Money Find', 'Thorns', 'Omni Resist', 'Fortified', 'Empowered', 'Crit Chance']", 'Magic Bonuses'),
        ("['HP Regen', 'Mana Regen', 'Potion Bonus', 'Leech', 'Money Find', 'Thorns', 'Omni Resist', 'Fortified', 'Empowered', 'Accuracy']", 'Distance Bonuses'),
        ("['HP Regen', 'Mana Regen', 'Potion Bonus', 'Leech', 'Money Find', 'Thorns', 'Omni Resist', 'Fortified', 'Empowered', 'Block %']", 'Mele Bonuses')
    ]

    id = models.AutoField(primary_key=True)
    icon = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    armour = models.IntegerField()
    level = models.IntegerField()
    primary_stat = models.CharField(max_length=10, choices=PRIM_STAT_CHOICES)
    max_amount_primary_stat = models.IntegerField()
    secondary_stat = models.TextField(max_length=40, choices=SEC_STAT_CHOICES)
    max_amount_secondary_stat = models.IntegerField()
    bonus = models.TextField(max_length=200, choices=BONUS_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.primary_stat} level {self.level})"

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

    def __str__(self):
        return f"{self.item} ({self.user} @ {self.price})"