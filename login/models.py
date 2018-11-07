from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)

    def __str__(self):
        return '<{} {}>'.format(self.name,self.password)
