from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_model_list_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('blog/<str:pk>/', views.post_model_detail_view, name='blog'),
    path('create', views.post_model_create_view, name='create'),
    path('blog/<str:pk>/edit', views.post_model_update_view, name="update"),
    path('blog/<str:pk>/delete', views.post_model_delete_view, name="delete")
]
