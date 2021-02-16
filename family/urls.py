from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'allgroceryitems/(?P<username>[\w-]+)/', views.AllGroceryItems.as_view()),
    url(r'viewgroceryitem/(?P<id>[\w-]+)/', views.ViewGroceryItem.as_view()),
    url(r'alltodoitems/(?P<username>[\w-]+)/', views.AllToDoItems.as_view()),
    url(r'viewtodoitem/(?P<id>[\w-]+)/', views.ViewToDoItem.as_view()),
    url(r'allevents/(?P<username>[\w-]+)/', views.AllEvents.as_view()),
    url(r'allbills/(?P<username>[\w-]+)/', views.AllBills.as_view()),
    url(r'viewbills/(?P<id>[\w-]+)/', views.ViewBills.as_view()),
    url(r'viewevent/(?P<id>[\w-]+)/', views.ViewEvent.as_view()), 
]