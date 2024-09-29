from django.urls import path
from .views import main_page, \
    main_page_, main_page_u_d, exact_product_page, catalog_page, get_form_data, contacts_page, about_page, \
    production_page

urlpatterns = [
    path('', main_page_),
    path('main_page/<str:language>', main_page),
    path('exact-product/<int:pr_id>/<str:language>', exact_product_page),
    path('catalog/<str:language>/', catalog_page),
    path('get-form-data/<str:language>', get_form_data),
    path('contacts/<str:language>', contacts_page),
    path('about/<str:language>', about_page),
    path('production/<str:language>', production_page),
]
