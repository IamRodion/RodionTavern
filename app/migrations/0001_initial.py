# Generated by Django 4.0.6 on 2023-10-23 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('icon', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('armour', models.IntegerField()),
                ('primary_stat', models.CharField(choices=[('Magic', 'Magic'), ('Distance', 'Distance'), ('Melee', 'Melee')], max_length=10)),
                ('max_amount_primary_stat', models.IntegerField()),
                ('secondary_stat', models.CharField(choices=[('Spirit', 'Spirit'), ('Defense', 'Defense'), ('Magic', 'Magic'), ('Distance', 'Distance'), ('Melee', 'Melee')], max_length=10)),
                ('max_amount_secondary_stat', models.IntegerField()),
                ('bonus', models.CharField(choices=[('HP Regen', 'HP Regen'), ('Mana Regen', 'Mana Regen'), ('Potion Bonus', 'Potion Bonus'), ('Leech', 'Leech'), ('Money Find', 'Money Find'), ('Thorns', 'Thorns'), ('Omni Resist', 'Omni Resist'), ('Fortified', 'Fortified'), ('Empowered', 'Empowered'), ('Crit Chance', 'Crit Chance'), ('Accuracy', 'Accuracy'), ('Block %', 'Block %')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount_primary_stat', models.IntegerField()),
                ('secondary_stat', models.CharField(choices=[('Spirit', 'Spirit'), ('Defense', 'Defense'), ('Magic', 'Magic'), ('Distance', 'Distance'), ('Melee', 'Melee')], max_length=10)),
                ('amount_secondary_stat', models.IntegerField()),
                ('bonus', models.CharField(choices=[('HP Regen', 'HP Regen'), ('Mana Regen', 'Mana Regen'), ('Potion Bonus', 'Potion Bonus'), ('Leech', 'Leech'), ('Money Find', 'Money Find'), ('Thorns', 'Thorns'), ('Omni Resist', 'Omni Resist'), ('Fortified', 'Fortified'), ('Empowered', 'Empowered'), ('Crit Chance', 'Crit Chance'), ('Accuracy', 'Accuracy'), ('Block %', 'Block %')], max_length=100)),
                ('elite', models.BooleanField()),
                ('enchant', models.CharField(blank=True, choices=[('Mana', 'Mana'), ('Ice', 'Ice'), ('Nature', 'Nature'), ('Energy', 'Energy'), ('Fire', 'Fire'), ('Physical', 'Physical')], max_length=10, null=True)),
                ('price', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]