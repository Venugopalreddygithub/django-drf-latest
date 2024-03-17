from django.urls import path
from tags.views import CreateTagView, TagDetailv1, TagDetailViewv2, DeleteTagView1, DeleteTagView2 

urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create-tag'),
    path('tag-detail/v1/<str:slug>', TagDetailv1.as_view(), name='tag-detail-v1'),
    path('tag-detail/v2/<str:slug>', TagDetailViewv2.as_view(), name='tag-detail-v2'),
    path('tag-delete/v1/<str:slug>', DeleteTagView1.as_view(), name='tag-delete-v1'),
    path('tag-delete/v2/<str:slug>', DeleteTagView2.as_view(), name='tag-delete-v2'),
]
