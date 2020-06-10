# Create your models here.
from django.db import models


class Subject(models.Model):
    """学科"""
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=31, verbose_name='名称')
    intro = models.CharField(max_length=511, verbose_name='介绍')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_subject'
        verbose_name_plural = '学科'


class Teacher(models.Model):
    """老师"""
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=15, verbose_name='姓名')
    gender = models.BooleanField(default=True, choices=((True, '男'), (False, '女')), verbose_name='性别')
    birth = models.DateField(null=True, verbose_name='出生日期')
    intro = models.CharField(max_length=511, default='', verbose_name='')
    good_count = models.IntegerField(default=0, verbose_name='好评数')
    bad_count = models.IntegerField(default=0, verbose_name='差评数')
    photo = models.CharField(max_length=255, verbose_name='照片')
    subject = models.ForeignKey(to=Subject, on_delete=models.PROTECT, db_column='sno', verbose_name='所属学科')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_teacher'
        verbose_name_plural = '老师'