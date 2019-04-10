# Generated by Django 2.2 on 2019-04-10 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Company name')),
                ('quote', models.IntegerField(max_length='5', verbose_name='Quote traffic')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120, verbose_name='First name')),
                ('last_name', models.CharField(max_length=240, verbose_name='Last name')),
                ('email', models.EmailField(max_length=120, verbose_name='Email')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Company', verbose_name='Company')),
            ],
        ),
    ]