from django.db import models


class UnderDevelopment(models.Model):
    main_text_ru = models.CharField(max_length=255, verbose_name='Основной текст (RU)')
    main_text_en = models.CharField(max_length=255, verbose_name='Основной текст (EN)')
    main_text_uz = models.CharField(max_length=255, verbose_name='Основной текст (UZ)')

    def __str__(self):
        return self.main_text_ru
