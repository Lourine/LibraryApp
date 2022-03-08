=====
Libary App
=====

Library App is a django  application that enables  a  crud operation using MVT architecture(django views and templates). It also exposes a Rest Framework API that enables a user to perform all crud operations as well. It also implents api authentication using jwt tokens

Quick start
-----------

1. Add "sil_django_scrapper" to INSTALLED_APPS:
  INSTALLED_APPS = [
    ...
    'sil_django_scrapper'
  ]

2. Include the sil_django_scrapper URLconf in your project urls.py like this::

    path('sil_django_scrapper/', include('sil_django_scrapper.urls')),

3. Run ``python manage.py migrate`` to create the sil_django_scrapper models.

4. Start the development server and visit http://127.0.0.1:8000/webscarpper/ to view your app

