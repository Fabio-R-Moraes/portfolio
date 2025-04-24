from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<int:id>/', views.product, name='product'),
    path('portfolio/about.html', views.about, name='about'),
    path('portfolio/curriculum.html', views.curriculum, name='curriculum'),
    path('portfolio/contact.html', views.contact, name='contact'),
]

