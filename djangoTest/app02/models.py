from django.db import models

# Create your models here.
'''
# Django 1.7 及以上的版本需要用以下命令
python3 manage.py makemigrations
python3 manage.py migrate
'''

class Business(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32,null=True,default='SA')

class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    # protocol Accepted values are 'both' (default), 'IPv4' or 'IPv6'.
    ip = models.GenericIPAddressField(protocol='IPv4')
    port = models.IntegerField()
    b = models.ForeignKey(to='Business',to_field='id')

class Appliction(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField('Host')
