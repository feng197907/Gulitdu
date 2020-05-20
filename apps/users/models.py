from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.
class UserProfile(AbstractUser):
    image = models.ImageField(upload_to='user/', max_length=200, verbose_name='用户头像', null=True, blank=True)
    nick_name = models.CharField(max_length=20, verbose_name='用户昵称', null=True, blank=True)
    birthday = models.DateTimeField(verbose_name='用户生日', null=True, blank=True)
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), max_length=10, verbose_name='用户性别', default='girl')
    address = models.CharField(max_length=200, verbose_name='用户地址', null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name='用户手机', null=True, blank=True)
    email = models.CharField(max_length=50, verbose_name='用户邮箱', null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class BannerInfo(models.Model):
    image = models.ImageField(upload_to='banner/', verbose_name='轮播图', max_length=200)
    url = models.URLField(default='http://www.baidu.com', max_length=200, verbose_name='图片链接')
    title = models.CharField(max_length=200, verbose_name='图片标题', null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


class EmailVerifyDode(models.Model):
    code = models.CharField(max_length=200, verbose_name='邮箱验证码')
    email = models.EmailField(max_length=50, verbose_name='验证码邮箱')
    send_type = models.IntegerField(choices=((1, 'register'), (2, 'forget'), (3, 'change')),verbose_name='验证码类型')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '验证码邮箱信息'
        verbose_name_plural = verbose_name

