from django.urls import path 

from  . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('how-it-works/', views.HowitWorks.as_view(), name='how-it-works'),
    path('faq/', views.Faq.as_view(), name='faq'),
    path('writers/', views.Writers.as_view(), name='writers'),
    path('reviews/',  views.Reviews.as_view(), name='reviews')

]