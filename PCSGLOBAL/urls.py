from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.signup, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup_page, name='signup'),
    path('about', views.about, name='about'),
    path('data_science', views.data_science, name='data_science'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('industry', views.industry, name='industry'),
    path('products', views.products, name='products'),
    path('services', views.services, name='services'),
    path('careers', views.careers, name='careers'),
    path('contact_us', views.contact, name='contact'),
    path('user_home', views.user_home, name='user_home'),
    path('admin', views.admin, name='admin'),

]