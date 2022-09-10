from django.db.models import Model
from modeltranslation.translator import TranslationOptions, register
from .models import ProductModel


@register(ProductModel)
class ProductModelTranslationOptions(TranslationOptions):
    fields = ['title', 'short_description', 'long_description', ]
