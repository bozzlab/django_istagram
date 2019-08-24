from django.urls import path
from .views import CreatePostView, ListPointView

urlpatterns = [ 
    path("", ListPointView.as_view(), name = "list_post"),
    path("new/", CreatePostView.as_view(), name = "new_post")
]