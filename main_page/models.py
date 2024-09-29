from django.db import models


class EngineType(models.Model):
    type_name = models.CharField(max_length=335, verbose_name='Вид двигателя')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "Вид двигателя"
        verbose_name_plural = "📥 Виды двигателей"


class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='Название категории')
    category_photo = models.ImageField(verbose_name='Фото к категории', upload_to='media')

    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "🔋 Категории"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    status = models.BooleanField(default=True, verbose_name="Активность товара", null=True, blank=True)
    # photo = models.ImageField(upload_to='products_photos/', verbose_name="Фото")
    description = models.TextField(verbose_name="Описание")
    count = models.IntegerField(verbose_name="Количество", null=True, blank=True)
    # volumes = models.CharField(max_length=255, verbose_name="Объемы")
    specifications = models.CharField(max_length=255, verbose_name="Спецификации")
    kachestvo = models.CharField(max_length=255, verbose_name="Уровень качества", null=True, blank=True)
    engine = models.ManyToManyField(EngineType, verbose_name="Вид двигателя")
    advantages = models.TextField(verbose_name="Преимущества")
    color = models.CharField(max_length=100, verbose_name="Цвет", null=True, blank=True)
    file = models.FileField(verbose_name="Техническое описание", null=True, blank=True, upload_to='media/tex')
    partner = models.ForeignKey('Partner', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Бренд')
    sae_status = models.CharField(max_length=255, verbose_name="Вязкость", null=True, blank=True)
    line = models.CharField(max_length=255, verbose_name="Линейка", null=True, blank=True)
    use_type = models.CharField(max_length=255, verbose_name="Область применения", null=True, blank=True)

    # price = models.FloatField(verbose_name="Цена", null=True, blank=True)

    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "🛢 Продукты"


class PhysChemCompositionSet(models.Model):
    product = models.ForeignKey(Product, related_name='composition_sets', on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=255, name='Название', null=True, blank=True)  # Например, можно дать название набору
    description = models.CharField(max_length=255, verbose_name="Требования", null=True, blank=True)
    test_result = models.CharField(max_length=255,
                                   verbose_name="Результаты анализа",
                                   null=True, blank=True)

    def __repr__(self):
        return "Физико-химический состав"


class ProductPhoto(models.Model):
    volume = models.CharField(max_length=255, verbose_name='Обьем')
    volume_photo = models.ImageField(max_length=255, verbose_name='Фото (202x250)px')
    volume_price = models.FloatField(verbose_name='Цена', null=True, blank=True)
    product = models.ForeignKey(Product, related_name='volume_photos', on_delete=models.CASCADE)

    first = models.BooleanField(default=False, verbose_name='Показать по умолчанию')

    def __repr__(self):
        return "Обьемы и их фото"


class PhysChemComponent(models.Model):
    composition_set = models.ForeignKey(PhysChemCompositionSet, related_name='components', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class MainPage(models.Model):
    banner = models.BooleanField(verbose_name='Баннер на главной странице')
    contacts = models.BooleanField(verbose_name='Блок с контактами')
    category_block = models.BooleanField(verbose_name='Блок с категориями')
    hit_of_sell = models.BooleanField(verbose_name='Хиты продаж')
    newsellers = models.BooleanField(verbose_name='Новинки')
    hot_sale = models.BooleanField(verbose_name='Горячие скидки')

    class Meta:
        verbose_name = "Основная страница"

        verbose_name_plural = "📃 Основная страница"


class Banner(models.Model):
    banner_text = models.TextField(verbose_name='Текст к баннеру')
    banner_image = models.ImageField(verbose_name='Фото', upload_to='media')
    banner_button = models.CharField(max_length=255, verbose_name='Текст кнопки')
    banner_button_link = models.CharField(max_length=255, verbose_name='Ссылка к кнопке')

    def __str__(self):
        return self.banner_text

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "🏞 Баннеры"


class FAQ(models.Model):
    question = models.CharField(max_length=550, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Часто задаваемый вопорс"
        verbose_name_plural = "❓ Часто задаваемые вопорсы"


class Feedback(models.Model):
    client_name = models.CharField(max_length=550, verbose_name='Имя')
    feedback_text = models.TextField(verbose_name='Текст')
    publish_date = models.DateField(verbose_name='Был опубликован')

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "⭐ Отзывы"


class ClientRequest(models.Model):
    full_name = models.CharField(max_length=550, verbose_name='ФИО')
    phone_number = models.CharField(max_length=550, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    request_text = models.TextField(verbose_name='Комментарий')
    status = models.CharField(max_length=255,
                              choices=[
                                  ('new', 'Новый'),
                                  ('done', 'Обработан')
                              ], null=True, blank=True)

    added_date = models.DateTimeField(verbose_name='Был отправлен',
                                      auto_now_add=True,
                                      null=True,
                                      blank=True)

    def __str__(self):
        return f"{self.email} | {self.status}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "🆕 Заявки"


class AboutCompany(models.Model):
    main_about = models.TextField(verbose_name='Краткое описание')
    history = models.TextField(verbose_name='История')
    ages = models.CharField(max_length=550, verbose_name='Заголовок для истории')
    history_photo = models.ImageField(max_length=550, verbose_name='Фото для истории (643px X 333px)')
    address = models.CharField(max_length=550, verbose_name='Адрес')
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "О Компании"
        verbose_name_plural = "ℹ️ О Компании"


class Achievement(models.Model):
    title = models.CharField(max_length=225, verbose_name='Заголовок')
    little_text = models.TextField(verbose_name='Краткое описание')
    photo = models.ImageField(upload_to='media')
    about = models.ForeignKey(AboutCompany, on_delete=models.CASCADE,
                              null=True, blank=True,
                              related_name='achievements')

    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Mission(models.Model):
    little_text = models.TextField(verbose_name='Краткое описание')
    photo = models.ImageField(upload_to='media', verbose_name='Фото (245х245)')
    about = models.ForeignKey(AboutCompany, on_delete=models.CASCADE,
                              null=True, blank=True,
                              related_name='missions')

    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.little_text


class PhoneNumbers(models.Model):
    contact_number = models.CharField(max_length=12,
                                      verbose_name='Номер телефона')
    status = models.BooleanField(default=True, verbose_name='Активность')

    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contact_number} | " \
               f"{'Активный' if self.status else 'Неактивный'}"

    class Meta:
        verbose_name = "Номер телефона"
        verbose_name_plural = "☎️ Номера телефонов"


class Email(models.Model):
    email = models.CharField(max_length=120,
                             verbose_name='Почта')
    status = models.BooleanField(default=True, verbose_name='Активность')

    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} | " \
               f"{'Активный' if self.status else 'Неактивный'}"

    class Meta:
        verbose_name = "Почта для связи"
        verbose_name_plural = "📥 Почты для связи"


# Хиты продаж
class TopSale(models.Model):
    products = models.ManyToManyField(Product, related_name='products')

    def __str__(self):
        return f"Хиты продаж"

    class Meta:
        verbose_name = "Хит продаж"
        verbose_name_plural = "📥 Хиты продаж"


# Скидки
class TopSale1(models.Model):
    product_sale = models.ManyToManyField(Product, related_name='product_sale')

    def __str__(self):
        return f"Горячие скидки"

    class Meta:
        verbose_name = "Горячая скидка"
        verbose_name_plural = "📥 Горячие скидки"


# Курс доллара
class Currency(models.Model):
    currency_rate = models.IntegerField(verbose_name='Курс доллара')

    def __str__(self):
        return f"Курс доллара: {self.currency_rate}"

    class Meta:
        verbose_name = "Курс доллара"
        verbose_name_plural = "📥 Курс доллара"


# Партнеры
class Partner(models.Model):
    partner_name = models.CharField(max_length=255, verbose_name='Наименование')
    partner_logo = models.ImageField(verbose_name='Логотип (390x205px)', upload_to='media/partners')
    partner_city = models.ImageField(verbose_name='Флаг производства (43x32px)', upload_to='media/partners')
    partner_url = models.CharField(max_length=255, verbose_name='Ссылка на источник', blank=True, null=True)
    partner_info = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.partner_name

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "📥 Партнеры"


