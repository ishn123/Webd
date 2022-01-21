"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.store,name='Store'),
    path('cart',view.cart,name='Cart'),
    path('checkout',view.checkout,name='Checkout'),
    path('about',view.aboutus,name='About'),
    path('disinfectants',view.disinfectants,name='Disinfec'),
    path('sanitizers',view.sanitizers,name='Sani'),
    path('households',view.Households,name='house'),
    path('cosematics',view.cosematics,name='cose'),
    path('collect',view.collect,name='collect')
]
