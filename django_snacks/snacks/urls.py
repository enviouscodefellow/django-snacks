from django.urls import path

from .views import AboutView, HomepageView

urlpatterns = [
  path('', HomepageView.as_view(), name='home'),
  path('about', AboutView.as_view(), name='about')
]