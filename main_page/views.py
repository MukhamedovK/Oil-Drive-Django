from datetime import datetime

from django.shortcuts import render, redirect
from django.utils import translation
from telebot import TeleBot

from cms.models import UnderDevelopment
from .models import Product, Category, \
    Feedback, ClientRequest, FAQ, AboutCompany, Email, PhoneNumbers, Banner, TopSale, Currency, Partner
from .utils import add_product_to_seen, send_google_sheets, create_lid

bot = TeleBot('6813417526:AAG7_jph1kByWrU2g6KOoQpSpq3za2V8BPA')


# Страница заглушка
def main_page_u_d(request, language='uz'):
    translation.activate(language)
    main_texts = UnderDevelopment.objects.first()

    return render(request, 'index.html', {'lang': language,
                                          'main_texts': main_texts})


def main_page_(request):
    return redirect('/main_page/uz')


# Главная страница
def main_page(request, language='uz'):
    translation.activate(language)

    if_search = request.GET.get('search')

    feedbacks = Feedback.objects.all()
    partners = Partner.objects.all()
    categories = Category.objects.all().order_by('category_name')
    contacts = PhoneNumbers.objects.all()
    address = AboutCompany.objects.all()[0].address
    banners = Banner.objects.all()
    faq = FAQ.objects.all()
    top_products = Product.objects.filter(products__id=1)
    top_sale = Product.objects.filter(product_sale__id=1)
    new_product = Product.objects.filter(status=True).order_by('id').last()
    currency_rate = Currency.objects.all()[0].currency_rate
    partners = Partner.objects.all()

    have_seen = request.session.get('have_seen')

    # print(categories)
    if if_search is None:
        return render(request, 'oil/index.html', {'lang': language,
                                                  'banners': banners,
                                                  'categories': categories,
                                                  'address': address,
                                                  'contacts': contacts,
                                                  'faqs': faq,
                                                  'top_products': top_products,
                                                  'top_sale': top_sale,
                                                  'currency_rate': currency_rate,
                                                  'feedbacks': feedbacks,
                                                  'partners': partners,
                                                  'new_product': new_product,
                                                  })

    products = Product.objects.filter(name__contains=if_search.upper())

    return render(request, 'oil/catalog.html',
                  {'lang': language,
                   'catalog_items': products,
                   'categories': categories,
                   'category_name': if_search,
                   'have_seen': have_seen,
                   'address': address,
                   'top_sale': top_sale,
                   'contacts': contacts,
                   'currency_rate': currency_rate,
                   'partners': partners
                   }
                  )


# Отображение всего каталога
def catalog_page(request, language='ru'):
    translation.activate(language)
    if_exact = request.GET.get('category')
    if_exact_partner = request.GET.get('brand')
    have_seen = request.session.get('have_seen')

    categories = Category.objects.all().order_by('category_name')
    contacts = PhoneNumbers.objects.all()
    address = AboutCompany.objects.all()[0].address
    currency_rate = Currency.objects.all()[0].currency_rate
    partners = Partner.objects.all()

    if if_exact is None and if_exact_partner is None:
        catalog_items = Product.objects.filter(status=True).order_by('name')

    else:
        if if_exact and if_exact_partner:
            catalog_items = Product.objects.filter(category__category_name=if_exact,
                                                   partner__partner_name=if_exact_partner)

        elif if_exact_partner:
            catalog_items = Product.objects.filter(
                                                   partner__partner_name=if_exact_partner)

        else:
            catalog_items = Product.objects.filter(category__category_name=if_exact)

    return render(request, 'oil/catalog.html', {'lang': language,
                                                'catalog_items': catalog_items,
                                                'categories': categories,
                                                'category_name': if_exact or 'Каталог',
                                                'have_seen': have_seen,
                                                'address': address,
                                                'contacts': contacts,
                                                'currency_rate': currency_rate,
                                                'partners': partners,
                                                })


# Страница определенного продукта
def exact_product_page(request, pr_id, language='ru'):
    translation.activate(language)
    exact_product = Product.objects.filter(id=pr_id)
    have_seen = add_product_to_seen(request, exact_product)

    categories = Category.objects.all().order_by('category_name')
    contacts = PhoneNumbers.objects.all()
    address = AboutCompany.objects.all()[0].address
    currency_rate = Currency.objects.all()[0].currency_rate

    if exact_product:
        return render(request, 'oil/exact-product.html', {'lang': language,
                                                          'product': exact_product[0],
                                                          'categories': categories,
                                                          'have_seen': have_seen,
                                                          'address': address,
                                                          'contacts': contacts,
                                                          'currency_rate': currency_rate
                                                          })

    return render(request, 'oil/exact-product.html',
                  {'lang': language,
                   'categories': categories,
                   'have_seen': have_seen,
                   'address': address,
                   'contacts': contacts,
                   'currency_rate': currency_rate
                   })


# Обработка формы для заявок
def get_form_data(request, language='ru'):
    translation.activate(language)
    if request.method == 'POST':
        full_name = request.POST.get('fio')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        from_form = request.GET.get('from')

        new_feedback = ClientRequest(full_name=full_name,
                                     phone_number=phone_number,
                                     email=email,
                                     request_text=comment,
                                     status='new')

        new_feedback.save()

        bot.send_message(chat_id=-4210526850,
                         parse_mode='HTML',
                         text=f"<b>Новая заявка</b> #{new_feedback.pk}\n\n"
                              f"<b>Имя:</b> {full_name}\n"
                              f"<b>Номер телефона:</b> {phone_number}\n"
                              f"<b>Почта:</b> {email}\n\n"
                              f"<b>Комментарий:</b> {comment}\n"
                              f"<b>Откуда:</b> {from_form}\n"
                              f"<b>Дата:</b> {datetime.strftime(datetime.now(), '%d %B %Y %H:%M:%S')}")

        # send_google_sheets(new_feedback.pk, full_name, phone_number,
        #                    email, comment, datetime.now())
        create_lid(client_name=full_name,
                   phone_number=phone_number,
                   email=email)

        return redirect(f'/main_page/{language}', status=302)


# Страница контактов
def contacts_page(request, language='uz'):
    translation.activate(language)
    # main_texts = UnderDevelopment.objects.first()
    contacts = PhoneNumbers.objects.filter(status=True).all()
    address = AboutCompany.objects.all()[0].address
    emails = Email.objects.filter(status=True).all()

    return render(request, 'oil/contacts.html', {'lang': language,
                                                 'main_texts': 'main_texts',
                                                 'address': address,
                                                 'contacts': contacts,
                                                 'emails': emails,
                                                 })


# Страница О компании
def about_page(request, language='uz'):
    translation.activate(language)
    about = AboutCompany.objects.all()[0]
    contacts = PhoneNumbers.objects.all()

    return render(request, 'oil/about.html', {'lang': language,
                                              'main_texts': 'main_texts',
                                              'about': about,
                                              'address': about.address,
                                              'contacts': contacts,
                                              })


def production_page(request, language='uz'):
    translation.activate(language)
    about = AboutCompany.objects.all()[0]
    contacts = PhoneNumbers.objects.all()
    partners = Partner.objects.all()

    return render(request, 'oil/production.html', {'lang': language,
                                                   'main_texts': 'main_texts',
                                                   'about': about,
                                                   'address': about.address,
                                                   'contacts': contacts,
                                                   'partners': partners,
                                                   })
