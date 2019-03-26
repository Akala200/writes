from django.urls import path , include

from  . import views

app_name = 'united_kingdom'


services_patterns = [
    path('custom-essay/', views.ServicesCustomEssay.as_view(), name='custom_essay'),
    path('dissatation-writing/', views.ServicesDissatationWriting.as_view(), name='dissatation_writing'),
    path('essay-writing/', views.ServicesEssayWriting.as_view(), name='essay_writing'),
    path('research/', views.ServicesResearch.as_view(), name='research'),
    path('admission-essay/', views.ServicesAdmissionEssay.as_view(), name='admission_essay'),
    path('term-paper/', views.ServicesTermPaper.as_view(), name='term_paper'),
    path('custom-writing/', views.ServicesCustomWriting.as_view(), name='custom_writing'),
    path('write-myessay/', views.ServicesWriteMyEssay.as_view(), name='write_my_essay')
    
]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('how-it-works/', views.HowitWorks.as_view(), name='how_it_works'),
    path('faq/', views.Faq.as_view(), name='faq'),
    path('writers/', views.Writers.as_view(), name='writers'),
    path('reviews/',  views.Reviews.as_view(), name='reviews'),
    path('services/', include(services_patterns)),
    path('about/', views.About.as_view(), name='about')

]