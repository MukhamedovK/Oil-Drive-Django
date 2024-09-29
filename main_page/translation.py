from modeltranslation.translator import register, TranslationOptions
from .models import Product, Category, Banner, EngineType, AboutCompany, Achievement, Mission


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description', 'advantages', 'kachestvo', )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('banner_text', 'banner_button',)


@register(EngineType)
class EngineTypeTranslationOptions(TranslationOptions):
    fields = ('type_name',)


@register(AboutCompany)
class AboutCompanyTranslationOptions(TranslationOptions):
    fields = ('main_about', 'history', 'address')


@register(Achievement)
class AboutCompanyTranslationOptions(TranslationOptions):
    fields = ('title', 'little_text',)


@register(Mission)
class AboutCompanyTranslationOptions(TranslationOptions):
    fields = ('little_text', )

