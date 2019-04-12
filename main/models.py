from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=120, verbose_name='Company name')
    quote = models.IntegerField(verbose_name='Quote traffic')

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=120, verbose_name='First name')
    last_name = models.CharField(max_length=240, verbose_name='Last name')
    email = models.EmailField(max_length=120, verbose_name='Email')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Company')

    def __str__(self):
        return self.first_name


class Transfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    date = models.DateTimeField(verbose_name='Time')
    resource = models.CharField(max_length=240, verbose_name='Recource', default='http://xxxx.xxx/xx.xx')
    traffic = models.IntegerField(verbose_name='Transfer')
    
    def __str__(self):
        return self.user

