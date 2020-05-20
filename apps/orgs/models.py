from django.db import models
from datetime import datetime


# 城市模型类.
class CityInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市名称')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name


# 机构模型类
class OrgInfo(models.Model):
    image = models.ImageField(upload_to='org/', max_length=200, verbose_name='机构封面')
    name = models.CharField(max_length=20, verbose_name='机构名称')
    course_num = models.IntegerField(default=0, verbose_name='课程数')
    study_num = models.IntegerField(default=0, verbose_name='学习人数')
    address = models.CharField(max_length=20, verbose_name='机构地址')
    desc = models.CharField(max_length=200, verbose_name='机构简介')
    detail = models.TextField(verbose_name='机构详情')
    love_num = models.IntegerField(default=0, verbose_name='收藏数')
    click_num = models.IntegerField(default=0, verbose_name='访问量')
    category = models.IntegerField(choices=((0, '培训机构'), (1, '高校'), (2, '个人')), verbose_name='机构类别')
    cityinfo = models.ForeignKey(CityInfo, verbose_name='所属城市', on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机构信息'
        verbose_name_plural = verbose_name


# 教师模型类
class TeacherInfo(models.Model):
    image = models.ImageField(upload_to='teacher/', max_length=200, verbose_name='教师头像')
    name = models.CharField(max_length=50, verbose_name='教师名称')
    auth = models.IntegerField(choices=((0, '普通讲师'), (1, '高级讲师'), (2, '金牌讲师')), verbose_name='认证类型', default=0)
    work_year = models.IntegerField(default=0, verbose_name='工作年限')
    work_position = models.IntegerField( verbose_name='工作职位')
    work_company = models.ForeignKey(OrgInfo, verbose_name='所属机构', on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name='教师年龄')
    work_style = models.CharField(max_length=200, verbose_name='教学特点')
    gender = models.CharField(choices=(('boy', '男'), ('girl', '女')), max_length=10, verbose_name='教师性别', default='boy')
    love_num = models.IntegerField(default=0, verbose_name='收藏量')
    click_num = models.IntegerField(default=0, verbose_name='访问量')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name
