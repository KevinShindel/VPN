# Generated by Django 2.2 on 2019-04-10 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190410_0708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Time')),
                ('resource', models.CharField(max_length=240, verbose_name='Recource')),
                ('traffic', models.IntegerField(verbose_name='Transfer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User', verbose_name='User')),
            ],
        ),
        migrations.DeleteModel(
            name='Abuses',
        ),
    ]
