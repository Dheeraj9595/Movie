# Generated by Django 5.0.6 on 2024-06-03 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('cinema_id', models.CharField(max_length=30, primary_key='true', serialize=False)),
                ('cinema_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('phoneno', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Puser',
            fields=[
                ('user_id', models.CharField(max_length=30, primary_key='true', serialize=False)),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phoneno', models.CharField(max_length=30)),
                ('bdate', models.DateTimeField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=50)),
                ('movie_details', models.TextField()),
                ('rating', models.IntegerField()),
                ('cinema_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('offer_id', models.AutoField(primary_key=True, serialize=False)),
                ('offer_name', models.CharField(max_length=30)),
                ('offer_details', models.TextField()),
                ('cinema_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('show_id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.CharField(max_length=100)),
                ('seat', models.CharField(max_length=100)),
                ('price_ex', models.IntegerField()),
                ('price_pr', models.IntegerField()),
                ('cinema_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.cinema')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('seat', models.IntegerField()),
                ('price', models.IntegerField()),
                ('offer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.offers')),
                ('show_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.show')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.puser')),
            ],
        ),
        migrations.CreateModel(
            name='TicketOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.offers')),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ticket')),
            ],
        ),
    ]