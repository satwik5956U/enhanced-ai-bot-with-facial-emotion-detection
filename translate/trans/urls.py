from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('index1',views.index1,name="index1"),
    path('speechpage',views.speechpage,name='speechpage'),
    path('translate',views.trans,name='translate'),
    #path('speakspeech',views.speakspeech,name='speakspeech'),
    path('respond',views.respond,name="respond"),
    path('signup',views.signup,name="signup"),
]