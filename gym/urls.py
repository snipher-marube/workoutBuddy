from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('singe_blog/<slug:slug>/', views.single_blog, name='single_blog'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('pricing/', views.pricing, name='pricing'),
    path('search/', views.search, name='search'),

]
