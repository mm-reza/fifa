from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', views.PostListView, name='blog-home'),
    path('scores/', views.Scores, name='scores'),
    # path('super16/', views.Super16, name='super16'),
    path('predict/', views.QuarterFinal, name='predict'),
    # path('quiz/', views.Quiz, name='quiz'),
    # path('predictions/', views.Predictions, name='predictions'),
    # path('final/', views.Final, name='final'),
    # path('', PostListView.as_view(), name='blog-home'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('ajax/load-teams/', views.load_teams, name='ajax_load_teams'), # AJAX
]