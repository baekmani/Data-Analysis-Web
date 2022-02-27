from django.db import models

# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=64, verbose_name = '닉네임')
    email = models.CharField(max_length=64, verbose_name = '이메일')
    password = models.CharField(max_length=64, verbose_name = '비밀번호')

    class Meta:
        db_table = 'account'
        app_label = 'start'
        ordering = ['id']
        managed = False

    def __str__(self):
        return '@@@' + self.name