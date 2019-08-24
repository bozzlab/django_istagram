from django.urls import path
from .views import ProfileDateilView

urlpatterns = [ 
    path('<str:username>',ProfileDateilView.as_view(), name = "profile_detail"),
]