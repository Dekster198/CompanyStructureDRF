from django.db import models


# Create your models here.
class Employee(models.Model):
    fio = models.CharField(max_length=255, blank=False, db_index=True, unique=True, verbose_name='ФИО')
    photo = models.ImageField(upload_to='photos/', default='photos/default_photo.jpg', verbose_name='Фото')
    post = models.CharField(max_length=64, blank=False, verbose_name='Должность')
    salary = models.IntegerField(blank=False, verbose_name='Зарплата')
    age = models.IntegerField(blank=False, verbose_name='Возраст')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Департамент')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.fio


class Department(models.Model):
    title = models.CharField(max_length=128, blank=False, verbose_name='Название')
    email = models.EmailField(blank=False, verbose_name='Связь с сотрудником - директором департамента')

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return self.title
