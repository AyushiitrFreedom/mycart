from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="home"),
    path('checkout', views.checkout,name="checkout"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('productview', views.productview,name="productview"),
    path('search', views.search,name="search"),
    path('tracker', views.tracker,name="tracker"),
]
