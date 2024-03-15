from django.urls import path
from tags.views import CreateTagView 

urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create-tag')
]
