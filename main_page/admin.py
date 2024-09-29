from django.contrib import admin
from django.db import models

from ckeditor.widgets import CKEditorWidget


from .models import Product, Category, \
    PhysChemComponent, PhysChemCompositionSet, \
    ClientRequest, FAQ, AboutCompany, Email, PhoneNumbers, \
    Mission, Achievement, Banner, TopSale, Currency, ProductPhoto, Partner, EngineType, TopSale1

admin.site.site_title = "OIL DRIVE | admin Panel"
admin.site.site_header = "OIL DRIVE"
admin.site.index_title = ""


class RequestAdmin(admin.ModelAdmin):
    list_display = ["email", "added_date", "status"]
    readonly_fields = ["request_text"]


class AchievementInline(admin.StackedInline):
    model = Achievement
    extra = 0
    verbose_name = 'Достижение'
    verbose_name_plural = 'Достижения'


class MissionInline(admin.StackedInline):
    model = Mission
    extra = 0
    verbose_name = 'Миссия'
    verbose_name_plural = 'Миссии'


class AboutCompanyAdmin(admin.ModelAdmin):
    inlines = [AchievementInline, MissionInline]


# Админ-классы для новой структуры
class PhysChemComponentInline(admin.TabularInline):
    model = PhysChemComponent
    extra = 1


class PhysChemCompositionSetInline(admin.TabularInline):
    model = PhysChemCompositionSet
    verbose_name = 'Физико-химическое свойство'
    verbose_name_plural = 'Физико-химические свойства'
    extra = 1
    # inlines = [PhysChemComponentInline, ]


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhysChemCompositionSetInline, ProductPhotoInline]
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.register(Category)
admin.site.register(TopSale)
admin.site.register(TopSale1)
admin.site.register(Currency)
admin.site.register(FAQ)
admin.site.register(Email)
admin.site.register(PhoneNumbers)
admin.site.register(Partner)
admin.site.register(EngineType)
admin.site.register(Banner)
admin.site.register(Product, ProductAdmin)
admin.site.register(AboutCompany, AboutCompanyAdmin)
admin.site.register(ClientRequest, RequestAdmin)

