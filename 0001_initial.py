# Generated by Django 5.0.6 on 2024-05-23 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playercategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=20)),
                ('categorydesc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Playerteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=30)),
                ('teamdesc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('runs', models.IntegerField()),
                ('wickets', models.IntegerField()),
                ('Hundreads', models.IntegerField()),
                ('fiftys', models.IntegerField()),
                ('jersyno', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.playercategory')),
                ('teamid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.playerteam')),
            ],
        ),
        migrations.CreateModel(
            name='Playerfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('review', models.TextField()),
                ('Feedback', models.DateField(auto_now_add=True)),
                ('Playerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.player')),
            ],
        ),
    ]
