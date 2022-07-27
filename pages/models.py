from django.db import models
from django.utils.translation import gettext_lazy as _


class BannerModel(models.Model):
    collections = models.CharField(max_length=60, verbose_name=_('collections'))
    title = models.CharField(max_length=60, verbose_name=_('title'))
    description = models.CharField(max_length=100, verbose_name=_('description'))
    image = models.ImageField(upload_to='banner/', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    is_active = models.BooleanField(default=False, blank=True, verbose_name=_('is active'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'


class ContactModel(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'