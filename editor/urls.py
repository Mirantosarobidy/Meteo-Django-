from django.urls import path
from .views import( BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)

urlpatterns = [
    path('editor/<int:pk>/delete/', BlogDeleteView.as_view(), name='editor_delete'),
    path('editor/<int:pk>/edit', BlogUpdateView.as_view(), name='editor_edit'),
    path('editor/new/', BlogCreateView.as_view(), name='edit_new'),
    path('editor/<int:pk>/', BlogDetailView.as_view(),
         name='editor_detail'),
    path('', BlogListView.as_view(), name='home'),
]
