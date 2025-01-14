from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.home, name='home'),
   path('subscribe/', views.subscribe, name='subscribe'),
   path('profile/', views.profile, name='profile'),
   path('register/', views.register, name='register'),
   path('login/', views.user_login, name='login'),
   path('logged_out/', views.user_logout, name='logged_out'),
   path('accounts/password_reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
   path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
   path('accounts/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
   path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
   path('filter/<int:tag_id>/', views.filter_photos_by_tag, name='filter_photos_by_tag'),
   path('like/<int:photo_id>/', views.like_photo, name='like_photo'),
   path('dislike/<int:photo_id>/', views.dislike_photo, name='dislike_photo'),
   path('update-profile/', views.update_profile, name='update_profile'),
   path('upload/', views.upload_photo, name='upload_photo'),
   path('delete_photo/<int:pk>/', views.delete_photo, name='delete_photo'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)