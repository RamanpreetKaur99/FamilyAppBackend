from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'allfamilies/', views.AllFamilies.as_view()),
    url(r'viewfamily/', views.ViewFamily.as_view()),
    url(r'viewuser/(?P<username>[\w-]+)/', views.ViewUser.as_view()), 
]