# -*- coding: utf-8 -*-

from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User, UserManager
import os

__author__ = 'Murad Gasanov'


class CashierSupervisor(User):
    def get_upload_folder(self, filename):
        return os.path.join(
            "profile", "id%d" % self.id, filename)
    patr = models.CharField(max_length=30)  # Отчество
    tel = models.CharField(max_length=20)
    imei = models.CharField(max_length=20)
    image = models.ImageField(upload_to=get_upload_folder, default="default.png", max_length=500)
    objects = UserManager()


@receiver(models.signals.post_delete, sender=CashierSupervisor)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Удалить файл при удаление соответствуюшей записи из БД
    """
    if instance.image:
        if instance.image.name != "default.png":
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=CashierSupervisor)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Удалить файл при изменение соответствуюшей записи из БД
    """
    if not instance.pk:
        return False
    try:
        old_file = CashierSupervisor.objects.get(pk=instance.pk).image
        if old_file.name != "default.png" and old_file.name != instance.image.name:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except CashierSupervisor.DoesNotExist:
        return False


class Sub(models.Model):
    personal_account = models.CharField(max_length=20)  # Номер счета
    counter_number = models.CharField(max_length=20)  # Номер счетчика


class CounterData(models.Model):
    def get_upload_folder(self, filename):
        return os.path.join(
            "counter", "%Y%m", "%d" % self.id, filename)
    date = models.DateField(null=True)
    ln = models.FloatField(default=0, null=True)  # Долгота
    lt = models.FloatField(default=0, null=True)  # Широта
    counter_foto = models.ImageField(
        upload_to=get_upload_folder, default="default.png", max_length=500)
    home_foto = models.ImageField(
        upload_to=get_upload_folder, default="default.png", max_length=500)
    disturb_foto = models.ImageField(
        upload_to=get_upload_folder, default="default.png", max_length=500)
    additional1_foto = models.ImageField(
        upload_to=get_upload_folder, default="default.png", max_length=500)
    additional2_foto = models.ImageField(
        upload_to=get_upload_folder, default="default.png", max_length=500)
    sub = models.ForeignKey(Sub)
    cashier_supervisor = models.ForeignKey(CashierSupervisor)