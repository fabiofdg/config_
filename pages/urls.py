from django.urls import path
from .views import HomePageView, AboutPageView, BasePageView  #homePageView,

urlpatterns = [
    #path('', homePageView, name='home'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('base/', BasePageView.as_view(), name='base')

]