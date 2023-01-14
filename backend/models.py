from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from PIL import Image
from django.utils import timezone


# ===========================================================================
class Profile(models.Model):
    ROLES = (
        ('A', 'Администратор'),
        ('D', 'Директор'),
        ('T', 'Тренер'),
        ('S', 'Студент'),
    )
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    role = models.CharField(verbose_name='Роль', max_length=1, choices=ROLES)
    surname = models.CharField(verbose_name='Фамилия', max_length=64, blank=True)
    name = models.CharField(verbose_name='Имя', max_length=64, blank=True)
    soname = models.CharField(verbose_name='Отчество', max_length=64, blank=True)
    phone = models.BigIntegerField(verbose_name='Номер телефона', unique=True, blank=True)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='avatars/', default='/no-image.png')
    tgID = models.IntegerField(verbose_name='Телеграм', unique=True, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    registered_at = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)

    # ТОЛЬКО для тренера:
    wage = models.IntegerField(verbose_name='Оклад', null=True, blank=True)
    cost = models.IntegerField(verbose_name='Ставка за групповое занятие', null=True, blank=True)
    cost_individual = models.IntegerField(verbose_name='Ставка за индивидуальное занятие', null=True, blank=True)
    cost_for_student = models.IntegerField(verbose_name='Стоимость индив. для студента', null=True, blank=True)

    # ТОЛЬКО для Студента:
    agent_name = models.CharField(verbose_name='Имя представителя', max_length=128, null=True, blank=True)
    agent_phone = models.CharField(verbose_name='Телефон представителя', max_length=16, null=True, blank=True)
    is_deleted = models.BooleanField(verbose_name='Удален', default=False)
    is_deleted_at = models.DateTimeField(verbose_name='Дата удаления', blank=True, null=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.soname} ({self.role})'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        try:
            filepath = self.avatar.path
            img = Image.open(filepath)
            if img.width > img.height:
                dist = int((img.width - img.height) / 2)
                cropped = img.crop((dist, 0, img.width - dist, img.height))
            else:
                dist = int((img.height - img.width) / 2)
                cropped = img.crop((0, dist, img.width, img.height - dist))
            cropped.save(filepath)
        except:
            pass

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        ordering = ['surname']

